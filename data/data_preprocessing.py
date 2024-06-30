import pandas as pd
import networkx as nx
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


stops_path = os.path.join(script_dir, '../toronto-gtfs/stops.txt')
routes_path = os.path.join(script_dir, '../toronto-gtfs/routes.txt')
trips_path = os.path.join(script_dir, '../toronto-gtfs/trips.txt')
stop_times_path = os.path.join(script_dir, '../toronto-gtfs/stop_times.txt')

# Load required GTFS data
stops = pd.read_csv(stops_path)
routes = pd.read_csv(routes_path)
trips = pd.read_csv(trips_path)
stop_times = pd.read_csv(stop_times_path)


# Filter only subway routes (route_type == 1)
subway_routes = routes[routes['route_type'] == 1]

# Extract only the relevant trips
subway_trips = trips[trips['route_id'].isin(subway_routes['route_id'])]

# Extract the relevant stop_times for subway trips
subway_stop_times = stop_times[stop_times['trip_id'].isin(subway_trips['trip_id'])]

# Extract the unique subway stations from the stop_times
unique_subway_stations = stops[stops['stop_id'].isin(subway_stop_times['stop_id'].unique())]

# Map route IDs to route colors
route_colors = subway_routes.set_index('route_id')['route_color'].to_dict()

subway_stations_info = []
for _, row in unique_subway_stations.iterrows():
    stop_id = row['stop_id']
    route_ids = subway_stop_times[subway_stop_times['stop_id'] == stop_id]['trip_id'].map(subway_trips.set_index('trip_id')['route_id']).unique()
    route_colors_list = [route_colors[route_id] for route_id in route_ids if route_id in route_colors]
    
    subway_stations_info.append({
        'stop_id': stop_id,
        'stop_name': row['stop_name'],
        'latitude': row['stop_lat'],
        'longitude': row['stop_lon'],
        'route_ids': ','.join(map(str, route_ids)),
        'route_colors': ','.join(route_colors_list)
    })

# Create a DataFrame from the subway stations information
subway_stations_df = pd.DataFrame(subway_stations_info)

# Save the DataFrame to a CSV file
output_csv_path = os.path.join(script_dir, '../data/toronto_subway_stations_info.csv')
subway_stations_df.to_csv(output_csv_path, index=False)
print(f"Data processing complete. CSV file saved to {output_csv_path}")