phonebook = {}
phonebook['Jen'] = "self"
phonebook['Elizabeth'] = "wife"
phonebook['Veronica'] = "sister"

print(phonebook) #prints the dictionary with key, value pairs separated by commas
print(phonebook.items())
#this prints the lable dict_items, then it prints what looks like a tuple of
#an array of tuples holding key-value pairs.  wtf???
print(type(phonebook.items()))
#the class is dict_items

print(phonebook.keys()) #this prints what looks like a tuple of an array of keys
print(phonebook.values())#this prints what looks like a tuple of an array of values

for key in phonebook:
    print(key, phonebook[key])
#this prints simple strings of the key and value pairs each on one line

for key in phonebook:
     print(key)
#this prints the keys as simple strings, each on one line
for i in phonebook:
    print(i)
#same as above
for key in phonebook:
    print(phonebook[key])
#this prints values as simple strings, each on one line
for i in phonebook:
    print(phonebook[i])
#same as above
print(phonebook['Jen'])
    #this prints the value
