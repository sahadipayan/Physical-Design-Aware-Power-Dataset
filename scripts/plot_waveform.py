"""Generate the README waveform from CSV measurements (standard library only)."""

import csv
from itertools import islice
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "Layout0" / "key0" / "Layout0.csv"
OUTPUT = ROOT / "assets" / "layout0-key0-waveform.svg"
SAMPLE_COUNT = 2000


def main():
    with SOURCE.open(newline="", encoding="utf-8") as handle:
        rows = list(islice(csv.DictReader(handle), SAMPLE_COUNT))
    times = [float(row["time"]) * 1e6 for row in rows]
    currents = [float(row["current"]) * 1e3 for row in rows]

    width, height = 1100, 420
    left, right, top, bottom = 88, 1060, 100, 340
    xmax = 1.0  # Show the initial microsecond.
    ymax = max(currents) * 1.12

    def x(value):
        return left + value / xmax * (right - left)

    def y(value):
        return bottom - value / ymax * (bottom - top)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        '<title id="title">Layout0 / key0 current waveform</title>',
        '<desc id="description">First 2,000 measurements from data/Layout0/key0/Layout0.csv. Time in microseconds and current in milliamperes. All selected samples are plotted in their original order.</desc>',
        '<rect width="1100" height="420" rx="12" fill="#ffffff"/>',
        '<g font-family="Segoe UI, Arial, sans-serif" fill="#172b4d">',
        '<text x="88" y="39" font-size="23" font-weight="600">Layout0 / key0</text>',
        '<text x="88" y="66" font-size="14" fill="#52637a">Current waveform · first 2,000 samples · AES-GF</text>',
    ]
    for tick in range(6):
        value = ymax * tick / 5
        pos = y(value)
        parts.extend([
            f'<line x1="{left}" y1="{pos:.2f}" x2="{right}" y2="{pos:.2f}" stroke="#e6ebf2"/>',
            f'<text x="{left - 14}" y="{pos + 5:.2f}" text-anchor="end" font-size="13">{value:.2f}</text>',
        ])
    for tick in range(6):
        value = tick / 5
        pos = x(value)
        parts.extend([
            f'<line x1="{pos:.2f}" y1="{top}" x2="{pos:.2f}" y2="{bottom}" stroke="#eef1f6"/>',
            f'<text x="{pos:.2f}" y="{bottom + 26}" text-anchor="middle" font-size="13">{value:.1f}</text>',
        ])
    points = " ".join(f"{x(t):.3f},{y(c):.3f}" for t, c in zip(times, currents))
    parts.extend([
        f'<polyline points="{points}" fill="none" stroke="#2463b5" stroke-width="1.25" stroke-linejoin="round"/>',
        f'<path d="M {left} {top} V {bottom} H {right}" fill="none" stroke="#8796ab"/>',
        '<text x="574" y="402" text-anchor="middle" font-size="14">Time (µs)</text>',
        '<text x="25" y="220" text-anchor="middle" font-size="14" transform="rotate(-90 25 220)">Current (mA)</text>',
        '</g></svg>',
    ])
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)} from {len(rows):,} measurements.")


if __name__ == "__main__":
    main()
