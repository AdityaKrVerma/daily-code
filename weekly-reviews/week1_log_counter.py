## Build week1_log_counter.py. The program should read a log file, 
## count INFO/WARN/ERROR, print totals, and gracefully handle a missing file.

from pathlib import Path

LOG_LEVELS = ["INFO","WARN","ERROR"]

def count_log_levels(filepath):
    counts = {level: 0 for level in LOG_LEVELS}

    with open(filepath, "r", encoding="utf-8") as log_file:
        for line in log_file:
            for level in LOG_LEVELS:
                if level in line:
                    counts[level] += 1
                    break

    return counts

def print_counts(counts):
    print("Below are each log counts")

    for level, count in counts.items():
        print(f"{level}: {count}")

def main():
    filename = input("Enter file name: ")
    filepath = Path(filename)

    try:
        counts = count_log_levels(filepath)
        print_counts(counts)
    
    except FileNotFoundError:
        print(f"Error: File '{filepath}' was not found")
    
if __name__ == "__main__":
    main()