phonebook = [{'Name:': 'Jen', 'Number:': '111-111-1111', 'Relationship:': 'self'},
    {'Name:': 'Elizabeth', 'Number:': '222-222-2222', 'Relationship:': 'wife'},
    {'Name:': 'Rose', 'Number:': '333-333-3333', 'Relationship:': 'mama'}]

phonebook.append({'Name:': 'Veronica', 'Number:': '444-444-4444', 'Relationship:':
    'sister'})

#for contact in phonebook:
    #print(type(contact))
    #prints dictionaries

#for contact in phonebook:
    #print(contact)

for contact in phonebook:
    for key in contact:
        print(key, contact[key])
        #That worked!  It printed the key-value pair on separate lines as strings

for contact in phonebook:
    for key in contact:
        if key == "Name:":
            print(contact[key])
