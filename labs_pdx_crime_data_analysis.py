import csv
def crime_stats(data_file):
        year = ""
        with open(data_file) as csvfile:
            reader = csv.DictReader(csvfile)
            crimes = {}
            for row in reader:
                year = row['Report Date'][-4:]
        #print(row['Major Offense Type'])
                if row['Major Offense Type'] in crimes:
                    crimes[row['Major Offense Type']] += 1
                else:
                    crimes[row['Major Offense Type']] = 1
    #print(crimes)
        lst = list(crimes.values())
        highest = max(lst)
        lowest = min(lst)
        year_total = sum(lst)
        print(year)
        for key, total in crimes.items():
            if total == highest:
                print("Highest crime: ", key, highest)
            elif total == lowest:
                print("Lowest crime: ", key, lowest)
        print("Total crimes: ", year_total)
        return {year : year_total}

years_list = ['crime_incident_data_2011.csv', 'crime_incident_data_2012.csv',
    'crime_incident_data_2013.csv', 'crime_incident_data_2014.csv',
    'crime_incident_data_recent.csv']
year_dict = {}
for file_name in years_list:
    temp = crime_stats(file_name)
    if list(temp.items())[0][0] not in year_dict:
        year_dict[list(temp.items())[0][0]] = int(list(temp.items())[0][1])
    else:
        year_dict[list(temp.items())[0][0]] += int(list(temp.items())[0][1])

lst = list(year_dict.values())
highest = max(lst)
for key, top in year_dict.items():
    if top == highest:
        print("Year with most crime: ", key, highest)
#take a look at the dictionary
#figure out how to choose the highest value
#items()
#list()

my_dict = {'key1' : 'value1', 'key2' : 'value2'}

#print(type(my_dict.items()))
#returns:  <class 'dict_items'>
#dict_items is it's own thing, and that thing is not idexable
#the rest of the code converts the dict_items into something idexable
#by turning it into a list

#print(my_dict.items()[0])
#returns:  TypeError: 'dict_items' object does not support indexing
print(list(my_dict.items()))
print(list(my_dict.items())[0])
print(list(my_dict.items())[0][0])
print(list(my_dict.items())[0][1])

variable = ('2015', '8573226')
