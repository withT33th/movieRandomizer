import csv
import random

listOfMovies = []

# Adding a 'main' method
def main():

    with open("watchlist-witht33th-2024-12-31-02-25-utc.csv", 'r') as csv_file:
        csvReader = csv.DictReader(csv_file, delimiter = ',')   #using DictReader to clearly state what fieldname from the csv is being used
        next(csvReader) #skipping the header

        #Adding the name of movie titles into an array
        for row in csvReader:
            listOfMovies.append(row['Name'])

        #Printing from the array the name of a randomly selected movie.
        print(random.choice(listOfMovies))

if __name__ == "__main__":
    main()