**Assignment description:**

Creating reusable network analysis pipeline

This exercise is building directly on the work we did in class. I want you to take the code we developed together and in you groups and turn it into a reusable command-line tool. You can see the code from class here:
https://github.com/CDS-AU-DK/cds-language/blob/main/notebooks/session6.ipynb

This command-line tool will take a given dataset and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents, like we did in class.

Your script should be able to be run from the command line

It should take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"

For any given weighted edgelist given as an input, your script should be used to create a network visualization, which will be saved in a folder called viz.

It should also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It should save this as a CSV in a folder called output.

**General instructions**

For this assignment, you should upload a standalone .py script which can be executed from the command line

Save your script as network.py

You must include a requirements.txt file and a bash script to set up a virtual environment for the project. You can use those on worker02 as a template

You can either upload the scripts here or push to GitHub and include a link - or both!

Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line.
