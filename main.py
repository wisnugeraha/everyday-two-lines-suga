#!/usr/bin/env python3
"""The Toaster's Brown Coat — make.fun entry for [u-suga-everyday-things-two-lines-longer-run-f8734479].

Two lines: line 1 explains a toaster to a 10-year-old with one vivid analogy;
line 2 says in one sentence why the analogy works — what it maps, what it leaves out.
Writes the entry to /output/entry.txt.
Gate: UTF-8 text, 1..400 characters, not only white space.
"""
import os
import sys

ENTRY = """A toaster is a tiny oven that only knows how to make bread wear a brown coat: glowing wires hug it until the outside crisps, then a spring pops it up when the coat fits.
The hug maps the wires' heat browning just the surface; it leaves out that a real coat warms you through — a toasted crumb is still cold bread at heart."""
MAX_CHARS = 400
OUT = "/output/entry.txt"


def entry_text() -> str:
    text = ENTRY.strip("\n")
    if not text.strip():
        sys.exit("entry is only white space")
    if len(text) > MAX_CHARS:
        sys.exit(f"entry is {len(text)} chars, gate allows at most {MAX_CHARS}")
    return text


def emit(text: str, out: str = OUT) -> None:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(out, 0o644)


def report() -> dict:
    """Read the emitted file back and confirm bytes vs the gate's cap."""
    with open(OUT, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8")
    return {"bytes": len(data), "chars": len(text), "within_cap": len(text) <= MAX_CHARS}


def main() -> None:
    text = entry_text()
    emit(text)
    rep = report()
    print(f"wrote {OUT}: {len(text)} chars, {rep['bytes']} bytes, cap {MAX_CHARS} ok={rep['within_cap']}")


if __name__ == "__main__":
    main()
