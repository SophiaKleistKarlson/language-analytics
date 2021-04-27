{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                        filename total_words unique_words\n",
      "0      Cbronte_Villette_1853.txt      196557        29084\n",
      "1        Forster_Angels_1905.txt       50477         9464\n",
      "2      Woolf_Lighthouse_1927.txt       70185        11157\n",
      "3     Meredith_Richmond_1871.txt      214985        28892\n",
      "4    Stevenson_Treasure_1883.txt       68448        10831\n",
      "..                           ...         ...          ...\n",
      "95  Chesterton_Thursday_1908.txt       58299        10385\n",
      "96         Burnett_Lord_1886.txt       58698         8131\n",
      "97      Braddon_Phantom_1883.txt      180676        22474\n",
      "98         Gaskell_Ruth_1855.txt      161797        18148\n",
      "99     Kipling_Captains_1896.txt       53467        11709\n",
      "\n",
      "[100 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "# import libraries\n",
    "import os\n",
    "from pathlib import Path\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re\n",
    "\n",
    "\n",
    "# set data path\n",
    "data_path = os.path.join(\"..\", \"data\", \"100_english_novels\", \"corpus\")\n",
    "\n",
    "# prepare list to be filled with word counts\n",
    "word_count_list = []\n",
    "\n",
    "# prepare panda to write logs\n",
    "columns = ['filename', 'total_words', 'unique_words']\n",
    "index = np.arange(0)\n",
    "DATA = pd.DataFrame(columns=columns, index = index)\n",
    "\n",
    "        \n",
    "# make for loop that reads the 100 texts\n",
    "for filename in Path(data_path).glob(\"*.txt\"):\n",
    "    with open(filename, \"r\", encoding=\"utf-8\") as file:\n",
    "        \n",
    "        loaded_text = file.read() # load texts\n",
    "        split_text = loaded_text.split() # for each text, split it into seperat words\n",
    "        word_count = len(split_text) # then counts the number of words\n",
    "        \n",
    "        # Filenames\n",
    "        _, text_name = os.path.split(filename) # use a dummy variable to isolate the text name (and leave out the path)        \n",
    "        #text_name = re.split('\\.', text_name)[0] # if I wanted to leave out the \".txt\", I could do this\n",
    "        \n",
    "        # Unique words - first, define an empty list to be filled with unique words\n",
    "        unique_words = []\n",
    "        \n",
    "        # nested for loop that iterates over the words in the split_text list\n",
    "        for word in split_text:\n",
    "            if word not in unique_words: # if word is not already in the unique_words list\n",
    "                unique_words.append(word) # then append the word to the list\n",
    "        \n",
    "        unique_words_count = len(unique_words) # count the number of unique words\n",
    "        \n",
    "        # write output to pandas\n",
    "        DATA = DATA.append({\n",
    "            'filename': text_name,\n",
    "            'total_words': word_count,\n",
    "            'unique_words': unique_words_count\n",
    "        }, ignore_index=True)\n",
    "\n",
    "\n",
    "# print the word count list\n",
    "print(DATA)\n",
    "\n",
    "# make outpath to show where to save the data and what to call the csv (I manually made a folder in the data folder called \"homework_output\")\n",
    "outpath = os.path.join(\"..\", \"data\", \"homework_output\", \"word_counts.csv\")\n",
    "\n",
    "# save the DATA panda as a csv file\n",
    "DATA.to_csv(outpath)   \n",
    "   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "lang101",
   "language": "python",
   "name": "lang101"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
