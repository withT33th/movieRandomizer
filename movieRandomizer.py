import csv
import random
import tkinter
import pickle
from tkinter.filedialog import askopenfilename

#defining a method to generate a list of movie titles from a csv file
def generate_list(watchlist):
    listOfMovies = []
    with open(watchlist, 'r') as csv_file:
        csvReader = csv.DictReader(csv_file, delimiter = ',')   #using DictReader to clearly state what fieldname from the csv is being used
        next(csvReader) #skipping the header

        #Adding the name of movie titles into an array
        for row in csvReader:
            listOfMovies.append(row['Name'])

        #Printing from the array the name of a randomly selected movie.
        print(random.choice(listOfMovies))
        return listOfMovies


# Adding a 'main' method
def main():
    # Using the imported tkinter modules, we prompt the user to upload their movie watchlist from their file explorer
    watchlist_file = askopenfilename()
    watchlist = generate_list(watchlist_file)


if __name__ == "__main__":
    main()