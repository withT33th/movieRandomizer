import csv

listOfMovies = []

with open("watchlist-witht33th-2024-12-31-02-25-utc.csv") as csv_file:
    csvReader = csv.reader(csv_file, delimiter = ',')
    next(csvReader) #skipping the header

    for row in csvReader:
        

    