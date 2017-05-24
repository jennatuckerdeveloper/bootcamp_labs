print("Welcome to your phonebook!")

phonebook = {'Jen': {
    'name': 'Jen',
    'number': 4443332222,
    'relationship': 'self'
}, 'Elizabeth' : {
    'name': 'Elizabeth',
    'number': 5552229999,
    'relationship': 'wife'
}, 'Rose' : {
    'name': 'Veronica',
    'number': 8887775555,
    'relationship': 'sister'
}}

def new_contact(name, number, relationship):
    new = {}
    new['name'] = name
    new['number'] = number
    new['relationship'] = relationship
    phonebook[name] = new
    print(new)

def retrieve_contact(name):
    print(phonebook[name])

def remove_contact(name):
    del phonebook[name]
    print(name + " removed.")

def change_contact(name, change, new):
    if change == 'name':
        phonebook[name]['name'] = new
    elif change == 'number':
        phonebook[name]['number'] = new
    elif change == 'relationship':
        phonebook[name]['relationship'] = new
    print(phonebook[name])

def run_phone_book():
    running = True
    while running:
        try:
            query = int(input("""What would you like to do:
                1. Look up a number
                2. Enter a new contact
                3. Update an existing contact
                4. Delete a contact
                5. Quit Phonebook
                >> """))
        except ValueError:
        #this allows your progam to keep running
        #otherwise, Python would kick the user out and stop running
            print('I did not understand that')
            continue
        if query == 1:
            name = input("Enter the name of the contact you want to retrieve: ")
            retrieve_contact(name)
        elif query == 2:
            name = input("Enter a name for your new contact: ")
            number = input("Enter a number for your new contact: ")
            relationship = input("Enter a relatoinship for your new contact: ")
            new_contact(name, number, relationship)
        elif query == 3:
            name = input("Enter the name of the contact you want to change: ")
            change = input("Do you want to change the name, number, or relationship? ")
            new = input("Enter the updated info: ")
            change_contact(name, change, new)
        elif query == 4:
            name = input("What is the name of the contact you want to remove? ")
            remove_contact(name)
        elif query == 5:
            quit()
        else:
            print("I didn't understand that.")

run_phone_book()
