
FILE_NAME = "contacts.txt"

def add_contact():
    print("\n--- Add New Contact ---")

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + phone + "|" + email + "\n")

    print("Contact added successfully!")

def view_contacts():
    print("\n--- All Contacts ---")

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("No contacts found.")

            for contact in contacts:
                name, phone, email = contact.strip().split("|")

                print("Name:", name)
                print("Phone:", phone)
                print("Email:", email)
                print("------------------")

    except FileNotFoundError:
        print("No contacts found.")

def search_contact():
    search_name = input("Enter name to search: ")

    found = False

    try:
        with open(FILE_NAME, "r") as file:

            for contact in file:
                name, phone, email = contact.strip().split("|")

                if search_name.lower() in name.lower():
                    print("Contact Found!")
                    print("Name:", name)
                    print("Phone:", phone)
                    print("Email:", email)

                    found = True

        if not found:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contacts available.")

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
