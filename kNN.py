from itertools import combinations
from collections import Counter
import networkx as nx
from preprocessing import document_graphs, create_graph
import pandas as pd

def compute_mcs(G1, G2):
    edges1 = set(G1.edges())
    edges2 = set(G2.edges())
    
    common_edges = edges1.intersection(edges2)
    
    mcs_graph = nx.Graph(list(common_edges))
    
    return mcs_graph

def compute_distance(G1, G2):
    mcs_graph = compute_mcs(G1, G2)
    return -len(mcs_graph.edges()) 

def knn_classify(test_graph, k):
    distances = []
    
    for train_id, train_graph in document_graphs.items():
        distance = compute_distance(test_graph, train_graph)
        distances.append((train_id, distance))
    
    distances.sort(key=lambda x: x[1])
    
    neighbors = distances[:k]
    
    neighbor_categories = [data.loc[i, 'Type'] for i, _ in neighbors]
    
    majority_class = Counter(neighbor_categories).most_common(1)[0][0]
    
    return majority_class

data = pd.read_csv('Webpages.csv')
#data = pd.concat([data.iloc[12: 15], data.iloc[27:30], data.iloc[42: 44]])
test_documents = [create_graph(str(data.iloc[12]['Content'])), create_graph(str(data.iloc[13]['Content'])), create_graph(str(data.iloc[14]['Content'])), create_graph(str(data.iloc[27]['Content'])), create_graph(str(data.iloc[28]['Content'])), create_graph(str(data.iloc[29]['Content'])), create_graph(str(data.iloc[42]['Content'])), create_graph(str(data.iloc[43]['Content'])), create_graph(str(data.iloc[44]['Content']))]

predicted_labels = []
for test_graph in test_documents:
    predicted_category = knn_classify(test_graph, k=3) # k = 3, because of three categories (Sports & Health, Sports and Food)
    predicted_labels.append(predicted_category)
    #print("Predicted category:", predicted_category)