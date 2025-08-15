import sys
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
        li = pickle.load(file)
    return li

# method to generate a list from the csv provided and save it using pickle
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
    # Initializing root window
    root = tkinter.Tk()
    root.withdraw()

    # While-loop to ensure user input is a valid option
    y = False
    while (y == False):
        # Asking the user if they would like to upload a new csv file or use an existing one
        choice = input('\nWould you like to upload a new file (1) or use an existing one (2)?: ')

        # Try/except block to evaluate if a user has input a valid choice
        try:
            choice = float(choice)
            if (choice == 1 or choice == 2):
                y = True
            else:
                print("\nPlease enter a valid number.")
        except:
            print("\nPlease enter a valid number.")

    x = False
    while(x == False):
        if(choice == 1):
            # Using the imported tkinter modules, we prompt the user to upload their movie watchlist from their file explorer
            root.attributes('-topmost', True)
            watchlist_file = askopenfilename(filetypes = (("CSV Files", "*.csv"),))
            root.attributes('-topmost', False)

            # Try/except block for if a user exits the dialog box and does not choose a file
            try:
                watchlist = generate_list(watchlist_file)
                print(get_random_movie(watchlist))
                x = True
            except:
                sys.exit('No file chosen. Goodbye!\n')

        elif(choice == 2):
            try:
                # in this choice, we load the existing saved data instead of opening the file explorer
                watchlist = load_pickle()
                print(get_random_movie(watchlist))
                x = True
            except:
                print("\nNo file available.")
                print("Generating new watchlist...\n")
                choice = 1

if __name__ == "__main__":
    main()