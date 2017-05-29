#phonebook lab using a list/array of dictionaries

phonebook = [{'Name:': 'Jen', 'Number:': '111-111-1111', 'Relationship:': 'self'},
    {'Name:': 'Elizabeth', 'Number:': '222-222-2222', 'Relationship:': 'wife'},
    {'Name:': 'Rose', 'Number:': '333-333-4444', 'Relationship:': 'mama'}]

phonebook.append({'Name:': 'Veronica', 'Number:': '444-444-4444', 'Relationship:':
    'sister'})

#C.R.U.D.
#Create, Retrieve, Update, Delete

#Create
def create_contact():
    name = input("Enter the name of the new contact: ")
    number = input("Enter the number of the new contact: ")
    relationship = input("Enter the relationship of the new contact: ")
    phonebook.append({"Name:": name, "Number:": number, "Relationship:":
        relationship})
    #This is just to show the entered contact
    for contact in phonebook:
        if contact['Name:'] == name:
            print("\nNew contact entered: \n")
            for key in contact:
                print(key, contact[key])
            print("\n")

#Retrieve
#This version should find all the entries with whatever portion of info is entered
def retrieve_contact():
    info = input("Enter a name, number, or relationship to lookup: ")
    for contact in phonebook:
        for key in contact:
            if contact[key] == info:
                print("\n")
                print("Name:", contact["Name:"])
                print("Number:", contact["Number:"])
                print("Relationship:", contact["Relationship:"])
                print("\n")
            elif info in contact[key]:
                print("\n")
                print("Name:", contact["Name:"])
                print("Number:", contact["Number:"])
                print("Relationship:", contact["Relationship:"])
                print("\n")
#Update
def update_contact():
    person = input("Enter the name of the contact you want to change: ")
    for contact in phonebook:
        for key in contact:
            if contact[key] == person:
                print("This is the current info: ")
                print("\n")
                print("Name:", contact["Name:"])
                print("Number:", contact["Number:"])
                print("Relationship:", contact["Relationship:"])
                print("\n")
    new_number = input("Enter the updated number: ")
    new_relationship = input("Enter the new relationship: ")
    for contact in phonebook:
        for key in contact:
            if contact[key] == person:
                contact['Number:'] = new_number
                contact['Relationship:'] = new_relationship
                print("\n")
                print("Here is the updated info: \n")
                for key in contact:
                    print(key, contact[key])
                print("\n")

#Delete
def delete_contact():
    person = input("Enter the name of the contact you want to delete: ")
    for contact in phonebook:
        if contact['Name:'] == person:
            phonebook.remove(contact)
            print(person, "removed.")
            #the del command did not work on this, only remove worked

while True:
    #create a while loop
    try:
    #create a try-except phrase at the same indentation
        #create a variabe with your input / menu, indent
        choice = input("""Welcome to phonebook!
            1. Create a new contact
            2. Retrieve a contact
            3. Update a contact
            4. Delete a contact
            5. Print entire phonebook 
            6. Quit """)
    except ValueError:
        #put the exception on the same line with except, like wiht if / elif
        #give commands of what to do
        print("I did not understand that")
        continue
    if choice == "1":
        create_contact()
    elif choice == "2":
        retrieve_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("\n")
        for contact in phonebook:
            for key in contact:
                print(key, contact[key])
            print("\n")
    elif choice == "6":
        quit()
