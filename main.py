"""Copy entry.png to output.png after a minimal JPEG check."""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "entry.png")
DST = os.path.join(ROOT, "output.png")


def validate(data):
    if data[:2] != b"\xff\xd8":
        return "missing JPEG SOI marker (FF D8)"
    if data[-2:] != b"\xff\xd9":
        return "missing JPEG EOI marker (FF D9)"
    if len(data) > 1048576:
        return "file larger than 1 MiB"
    pos = 2
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            return "bad JPEG marker"
        marker = data[pos + 1]
        if marker in (0xC0, 0xC2):
            height = int.from_bytes(data[pos + 5:pos + 7], "big")
            width = int.from_bytes(data[pos + 7:pos + 9], "big")
            if height > 1024 or width > 1024:
                return f"dimensions {width}x{height} exceed 1024"
            return None
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        size = int.from_bytes(data[pos + 2:pos + 4], "big")
        pos += 2 + size
    return "no SOF0/SOF2 segment found"


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    problem = validate(data)
    if problem is not None:
        print(f"error: invalid JPEG: {problem}", file=sys.stderr)
        return 1
    # JPEG files start with the SOI marker FF D8.
    if data[:2] != b"\xff\xd8":
        print("error: entry.png is not a JPEG (missing SOI)", file=sys.stderr)
        return 1
    with open(DST, "wb") as f:
        f.write(data)
    print(f"copied {len(data)} bytes: entry.png -> output.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
