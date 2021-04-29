# Self-guided assignment: Development of polarity score of the word "gay" in headlines from ABC News from 2003-2021.

In this self-guided assignment, I have made a script that runs through the abcnews headlines, selects all headlines that contains the keyword "gay", finds the polarity scores for these headlines and produces two plots, one that shows the 7 days mean average polarity, and one that shows this for each month.

My hypothesis was that the keyword "gay" has gained a more positive sentiment score over time (from 2003 where the first news headlines are from), but that the election of president Trump in 2016 might cause this gain to slow down, or even the polarity score to drop. As seen in the plots ("polarity_plot.png"), this seems to be a general trend, even though there are many ups and downs throughout the last 17 years.

To run the script, simply paste the bash script ("create_keyword_sentiment_venv.sh") - this will both create the virtual environment and run the script.
