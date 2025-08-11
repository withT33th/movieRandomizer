import csv
import random
import tkinter
import pickle
from tkinter.filedialog import askopenfilename

# defining a method to write the contents of a list into a pickle file
def save_to_pickle(list):
    with open('list.pkl', 'wb') as file:
        pickle.dump(list, file)

def load_pickle():
    with open('list.pkl', 'rb') as file:
        l = pickle.load(file)
    return l

#defining a method to generate a list of movie titles from a csv file and saving it to a pickle file
def generate_list(watchlist_file):
    gen_list = []
    with open(watchlist_file, 'r') as csv_file:
        csvReader = csv.DictReader(csv_file, delimiter = ',')   #using DictReader to clearly state what fieldname from the csv is being used
        next(csvReader) #skipping the header

        #Adding the name of movie titles into an list
        for row in csvReader:
            gen_list.append(row['Name'])

    save_to_pickle(gen_list)

    return gen_list

# returns a random element from the movielist
def get_random_movie(movielist):
    return random.choice(movielist)


# Adding a 'main' method
def main():

    # Asking the user if they would like to upload a new csv file or use an existing one
    choice = input('Would you like to upload a new file (1) or use an existing one (2)?: ')
    if(choice == '1'): 
        # Using the imported tkinter modules, we prompt the user to upload their movie watchlist from their file explorer
        watchlist_file = askopenfilename()
        watchlist = generate_list(watchlist_file)
        print(get_random_movie(watchlist))



if __name__ == "__main__":
    main()