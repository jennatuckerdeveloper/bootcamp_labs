phonebook = [{
    'name': 'Jen',
    'number': 4443332222,
    'relationship': 'self'
}, {
    'name': 'Elizabeth',
    'number': 5552229999,
    'relationship': 'wife'
}, {
    'name': 'Veronica',
    'number': 8887775555,
    'relationship': 'sister'
}]

def new_contact(name, number, relationship):
    new = {}
    new['name'] = name
    new['number'] = number
    new['relationship'] = relationship
    phonebook.append(new)

new_contact('Rose', 8884441111, 'Mama')

def update_contact(name):
    name = phonebook[i].name
    return phonebook[i]
    

#def retrieve_contact(name):
    #for item in phonebook:
        #if name = phonebook['name']:

            #return items(phonebook[i])

#print(retrieve_contact('Rose'))
