"""Roast Your Own Agent entry writer.

Reads the single-line roast from entry.txt next to this file and writes
it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt with one direct write.
Stdlib only; no temporary files, no rename, no shelling out.
"""
import os

here = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(here, "entry.txt"), "rb") as f:
        data = f.read()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)
except OSError as exc:
    raise SystemExit(f"roast entry: cannot copy entry.txt to output dir: {exc}") from exc
