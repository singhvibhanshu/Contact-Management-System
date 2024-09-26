import json


output = []


def add_contact():
    name = input("Name: ")
    age = input("Age: ")
    phone_no = input("Phone Number: ")
    email = input("Email: ")

    person_dictionary = {
        "Name": name,
        "Age": age,
        "Phone_Number": phone_no,
        "Email": email,
    }
    return person_dictionary


def del_contact(contact_list):
    display_contact(contact_list)

    while True:
        s_no = input("Enter the serial number of the contact you wish to delete: ")
        try:
            s_no = int(s_no)
            if s_no <= 0 or s_no > len(contact_list):
                print("Invalid serial number.")
            else:
                break
        except:
            print("Invalid input.")
    contact_list.pop(s_no - 1)
    print("Contact deleted successfully.")


def search(contact_list):
    choice = input(
        "Press '1' to search with the name OR Press '2' to search with phone number: "
    )
    if choice == "1":
        search_name = input("Enter the name: ").lower()
        for person_dictionary in contact_list:  # want to understand
            name = person_dictionary["Name"]
            if search_name in name.lower():
                output.append(person_dictionary)
    elif choice == "2":
        search_phone_no = input("Enter the phone number: ")
        for person_dictionary in contact_list:
            phone_no = person_dictionary["Phone_Number"]
            if search_phone_no in phone_no:
                output.append(person_dictionary)
    else:
        print("Invalid input.")


def display_contact(contact_list):
    for i, person_dictionary in enumerate(contact_list):
        print(
            i + 1,
            ":",
            person_dictionary["Name"],
            "|",
            person_dictionary["Age"],
            "|",
            person_dictionary["Phone_Number"],
            "|",
            person_dictionary["Email"],
        )


display_contact(output)


print("Hey! Welcome to the Contact Management System.")
print()

with open("contacts.json", "r") as f:
    contact_list = json.load(f)["contacts"]

while True:
    print()
    print("Size of the Contact List: ", len(contact_list))
    operation = input(
        "Which of the following actions do you wish to perform: 'Add', 'Delete' or 'Search' and 'Q' for quit: "
    ).lower()

    if operation == "add":
        person_dictionary = add_contact()
        contact_list.append(person_dictionary)
        print("Person added successfully.")
    elif operation == "delete":
        del_contact(contact_list)
    elif operation == "search":
        search(contact_list)
    elif operation == "q":
        break
    else:
        print("Invalid operation choosen.")

        with open("contacts.json", "w") as f:
            json.dump({"contacts": contact_list}, f)
