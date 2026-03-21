## Create day05_file_reader.py that opens a sample 
## log file and counts the number of lines.

file_path = "sample.log"

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            count = 0
            for line in file:
                count += 1
            return count
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return 0

line_count = count_lines(file_path)
print(f"Total lines in {file_path}: {line_count}")