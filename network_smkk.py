#!/usr/bin/env python
"""
Network analysis script
Parameters:
    path: str <path-to-folder>
Usage:
    network_smkk.py --path <path-to-folder>
Example:
    $ python network_smkk.py --path data/labelled_data
"""

# to call path from command line
import os
from pathlib import Path
import argparse


# System tools
import os

# Data analysis
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm

# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# drawing
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)


def main():
    
    ### Initial stuff with pathes ###
    
    # Initialise ArgumentParser class
    ap = argparse.ArgumentParser()
    
    # CLI parameters
    ap.add_argument("-i", "--path", required=True, help="Path to data folder")
    ap.add_argument("-o", "--outfile", required=True, help="Output filename")
    
    # Parse arguments
    args = vars(ap.parse_args())

    # Output filename
    out_file_name = args["network"]
    
    # Create directory called "viz" for the visualisation, if it doesn't exist
    if not os.path.exists("viz"):
        os.mkdir("viz")
        
    # Output filepath
    out_image = os.path.join("viz", out_file_name, ".png")
     
    # Create directory called "output" for the csv, if it doesn't exist
    if not os.path.exists("output"):
        os.mkdir("output")
        
    # Output filepath
    out_file = os.path.join("output", out_file_name, ".csv")
    
    # Create column headers
    column_headers = "degree,betweenness,eigenvector_centrality"
    
    # Write column headers to file
    with open(out_file, "a", encoding="utf-8") as headers:
        # add newling after string
        headers.write(column_headers + "\n")
    
        
    # Create explicit filepath variable
    filepath = Path(args["path"])
    
    # get the file
    input_file = os.path.join(filepath, "fake_or_real_news.csv")

    # read 
    data = pd.read_csv(input_file)
    
    # make into dataframe
    real_df = data[data["label"]=="REAL"]["text"]


    ### Now for the network analysis ###
    
    # create empty list
    text_entities = []
    for text in tqdm(real_df):
        # create temporary list 
        tmp_entities = []
        # create doc object
        doc = nlp(text)
        # for every named entity
        for entity in doc.ents:
            # if that entity is a person
            if entity.label_ == "PERSON":
                # append to temp list
                tmp_entities.append(entity.text)
        # append temp list to main list
        text_entities.append(tmp_entities)

    # create empty list
    edgelist = []
    # iterate over every document
    for text in text_entities:
        # use itertools.combinations() to create edgelist
        edges = list(combinations(text, 2))
        # for each combination - i.e. each pair of 'nodes'
        for edge in edges:
            # append this to final edgelist
            edgelist.append(tuple(sorted(edge)))

    # create empty list
    counted_edges = []
    for key, value in Counter(edgelist).items():
        source = key[0]
        target = key[1]
        weight = value
        counted_edges.append((source, target, weight))


    edges_df = pd.DataFrame(counted_edges, columns=["nodeA", "nodeB", "weight"])
    filtered = edges_df[edges_df["weight"]>500]
    G=nx.from_pandas_edgelist(filtered, 'nodeA', 'nodeB', ["weight"])


    # Plot it
    pos = nx.nx_agraph.graphviz_layout(G, prog="neato")
    # draw 
    nx.draw(G, pos, with_labels = True, node_size = 20, font_size = 10)

    # save using matplotlib
    outpath_viz = os.path.join(outfile, 'network.png') 
    plt.savefig(outpath_viz, dpi = 300, bbox_inches = "tight")

    
    #### SOMETHING GOES WRONG HERE WITH THE "WEIGHT" AND i CAN'T FIGURE OUT WHAT
    # make dataframe
    ev = nx.eigenvector_centrality(G)
    bc = nx.betweenness_centrality(G)
    pd.DataFrame(ev.items()).sort_values("weight", ascending=False)
    pd.DataFrame(bc.items()).sort_values("weight", ascending=False)
    
    # save the DataFrame panda as a csv file
    DataFrame.to_csv(out_file) 
    

# Define behaviour when called from command line
if __name__=="__main__":
    main()