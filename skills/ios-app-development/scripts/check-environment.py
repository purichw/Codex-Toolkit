#!/usr/bin/env python3
"""Read-only iOS toolchain inventory. No installs, builds, network fetches or device access.

Exit 0 means an inventory was produced, not that the project can build.
Exit 2 means invalid input. Optional Android checks never gate iOS results.
"""
import argparse
import json
import os
import platform
from pathlib import Path
import shutil
import subprocess


def probe(argv, cwd, json_output=False):
    executable = shutil.which(argv[0])
    if not executable:
        return {"status": "not_on_PATH"}
    try:
        result = subprocess.run([executable, *argv[1:]], cwd=cwd, capture_output=True,
                                text=True, timeout=15, check=False)
        if json_output and result.returncode == 0:
            try:
                return {"status": "observed", "data": json.loads(result.stdout)}
            except ValueError:
                return {"status": "invalid_json", "output": (result.stdout + result.stderr).strip()[:3000]}
        return {"status": "observed" if result.returncode == 0 else "failed",
                "exit_code": result.returncode,
                "output": (result.stdout + result.stderr).strip()[:3000]}
    except subprocess.TimeoutExpired:
        return {"status": "timed_out"}
    except OSError as error:
        return {"status": "failed", "error": type(error).__name__}


def project_manifest(path):
    if not path.is_file():
        return None
    try:
        if path.stat().st_size > 1_000_000:
            return {"status": "too_large_to_inspect"}
        data = json.loads(path.read_text())
        if not isinstance(data, dict):
            return {"status": "invalid_manifest"}
        packages = {}
        for group in ("dependencies", "devDependencies"):
            if isinstance(data.get(group), dict):
                packages.update(data[group])
        return {"status": "observed", "packageManager": data.get("packageManager"),
                "engines": data.get("engines"),
                "dependencies": {key: packages[key] for key in
                                 ("expo", "react-native", "react", "typescript", "expo-dev-client") if key in packages}}
    except (OSError, ValueError, UnicodeError):
        return {"status": "unreadable_or_invalid_manifest"}


def child_directories(path):
    try:
        return sorted(item.name for item in path.iterdir() if item.is_dir())[:50]
    except OSError:
        return []


def inventory(project, app, android=False):
    mac = platform.system() == "Darwin"
    result = {
        "kind": "read_only_environment_inventory", "build_readiness": "not_verified",
        "project": str(project), "app": str(app),
        "host": {"system": platform.system(), "release": platform.release(),
                 "process_architecture": platform.machine(),
                 "free_disk_gib": round(shutil.disk_usage(project).free / (1024 ** 3), 1)},
        "manifests": {"root": project_manifest(project / "package.json"),
                      "app": project_manifest(app / "package.json")},
        "lockfiles": {}, "project_files": {},
        "tools_on_PATH": {tool: shutil.which(tool) for tool in
                          ("git", "node", "npm", "pnpm", "yarn", "bun", "ruby", "bundle", "pod")},
        "probes": {},
        "notes": ["No installation, build, license acceptance, shell edits or phone access performed.",
                  "Package-manager shims were not executed; this avoids implicit downloads.",
                  "Compare observed tools with this project's pins; PATH absence does not prove absence on disk.",
                  "Signing, physical feature behavior and release readiness are not checked."],
    }
    for label, root in (("root", project), ("app", app)):
        result["lockfiles"][label] = [name for name in
            ("pnpm-lock.yaml", "package-lock.json", "yarn.lock", "bun.lock", "bun.lockb") if (root / name).is_file()]
    result["project_files"] = {name: (app / name).exists() for name in
        ("app.json", "app.config.ts", "app.config.js", "pubspec.yaml", "Gemfile", "ios/Gemfile",
         "ios/Podfile", "ios/Podfile.lock", "android/gradlew", "ios", "android")}
    result["native_projects"] = sorted(str(path.relative_to(app)) for root in (app, app / "ios")
                                       for pattern in ("*.xcodeproj", "*.xcworkspace") for path in root.glob(pattern))
    pins = {}
    for label, root in (("root", project), ("app", app)):
        for name in (".nvmrc", ".node-version"):
            path = root / name
            if path.is_file():
                try:
                    pins[f"{label}/{name}"] = path.read_text()[:100].strip()
                except (OSError, UnicodeError):
                    pins[f"{label}/{name}"] = "unreadable"
    result["node_pins"] = pins
    for name, command in (("node_version", ["node", "--version"]), ("git_version", ["git", "--version"])):
        result["probes"][name] = probe(command, project)
    if mac:
        for name, command in (
            ("apple_silicon_capable", ["sysctl", "-n", "hw.optional.arm64"]),
            ("memory_bytes", ["sysctl", "-n", "hw.memsize"]),
            ("rosetta_translation", ["sysctl", "-n", "sysctl.proc_translated"]),
            ("developer_directory", ["xcode-select", "-p"]),
            ("xcode_version", ["xcodebuild", "-version"]),
        ):
            result["probes"][name] = probe(command, project)
        # Do not enumerate personal devices or trigger simulator/device boots.
        if result["probes"]["xcode_version"]["status"] == "observed":
            result["probes"]["ios_sdk_version"] = probe(["xcrun", "--sdk", "iphoneos", "--show-sdk-version"], project)
            runtime = probe(["xcrun", "simctl", "list", "runtimes", "--json"], project, json_output=True)
            if runtime["status"] == "observed":
                try:
                    result["simulator_runtimes"] = [
                        {"name": r.get("name"), "version": r.get("version"), "available": r.get("isAvailable")}
                        for r in runtime["data"].get("runtimes", [])]
                except (AttributeError, TypeError):
                    result["simulator_runtimes"] = {"status": "unreadable"}
            else:
                result["simulator_runtimes"] = runtime
    else:
        result["notes"].append("Local Xcode/iOS Simulator builds require macOS; consider a supported remote build only if in scope.")
    if android:
        candidates = [os.environ.get("ANDROID_HOME"), os.environ.get("ANDROID_SDK_ROOT")]
        if mac:
            candidates.append(str(Path.home() / "Library/Android/sdk"))
        sdk = next((Path(value).expanduser() for value in candidates if value and Path(value).expanduser().is_dir()), None)
        result["android"] = {"scope": "optional_local_android", "sdk_path": str(sdk) if sdk else None,
            "adb_on_PATH": shutil.which("adb"), "java_on_PATH": shutil.which("java"),
            "installed": {name: child_directories(sdk / name) for name in ("platforms", "build-tools", "ndk", "cmdline-tools")} if sdk else {},
            "licenses": "not_accepted_or_checked", "compatibility": "compare_with_project_Gradle_AGP_and_SDK_pins"}
        if mac:
            result["android"]["installed_jdks"] = probe(["/usr/libexec/java_home", "-V"], project)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Existing repository/project directory")
    parser.add_argument("--app", default=".", help="App path within the project, relative or absolute")
    parser.add_argument("--android", action="store_true", help="Also inspect optional local Android tooling")
    args = parser.parse_args()
    project = Path(args.project).expanduser().resolve()
    app_arg = Path(args.app).expanduser()
    app = (app_arg if app_arg.is_absolute() else project / app_arg).resolve()
    if not project.is_dir() or not app.is_dir() or not app.is_relative_to(project):
        parser.error("--project and --app must be existing directories, with the app inside the project")
    print(json.dumps(inventory(project, app, args.android), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
