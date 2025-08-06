import csv

with open("favorites.csv", "r") as file:
    #this will take data in the form of indexes
    #reader = csv.reader(file)

    #this will take data as key value pairs 
    reader = csv.DictReader(file)
    #to skip first row
    next(reader) 
    for row in reader:
        #it was priting all including heading
        #favorites = row[1]

        #this can print data using column name
        favorites = row["language"]
        print(favorites)

       