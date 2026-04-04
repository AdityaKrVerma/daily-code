## Create day03_functions.py with at least 
## three small functions such as greet_user(name), 
## square_number(n), and classify_severity(level).

def greet_user(name="friend"):
    print(f"Hello there {name}!")

def square_number(n):
    return n * n

def classify_severity(level):
    if level < 3:
        return "Low"
    elif level < 7:
        return "Medium"
    else:
        return "High"

greet_user("Aditya")
print(f"Square of 25 is {square_number(25)}")
print(f"Severity level of 8 is classified as {classify_severity(8)}")