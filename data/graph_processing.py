import pandas as pd
import networkx as nx
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the CSV file
csv_path = os.path.join(script_dir, '../data/ttc_data.csv')

# Load the CSV data into a pandas DataFrame
stations_df = pd.read_csv(csv_path)

# Ensure route_ids are strings
stations_df['route_ids'] = stations_df['route_ids'].astype(str)

# Create a graph
G = nx.Graph()

# Add nodes with attributes
for index, row in stations_df.iterrows():
    G.add_node(row['stop_id'], 
               name=row['stop_name'], 
               latitude=row['latitude'], 
               longitude=row['longitude'],
               route_ids=row['route_ids'], 
               route_colors=row['route_colors'])

# Add edges based on sequential stops in the same route
for route_id in stations_df['route_ids'].str.split(',').explode().unique():
    route_stations = stations_df[stations_df['route_ids'].str.contains(route_id)]
    route_stations = route_stations.sort_values(by='stop_id')  # Ensure the order is correct
    previous_stop_id = None
    
    for stop_id in route_stations['stop_id']:
        if previous_stop_id is not None:
            G.add_edge(previous_stop_id, stop_id, route_id=route_id)
        previous_stop_id = stop_id

# Save the graph to a file
output_path = os.path.join(script_dir, '../data/ttc_graph.graphml')
nx.write_graphml(G, output_path)
print(f"Graph saved to {output_path}")
