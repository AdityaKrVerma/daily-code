## Create day05_exception_demo.py that 
## safely handles missing files or invalid numeric input.

def get_num():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter valid whole number.")
    else:
        print(f"The entered number is: {num}")

def open_file(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")

if __name__ == "__main__":
    get_num()
    file_path = input("Enter the file name/path: ")
    open_file(file_path)