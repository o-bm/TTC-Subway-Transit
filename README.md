# TTC Subway Transit Visualization

This project demonstrates how to create and visualize a graph of the Toronto Transit Commission (TTC) subway stations using data from the GTFS feed.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Processing](#data-processing)
- [License](#license)

## Introduction
This project processes GTFS data to extract information about subway stations, constructs a graph representing the connections between these stations, and visualizes the graph. The inspiration for this project came from a trip to Moscow, where I was deeply impressed by the uniqueness of each subway station. With this project, I aim to create an interactive map that showcases interesting facts and details for each stop in Toronto's subway system. By visualizing the data in this way, users can explore the Toronto subway network and learn about the distinctive features of its stations.

## Data Processing
### Data Source
The GTFS data used in this project was obtained from TransitFeeds and dates back to October 2020. It is important to note that since then, TTC's line 3 has been permanently closed, which is reflected in the dataset.

### Data Preparation
Since the GTFS data includes various forms of transport such as streetcars and buses, it was necessary to filter out all non-subway data. Additionally, the dataset contained duplicate entries due to separate entries for northbound and southbound platforms. These duplicates were filtered to ensure that each station is represented only once.

### Graph Construction
Nodes: Each subway station is added as a node in the graph, with attributes such as name, latitude, longitude, route IDs, and route colors.
Edges: Connections between sequential stops on the same route are added as edges. The script ensures the stops are in the correct order by sorting them by stop ID.

### Visualization
The graph is visualized using GraphML and Matplotlib. Each node represents a subway station, and each edge represents a connection between sequential stations on the same route.


