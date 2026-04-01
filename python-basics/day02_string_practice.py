## that joins first name and last name,
## counts characters, and prints the name in upper and lower case

first_name = input("Enter your First name: ")
last_name = input("Enter your Last name: ")

full_name = first_name + " " + last_name

char_count = len(full_name)

print(f"Full Name: {full_name}")
print(f"Character count: {char_count}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")