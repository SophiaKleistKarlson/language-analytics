#### __import packages__ ####

import os 
import pandas as pd
import spacy
import matplotlib.pyplot as plt 
from spacytextblob.spacytextblob import SpacyTextBlob 


#### __unzip the zipfile with the archive__ ####

# define path to the zip file
zip_path = os.path.join("..", "data") 

# set working directory to the zip path
os.chdir(zip_path)
print(zip_path)

# unzip the zipfile into the working directory (data folder)
!unzip 'archive.zip'


#### __initialize spaCy__ ####

# we use the English model
nlp = spacy.load("en_core_web_sm")

# define path to csv
path_to_csv = os.path.join("..", "data", "abcnews-date-text.csv")

# read the csv
abc_news = pd.read_csv(path_to_csv)

# define the spacy object
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)



#### __define functions__ ####

# date function
def date_change(df):
    all_dates=[]

    # for loop that takes every row in our dataframe and changes "publish_date" to the format yyyy-mm-dd
    for index, row in df.iterrows():
        date = str(row['publish_date'])
        time_df = pd.DataFrame({'year': [int(date[0:4])],
                       'month': [int(date[4:6])],
                       'day': [int(date[6:8])]})
        time_df = pd.to_datetime(time_df)
        
        # append the new dates dataframe to the list containing all_dates
        all_dates.append(time_df[0]) # this appends the 0 element

    df["publish_date"]= all_dates # append them to the dataframe
    return df


# polarity function
def polarity(df):
    polarity_scores = []

    for doc in nlp.pipe(df["headline_text"]):
        polarity_scores.append(doc._.sentiment.polarity)

    return polarity_scores


# plot function
def plot_polarity(df, roll_val1 = 7, roll_val2 = 30, save = False):
    fig = plt.figure(figsize = (10.0, 3.0))

    axes_1 = fig.add_subplot(1,2,1) # 1 row , 3 columns, 1st column position
    axes_2 = fig.add_subplot(1,2,2) # 1 row , 3 columns, 2nd column position

    axes_1.set_ylabel(f"Polarity (rolling mean of {roll_val1} days)")
    smoothed_sent_week = df.groupby("publish_date").mean("polarity").rolling(roll_val1).mean()
    axes_1.plot(smoothed_sent_week) # plot the mean_val on the axes_1 on the canvas from above
    axes_1.legend("Week average", loc="upper left")
    
    axes_2.set_ylabel(f"Polarity average (rolling mean of {roll_val2} days)")
    smoothed_sent_month = df.groupby("publish_date").mean("polarity").rolling(roll_val2).mean()
    axes_2.plot(smoothed_sent_month) # plot the mean_val on the axes_1 on the canvas from above
    axes_2.legend("Month average", loc="upper left")

    fig.tight_layout()
    
    # save and show figure
    if save == True:
        plt.savefig("polarity_plot.png")
    plt.show()
    
    
    
#### __now I define the main() function__ ####

def main():
    # choose a sample of 10000 rows
    sample = abc_news[1:10000]
    sample = date_change(sample)
    polarity_scores = polarity(sample)
    sample["polarity"] = polarity_scores
    plot_polarity(sample, save = True)


# define behaviour when main() is called from command line
if __name__=="__main__":
    main()
