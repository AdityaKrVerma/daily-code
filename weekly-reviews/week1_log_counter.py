## Build week1_log_counter.py. 
## The program should read a log file, 
## count INFO/WARN/ERROR, print totals, and gracefully handle a missing file.

import argparse
from pathlib import Path
import sys


LEVELS = ("INFO", "WARN", "ERROR")


def count_log_levels(log_path: Path) -> dict[str, int]:
    """Return counts for INFO, WARN, and ERROR in the given log file."""
    counts = {level: 0 for level in LEVELS}

    with log_path.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            for level in LEVELS:
                if level in line:
                    counts[level] += 1
                    break

    return counts


def print_totals(counts: dict[str, int]) -> None:
    """Print log level totals in a readable format."""
    print("Log level totals:")
    for level in LEVELS:
        print(f"{level}: {counts[level]}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Count INFO, WARN, and ERROR entries in a log file."
    )
    parser.add_argument("log_file", help="Path to the log file to read")
    args = parser.parse_args()

    log_path = Path(args.log_file)

    if not log_path.exists():
        print(f"Error: File not found: {log_path}", file=sys.stderr)
        return 1

    if not log_path.is_file():
        print(f"Error: Not a file: {log_path}", file=sys.stderr)
        return 1

    counts = count_log_levels(log_path)
    print_totals(counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())