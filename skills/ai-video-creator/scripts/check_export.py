"""Check a local video export with ffprobe and ffmpeg."""

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def probe(path):
    data = json.loads(run("ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)))
    streams = data["streams"]
    video = [stream for stream in streams
             if stream["codec_type"] == "video" and not stream.get("disposition", {}).get("attached_pic")]
    audio = [stream for stream in streams if stream["codec_type"] == "audio"]
    if not video:
        raise ValueError(f"No video stream in {path}")
    duration = float(data["format"].get("duration", "nan"))
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError(f"No finite positive duration reported for {path}")
    return duration, video[0], audio


def picture_digest(path, stream):
    packets = run("ffmpeg", "-nostdin", "-v", "error", "-i", str(path), "-map", f"0:{stream['index']}",
                  "-c", "copy", "-f", "framehash", "-")
    return hashlib.sha256(packets.encode()).hexdigest()


def positive_seconds(value):
    seconds = float(value)
    if not math.isfinite(seconds) or seconds <= 0:
        raise argparse.ArgumentTypeError("Expected finite positive seconds")
    return seconds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--require-audio", action="store_true", help="Require an audio stream")
    parser.add_argument("--max-seconds", type=positive_seconds, help="Maximum allowed container duration")
    parser.add_argument("--decode", action="store_true", help="Fully decode the selected video and audio streams")
    parser.add_argument("--same-video-as", type=Path, help="Compare encoded video packets and timing to a reference video")
    args = parser.parse_args()

    try:
        duration, video, audio = probe(args.file)
        if args.require_audio and not audio:
            raise ValueError(f"No audio stream in {args.file}")
        if args.max_seconds is not None and duration > args.max_seconds:
            raise ValueError(f"Duration {duration:.3f}s exceeds {args.max_seconds:.3f}s")
        if args.same_video_as:
            _, reference_video, _ = probe(args.same_video_as)
            if picture_digest(args.file, video) != picture_digest(args.same_video_as, reference_video):
                raise ValueError("Encoded video packets or timing differ from the reference")
        if args.decode:
            maps = [part for stream in [video, *audio] for part in ("-map", f"0:{stream['index']}")]
            run("ffmpeg", "-nostdin", "-v", "error", "-xerror", "-i", str(args.file), *maps, "-f", "null", "-")
    except subprocess.CalledProcessError as error:
        parser.exit(1, f"{error.stderr.strip() or str(error)}\n")
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"{error}\n")

    print(json.dumps({
        "file": str(args.file),
        "duration_seconds": duration,
        "width": video.get("width"),
        "height": video.get("height"),
        "video_codec": video.get("codec_name"),
        "audio_streams": len(audio),
        "full_decode_checked": args.decode,
        "encoded_video_compared": args.same_video_as is not None,
    }))


if __name__ == "__main__":
    sys.exit(main())
