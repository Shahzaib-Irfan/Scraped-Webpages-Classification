from itertools import combinations
from collections import Counter
import networkx as nx

# Function to compute the maximal common subgraph (MCS) between two graphs
def compute_mcs(G1, G2):
    # Convert graphs to edge sets
    edges1 = set(G1.edges())
    edges2 = set(G2.edges())
    
    # Compute the intersection of edges
    common_edges = edges1.intersection(edges2)
    
    # Create a new graph with common edges
    mcs_graph = nx.Graph(list(common_edges))
    
    return mcs_graph

def compute_distance(G1, G2):
    mcs_graph = compute_mcs(G1, G2)
    return -len(mcs_graph.edges()) 

def knn_classify(test_graph, k):
    distances = []
    
    # Compute distance between test_graph and each training graph
    for train_id, train_graph in document_graphs.items():
        distance = compute_distance(test_graph, train_graph)
        distances.append((train_id, distance))
    
    # Sort distances in ascending order
    distances.sort(key=lambda x: x[1])
    
    # Get the k-nearest neighbors
    neighbors = distances[:k]
    
    # Get categories of the neighbors
    neighbor_categories = [data.loc[i, 'Type'] for i, _ in neighbors]
    
    # Find the majority class
    majority_class = Counter(neighbor_categories).most_common(1)[0][0]
    
    return majority_class