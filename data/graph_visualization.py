import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import re

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the GraphML file
graphml_path = os.path.join(script_dir, '../data/transit_graph2.graphml')

# Load the graph from the GraphML file
G = nx.read_graphml(graphml_path)

# Clean the stop name to ensure it only contains the station name
def clean_stop_name(name):
    return re.sub(r'\s*STATION.*$', '', name).strip()

# Update node labels to show cleaned stop names
for node, data in G.nodes(data=True):
    data['name'] = clean_stop_name(data['name'])

# Get positions for each node based on latitude and longitude
pos = {node: (float(data['longitude']), float(data['latitude'])) for node, data in G.nodes(data=True)}

# Draw the graph with labels showing the cleaned stop names
plt.figure(figsize=(20, 12))
nx.draw(G, pos, labels=nx.get_node_attributes(G, 'name'), node_size=50, font_size=8)
plt.title("Toronto Subway Stations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
