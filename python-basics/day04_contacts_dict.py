## Create day04_contacts_dict.py storing names 
## to phone numbers in a dictionary.

telebook = {}

def add_contact(name, num):
    telebook[name] = num
    print(f"Added {name}:{num}")

def get_phone_number(name):
    return telebook.get(name, "Contact not found")

def display_all_contacts():
    if not telebook:
        print("No contacts added")
    else:
        for name, num in telebook.items():
            print(f"{name}: {num}")

add_contact("Aditya","0123456789")
add_contact("Ashley","9876543210")
add_contact("Aidan","2468013579")

display_all_contacts();

print(f"Ashley's phone number is: {get_phone_number("Aidan")}")
print(f"Aidan's phone number is: {get_phone_number("Ashley")}")