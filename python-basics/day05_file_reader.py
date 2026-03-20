## Create day05_file_reader.py that opens a sample 
## log file and counts the number of lines.

file_path = "sample.log"

def count_log_lines(path):
    try:
        with open(path, 'r') as file:
            count = sum(1 for line in file)
        return count
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return 0

line_count = count_log_lines(file_path)
print(f"Total lines in {file_path}: {line_count}")