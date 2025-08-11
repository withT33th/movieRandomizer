import csv
import random
import tkinter
import pickle
from tkinter.filedialog import askopenfilename

#defining a method to generate a list of movie titles from a csv file
def generate_list(watchlist_file):
    listOfMovies = []
    with open(watchlist_file, 'r') as csv_file:
        csvReader = csv.DictReader(csv_file, delimiter = ',')   #using DictReader to clearly state what fieldname from the csv is being used
        next(csvReader) #skipping the header

        #Adding the name of movie titles into an array
        for row in csvReader:
            listOfMovies.append(row['Name'])

        return listOfMovies

# returns a random element from the movielist
def get_random_movie(movielist):
    return random.choice(movielist)


# Adding a 'main' method
def main():
    # Using the imported tkinter modules, we prompt the user to upload their movie watchlist from their file explorer
    watchlist_file = askopenfilename()
    watchlist = generate_list(watchlist_file)
    print(get_random_movie(watchlist))


if __name__ == "__main__":
    main()