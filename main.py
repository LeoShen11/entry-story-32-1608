#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to /output/entry.txt. The name has to land
a joke and imply a whole story in the few words a passer-by sees in a
phone's network list, in at most 32 characters.

Draft story: a breakup told through the router. She didn't just leave --
she took the dog, and she took the Wi-Fi too, so the whole flat went
dark and silent in one move. The ex, the dog, the network: a custody
battle where the internet is listed next to the pet.
"""

import os

STORY = "My ex took the dog AND the WiFi"

MAX_CHARS = 32


def main() -> None:
    text = STORY.strip()
    if not text:
        raise SystemExit("story is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"story is {len(text)} chars, over the {MAX_CHARS} limit")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back validation: what landed on disk must be byte-identical
    # to the story, non-blank, and within the 1..32 character gate.
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == text, f"read-back mismatch: {back!r} != {text!r}"
    assert 1 <= len(back) <= MAX_CHARS, f"read-back is {len(back)} chars"
    assert back.strip(), "read-back is only whitespace"
    print(f"read-back OK: {len(back)} chars: {back!r}")
    print(f"wrote {len(text)} chars to {path}: {text!r}")


if __name__ == "__main__":
    main()
