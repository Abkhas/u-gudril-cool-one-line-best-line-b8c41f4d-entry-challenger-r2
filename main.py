#!/usr/bin/env python3
"""One Line, Best Line — challenger-r2 entry (d2-burnt-toast).

Writes the locked one-line entry to <output>/entry.txt and exits 0.
Standard library only. No rendering, no network, no reads beyond this file.
"""

import os
import sys

LINE = "The last thing my mother ever cooked was burnt toast, and I have spent ten years trying to burn it exactly the same way."


def pick_target_dir():
    """Return the directory that should receive entry.txt."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    if not 1 <= len(LINE) <= 240:
        print("entry line must be 1-240 characters, got %d" % len(LINE))
        return 1
    target_dir = pick_target_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
