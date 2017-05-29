phonebook = {}
phonebook['Jen'] = "self"
phonebook['Elizabeth'] = "wife"
phonebook['Veronica'] = "sister"

#print(phonebook['Jen'])
    #prints the value "self"
#for key in phonebook:
    #print(key)
#prints keys
#for key in phonebook:
    #print(phonebook[key])
#prints values

#for key in phonebook:
    #if key == "Jen":
        #print(key, phonebook[key])
        #prints key then value as strings:  Jen self
for key in phonebook:
    if phonebook[key] == "self":
        print(key)
        #prints the key Jen
