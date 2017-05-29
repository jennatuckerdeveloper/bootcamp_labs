phonebook = [{'Name:': 'Jen', 'Number:': '111-111-1111', 'Relationship:': 'self'},
    {'Name:': 'Elizabeth', 'Number:': '222-222-2222', 'Relationship:': 'wife'},
    {'Name:': 'Rose', 'Number:': '333-333-3333', 'Relationship:': 'mama'}]

phonebook.append({'Name:': 'Veronica', 'Number:': '444-444-4444', 'Relationship:':
    'sister'})

for contact in phonebook:
    for key in contact:
        if contact[key] == "Jen":
            contact['Number:'] = "7777777777"
            contact['Relationship:'] = "Queen"
            print(contact)
