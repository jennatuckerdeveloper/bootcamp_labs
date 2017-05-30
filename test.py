import csv
with open("crime_incident_data_2011.csv") as csvfile:
    #opens the CSV file
    reader = csv.DictReader(csvfile)
    #runs the csv.DictReader on the csvfile and saves it to a variable
    crimes = {}
    for item in reader:
        #iterates through the dictionaries in the csv_file
        #print(row) --> test to show that the csvfile outputs to terminal
        #appears to print with rows as dictionaries
        if item['Major Offense Type'] not in crimes:
            #this iterates through the keys of the items to see if they're in my dict
            crimes[item['Major Offense Type']] = 1
            #if the key is not in my dict, the key is added with a value of 1
        elif item['Major Offense Type'] in crimes:
            crimes[item['Major Offense Type']] += 1
            #if the key is already in my dict, the value gets 1 added
    #the output should be a new dict called crimes with Major Offense Types as keys
    #and the number of occurances as values
    #print(crimes) --> test to ensure the new dictionary prints properly
