contacts = []

def add_contact(name, email):
    contact = {"name": name, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            print("Name:", contact["name"])
            print("Email:", contact["email"])
            break
    else:
        print("Contact not found.")

def edit_contact(name, email):
    for contact in contacts:
        if contact["name"] == name:
            contact["email"] = email
            print("Contact updated successfully!")
            break
    else:
        print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.")

def display_contacts():
    print("\nContacts:")
    for contact in contacts:
        print("Name:", contact["name"])
        print("Email:", contact["email"])
        print("")

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        add_contact(name, email)

    elif choice == "2":
        name = input("Enter name: ")
        search_contact(name)

    elif choice == "3":
        name = input("Enter name: ")
        email = input("Enter new email: ")
        edit_contact(name, email)

    elif choice == "4":
        name = input("Enter name: ")
        delete_contact(name)

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please try again.")
