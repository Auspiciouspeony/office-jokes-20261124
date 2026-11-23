"""office-jokes-20261124 — program/v1 entry.

One fixed one-line joke about office life, written to entry.txt in the
output directory. The grader reads exactly the bytes written: no trailing
newline, no second line.

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py

Deterministic: a single constant string; no randomness, no network,
no clock. Python 3.13, standard library only.
"""

import os
from pathlib import Path

# Two beats in one line. The setup names the office's most dreaded button
# — reply-all — and the complaint itself becomes the thing complained
# about: Legal, replying-all, turns the plea into company policy.
# Recognition (reply-all), surprise (it becomes policy), tight, fresh.
# v2: dropped "to say" — the colon lands the punchline faster.
JOKE = (
    "I hit reply-all asking everyone to stop replying all. "
    "Legal replied-all: my email is now company policy."
)


def _best_effort_chmod(path: Path, mode: int) -> None:
    """Chmod when the path is ours; never fail the run when it is not.

    In the grader the output directory is mounted by the grader and not
    owned by us, so chmod there raises PermissionError. The entry file
    itself is created by us, so its own chmod still applies.
    """
    try:
        path.chmod(mode)
    except OSError:
        pass


def run(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    _best_effort_chmod(output_dir, 0o755)
    entry = output_dir / "entry.txt"
    entry.write_text(JOKE, encoding="utf-8")
    # Outputs are collected by another user than the one running this
    # program, so the file must be world-readable.
    entry.chmod(0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))))
