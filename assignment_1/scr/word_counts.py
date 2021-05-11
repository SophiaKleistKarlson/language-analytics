# import libraries
import os
from pathlib import Path
import pandas as pd
import numpy as np
import re


def main():
    # set data path
    data_path = os.path.join("..", "data", "100_english_novels", "corpus")

    # prepare list to be filled with word counts
    word_count_list = []

    # prepare panda to write logs
    columns = ['filename', 'total_words', 'unique_words']
    index = np.arange(0)
    DATA = pd.DataFrame(columns=columns, index = index)


    # make for loop that reads the 100 texts
    for filename in Path(data_path).glob("*.txt"):
        with open(filename, "r", encoding="utf-8") as file:

            loaded_text = file.read() # load texts
            split_text = loaded_text.split() # for each text, split it into seperat words
            word_count = len(split_text) # then counts the number of words

            # Filenames
            _, text_name = os.path.split(filename) # use a dummy variable to isolate the text name (and leave out the path)        
            #text_name = re.split('\.', text_name)[0] # if I wanted to leave out the ".txt", I could do this

            # Unique words - first, define an empty list to be filled with unique words
            unique_words = []

            # nested for loop that iterates over the words in the split_text list
            for word in split_text:
                if word not in unique_words: # if word is not already in the unique_words list
                    unique_words.append(word) # then append the word to the list

            unique_words_count = len(unique_words) # count the number of unique words

            # write output to pandas
            DATA = DATA.append({
                'filename': text_name,
                'total_words': word_count,
                'unique_words': unique_words_count
            }, ignore_index=True)


    # print the word count list
    print(DATA)

    # make outpath to show where to save the data and what to call the csv (I manually made a folder in the data folder called "homework_output")
    outpath = os.path.join("..", "data", "homework_output", "word_counts.csv")

    # save the DATA panda as a csv file
    DATA.to_csv(outpath)   
 

# Define behaviour when called from command line
if __name__=="__main__": 
    main()
