import numpy as np
from collections import Counter 
import os
from pathlib import Path
import pandas as pd
import numpy as np
import re # regex
import string # regex



### I DIDN'T HAVE TIME TO MAKE A REQUIREMENTS TXT
### I USED THE TEXTS FROM THE CENLAB FOLDER (EXCLUDED THE "1887_she.txt")



# define main function
def main():
    
    # prepare regex tokenizer for splitting strings
    def tokenize(input_string):

        # split on any non-alphanumeric character
        tokenizer = re.compile(r"\W+")

        # tokenize
        token_list = tokenizer.split(input_string)

        # return the token list
        return token_list


    # prepare panda to write logs
    columns = ['collocate', 'raw_frequency', 'MI']
    index = np.arange(0)
    DATA = pd.DataFrame(columns=columns, index = index)


    # define keyword
    keyword = "gender"

    # set data path
    data_path = os.path.join("..", "data", "cenlab", "texts")

    # prepare empty corpus list
    corpus = []



    # make for loop that reads the texts
    for filename in Path(data_path).glob("*.txt"):
        with open(filename, "r", encoding="utf-8") as file:

            loaded_text = file.read() # load texts
            corpus.append(loaded_text)

    # flatten the corpus so we get one list instead of a list of lists
    flattened_corpus = [val for sublist in corpus for val in sublist]



    # prepare kwic function - I put the default window size to 5 (words)
    def kwic(text, keyword, window_size=5):  

        #prepare empty concordance_lines_kwic list to be filled with concordance lines for each text
        concordance_lines_kwic = []

        # tokenize the text
        text_tokens = re.compile(r"\W+").split(text)

        # do this (why???)
        N = 0
        N += len(text_tokens)

        # Return index for each element text_tokens if the element in text_tokens is equal to keyword
        indices = [index for index, match in enumerate(text_tokens) if match == keyword]

        # For each keyword in the text, create the object concordance_line which has keyword and the words just before and after (keyword +- window_size)
        for index in indices:

            # the concordance line starts from the token that is 5 tokens before the keyword (or at index 0 if the keyword is less than 5 words from the beginning of the text) and ends at the word that is 5 words after the keyword
            concordance_line = text_tokens[max(0,index - window_size):index+window_size+1]

            # append the concordance_line to the concordance_lines_kwic list 
            concordance_lines_kwic.append(concordance_line)

            #print(concordance_line)

        # return the tokenized list of concordance lines
        return concordance_lines_kwic


    # prepare empty concordance_lines list
    concordance_lines = []


    # get concordance lines using the kwic function for each text in the corpus and append to the empty concordance_lines list
    for text in corpus:

        # set text and keyword
        concordances_text = kwic(text=text, keyword=keyword) 

        # append concordances_text list to the concordance_lines list
        concordance_lines.append(concordances_text) 
    #print(concordance_lines)


    # flatten the output of the kwic function (concordance_lines) so we get one list instead of a list of lists 
    # we have to do it two times because it's actually a list of lists of lists
    flattened_concordance_lines_1 = [val for sublist in concordance_lines for val in sublist]
    flattened_concordance_lines_2 = [val for sublist in flattened_concordance_lines_1 for val in sublist]
    #print(flattened_concordance_lines_2)


    # get a numpy array of all the unique collocates
    collocates = np.unique(flattened_concordance_lines_2) # this is a numpy.ndarray

    # sort the collocates alphabetically (not necessary but nice)
    collocates = sort(collocates)

    #print(collocates)
    #print(type(collocates))



    # now tokenize the corpus: 
    tokenized_corpus = []
    for text in corpus:
        tokenized_text = tokenize(text) # tokenize the corpus (i.e. split it into seperat words and exclude punctuation)
        tokenized_corpus.append(tokenized_text)

    # flatten the tokenized corpus:
    flattened_tokenized_corpus = [val for sublist in tokenized_corpus for val in sublist]


    #### Now the math begins ####

    # set u to 0 to begin with
    u = 0

    # count the number of time the keyword appears in each text of the corpus and add this number to u
    for i in range(len(flattened_tokenized_corpus)):
        u_i = flattened_tokenized_corpus[i].count(keyword) #count the number of times the keyword appear in the corpus.
        u = u + u_i

    #print(u)
    #print(f"the keyword {keyword} appears {u} times in the corpus (u)")


    # for loop that goes through the collocates in the collocates list and finds the MI 
    for i in range(len(collocates)):
        v = flattened_tokenized_corpus.count(collocates[i]) # the number of times the collocate appears in the corpus
        #print(f"the collocate {collocates[i]} appears {v} times in the corpus (v)")

        O11 = flattened_concordance_lines_2.count(collocates[i]) # the number of times the collocate appears in the concordance lines
        #print(f"the collocate {collocates[i]} appears {O11} time(s) in the concordance lines (O11)")

        O12 = u - O11 # the number of times target word (u) appears alongside any other collocate (i.e. not-v) within the chosen window size
        #print(f"O12: {O12}")

        O21 = v - O11 # the number of times collocate (v) appears without target (u) across the whole text/corpus
        #print(f"O21: {O21}")

        R1 = O11 + O12 # the number of times target word (u) appears with any collocate within a chosen window size
        #print(f"R1: {R1}")

        C1 = O11 + O21 # the number of times the collocate appears across the whole text/corpus
        #print(f"C1: {C1}")

        N = len(flattened_tokenized_corpus) # length of corpus
        #print(f"N: {N}")

        E11 = (R1*C1/N) # expected
        #print(f"E11: {E11}")

        MI = np.log(O11/E11) # return MI
        #print(f"MI of collocate {collocates[i]}: {MI}")

        # add output to pandas
        DATA = DATA.append({
        'collocate': collocates[i],
        'raw_frequency': O11,
        'MI': MI
        }, ignore_index=True)

    print(DATA)

    # output filename
    out_file_name = "collocations_outfile"

    # create directory called "out", if it doesn't exist (for me, this directory is put inside the "notebooks" folder)
    if not os.path.exists("out"):
        os.mkdir("out")

    # output filepath
    outfile = os.path.join("out", out_file_name)

    # save the DATA panda as a csv file
    DATA.to_csv(outfile) 


# Define behaviour when called from command line
if __name__=="__main__":
    main()