#!/usr/bin/env python3
"""Create looping figure previews from authors' published figures, not simulated results.

Requires Pillow and ffmpeg with libx264. Run from any directory:
  python3 scripts/create_publication_previews.py --ffmpeg /path/to/ffmpeg
Source downloads are cached outside the repository. Each output includes provenance.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import tempfile
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SIZE = (960, 640)
FPS = 20
DURATION = 24
BLUE = "#1E3765"
SOURCES = {
    "field-guide-ball.jpeg": "https://arxiv.org/html/2610.19143v1/figures/tasks/ball_to_bowl_1.jpeg",
    "field-guide-cups.jpeg": "https://arxiv.org/html/2610.19143v1/figures/tasks/stack_cups_1.jpeg",
    "field-guide-block.jpeg": "https://arxiv.org/html/2610.19143v1/figures/tasks/pick_up_block_1.jpeg",
    "field-guide-marker.jpg": "https://arxiv.org/html/2610.19143v1/figures/tasks/remove_marker.jpg",
    "wmpa-overview.png": "https://junwei0102.github.io/wmpa-webpage/static/images/wmpa_overview.png",
    "wmpa-episode.png": "https://junwei0102.github.io/wmpa-webpage/static/images/episode_cube_double.png",
    "sparrow-intro.png": "https://arxiv.org/html/2609.21008v1/figures/intro.png",
    "sparrow-real.png": "https://arxiv.org/html/2609.21008v1/figures/real_world_sparrow.png",
}


def font(size):
    path = ROOT / "static/fonts/trade_gothic_lt_std_light.otf"
    return ImageFont.truetype(str(path), size)


def panel(image, title, caption):
    frame = Image.new("RGB", SIZE, "white")
    draw = ImageDraw.Draw(frame)
    draw.text((28, 15), title, font=font(32), fill=BLUE)
    draw.line((28, 59, 932, 59), fill="#dce2e9", width=2)
    region = (904, 488)
    fitted = ImageOps.contain(image, region, method=Image.Resampling.LANCZOS)
    frame.paste(fitted, ((SIZE[0] - fitted.width) // 2, 73 + (488 - fitted.height) // 2))
    draw.text((SIZE[0] // 2, 589), caption, anchor="mm", font=font(27), fill=BLUE)
    return frame


def scenes(images):
    field = [
        panel(images[name], "Adapting robot policies", caption)
        for name, caption in [
            ("field-guide-ball.jpeg", "Ball to bowl"),
            ("field-guide-cups.jpeg", "Stack cups"),
            ("field-guide-block.jpeg", "Block to cardboard"),
            ("field-guide-marker.jpg", "Remove marker"),
        ]
    ]
    episode = images["wmpa-episode.png"]
    boxes = [(6, 6, 318, 335), (337, 6, 648, 335), (669, 6, 979, 335),
             (998, 6, 1309, 335), (1329, 6, 1640, 335)]
    wmpa = [panel(images["wmpa-overview.png"], "World-Model Policy Arbiter", "Imagine futures, select a policy, act")]
    labels = ["HIQL: start", "GCIQL: reach the blue cube", "HIQL: blue cube placed",
              "GCIQL: stack the red cube", "Success: cubes stacked"]
    wmpa.extend(panel(episode.crop(box), "WMPA: an example episode", label)
                for box, label in zip(boxes, labels))
    intro = images["sparrow-intro.png"]
    real = images["sparrow-real.png"]
    sparrow = [
        panel(intro, "SPARROW", "Wait, observe, or reroute?"),
        panel(intro.crop((0, 0, 546, 610)), "SPARROW: mobile robot", "Jackal robot with LiDAR sensing"),
        panel(real.crop((20, 815, 803, 1547)), "SPARROW: a real-world encounter", "Navigation among temporary obstacles"),
    ]
    return {
        "attarian-2026-post-training": ("post-training", field, list(SOURCES)[:4]),
        "quan-2026-wmpa": ("wmpa", wmpa, ["wmpa-overview.png", "wmpa-episode.png"]),
        "sahak-2026-sparrow": ("sparrow", sparrow, ["sparrow-intro.png", "sparrow-real.png"]),
    }


def encode(ffmpeg, frames, output):
    command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo",
               "-pixel_format", "rgb24", "-video_size", "960x640", "-framerate", str(FPS),
               "-i", "pipe:0", "-an", "-c:v", "libx264", "-crf", "23", "-preset", "slow",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output)]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    try:
        length = DURATION * FPS / len(frames)
        for n in range(DURATION * FPS):
            position = n / length
            index = int(position)
            phase = position - index
            # Hold figures long enough to read, then dissolve into the next one.
            blend = max(0.0, (phase - 0.82) / 0.18)
            blend = (1 - math.cos(math.pi * blend)) / 2
            frame = Image.blend(frames[index], frames[(index + 1) % len(frames)], blend)
            process.stdin.write(frame.tobytes())
        process.stdin.close()
        if process.wait() != 0:
            raise RuntimeError(f"ffmpeg failed for {output}")
    except BaseException:
        process.kill()
        process.wait()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ffmpeg", default=shutil.which("ffmpeg"))
    parser.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / "leaf-publication-media")
    args = parser.parse_args()
    if not args.ffmpeg:
        parser.error("ffmpeg is required; install it or pass --ffmpeg")
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    images = {}
    for name, url in SOURCES.items():
        target = args.cache_dir / name
        if not target.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "LEAF-Lab-Website/1.0"})
            with urllib.request.urlopen(request, timeout=30) as response:
                target.write_bytes(response.read())
        with Image.open(target) as image:
            images[name] = ImageOps.exif_transpose(image).convert("RGB")
    for slug, (name, frames, sources) in scenes(images).items():
        bundle = ROOT / "content/publication" / slug
        folder = bundle / "result-candidates"
        folder.mkdir(exist_ok=True)
        output = folder / f"{name}-snippet.mp4"
        encode(args.ffmpeg, frames, output)
        frames[0].save(folder / f"{name}-poster.jpg", quality=88)
        frames[0].save(bundle / "featured.jpg", quality=88)
        (folder / "provenance.json").write_text(json.dumps({
            "kind": "animated-figure-preview",
            "description": "Published still figures presented with crossfades; not experimental video footage.",
            "sources": [{"file": source, "url": SOURCES[source]} for source in sources],
            "generator": "scripts/create_publication_previews.py",
            "duration_seconds": DURATION,
            "fps": FPS,
        }, indent=2) + "\n")
        print(f"Created {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes)", flush=True)


if __name__ == "__main__":
    main()
