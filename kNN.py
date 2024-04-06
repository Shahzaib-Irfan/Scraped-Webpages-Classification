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