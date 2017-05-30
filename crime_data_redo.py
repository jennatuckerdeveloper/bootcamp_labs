import csv
def crime_stats(data_file):
    year = ""
    with open(data_file) as csvfile:
        #opens the CSV file
        reader = csv.DictReader(csvfile)
        #runs the csv.DictReader on the csvfile and saves it to a variable
        crimes = {}
        for item in reader:
            #iterates through the dictionaries in the csv_file
            #print(row) --> test to show that the csvfile outputs to terminal
            #appears to print with rows as dictionaries
            year = item['Report Date'][-4:]
            #By looking at file, choses the key 'Report Date', starts 4 from end to end
            if item['Major Offense Type'] not in crimes:
                #this iterates through the keys of the items to see if they're in my dict
                crimes[item['Major Offense Type']] = 1
                #if the key is not in my dict, the key is added with a value of 1
            elif item['Major Offense Type'] in crimes:
                crimes[item['Major Offense Type']] += 1
                #if the key is already in my dict, the value gets 1 added
        #the output should be a new dict called crimes with Major Offense Types as keys
        #and the number of occurances as values
        lst = list(crimes.values())
        highest = max(lst)
        lowest = min(lst)
        year_total = sum(lst)
        print("Stats for the year: ", year)
        for key, total in crimes.items():
            if total == highest:
                print("Highest crime: ", key, highest)
            elif total == lowest:
                print("Lowest crime: ", key, lowest)
        print("\n")
        return[year, year_total]
            #--> test to ensure the new dictionary prints properly
#crime_stats("crime_incident_data_2011.csv") --> test of function
#crime_stats("crime_incident_data_2011.csv")
#crime_stats("crime_incident_data_2012.csv")
#crime_stats("crime_incident_data_2013.csv")
#crime_stats("crime_incident_data_2014.csv")
#crime_stats("crime_incident_data_recent.csv")

all_data = ["crime_incident_data_2011.csv", "crime_incident_data_2012.csv",
    "crime_incident_data_2013.csv", "crime_incident_data_2014.csv",
    "crime_incident_data_recent.csv"]
years = []

for file_name in all_data:
    temp = crime_stats(file_name)
    #this runs the function on every file in the list
    #each time, it returns a list of year, crimes that year
    years.append(temp)
    #now I have a list of lists with year, crimes that year
totals = []
for year in years:
    totals.append(year[1])
    #now I have a list/array of the crime totals alone
highest = max(totals)
    #so I can return the max to pull out that year and its total
for year in years:
    #iterates through my list of lists to find the highest crime total
    if year[1] == highest:
    #looks at the crime total
        print("Year with most crime: ", year[0], "Crime total: ", highest)
        #prints the year and the higheset 

#I am confident that the 2014 and recent files are indentical.
#This could be my own error.
#But the code all works.
