# Assets, motion, and custom/game-adjacent surfaces

Use only for work that needs imagery or motion. This is an original design/review workflow; verify
runtime APIs against the project's stack and [sources](sources.md). No artwork/font binaries are bundled.

Maintain an asset contract: source/provenance, permitted use, intrinsic size, crop/focal point,
transparency, scale behavior, loading/error fallback, and semantic role. For approved character/sprite
assets, preserve atlas coordinates, frame count, pivot, hit region and timing; do not guess or redraw
assets merely because implementation tooling cannot generate tasteful art.

Imagery must belong to the product and carry a purpose. A cozy illustrated game can be expressive,
while form text sits on a calm readable surface. A service app need not inherit the game style. Avoid
replacing all missing imagery with emoji or unrelated stock photos. Label missing assets and continue
with a neutral placeholder without claiming final art direction is validated.

For each consequential animation, define trigger, states, duration/easing source, interruption/reversal,
completion/cancel behavior and reduced-motion alternative. Native transitions should not fight system
back or sheet gestures. Avoid universal timing numbers and a spring on every interaction. Preserve
input responsiveness and do not block an urgent action until decorative motion completes.

Haptics/audio are supplemental feedback, not the only success/error signal. Verify meaningful events,
platform capability, user settings and repeat suppression; don't claim haptics feel good from a video.
For scrolling/animation performance, capture relevant device/build traces rather than claim smoothness
from an emulator screenshot or a fixed 60-fps target regardless of device.

Game-adjacent UI: test safe areas, finger occlusion, pause/background/resume, reduced motion where
applicable, rapid taps, hit areas and layering. A score panel should not cover the game task; an animated
avatar should not move the form's tap targets. Keep essential actions accessible outside purely decorative
or gesture-only surfaces when the product needs an equivalent path. Do not add a game engine to a normal app.
