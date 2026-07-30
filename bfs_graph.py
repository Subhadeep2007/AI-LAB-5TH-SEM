# Import the NetworkX library for creating and manipulating graphs
import networkx as nx

# Import Matplotlib for graph visualization
import matplotlib.pyplot as plt

# Import deque (Queue) for BFS traversal
from collections import deque

# Create an empty graph
G = nx.Graph()

# Define the edges of the graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('C', 'G'),
    ('E', 'H')
]

# Add all edges to the graph
G.add_edges_from(edges)

# Select the starting node
start = 'A'

# Create an empty list to store visited nodes
visited = []

# Create a queue and insert the starting node
queue = deque([start])

# Repeat until the queue becomes empty
while queue:

    # Remove the first node from the queue (FIFO)
    node = queue.popleft()

    # Check whether the node has already been visited
    if node not in visited:

        # Mark the node as visited
        visited.append(node)

        # Add all unvisited neighboring nodes to the queue
        queue.extend(
            sorted(set(G.neighbors(node)) - set(visited))
        )

# Display the BFS traversal order
print("BFS Traversal:", visited)

# Calculate positions of nodes for graph drawing
pos = nx.spring_layout(G, seed=42)

# Color visited nodes red and others light blue
node_colors = [
    'red' if node in visited else 'lightblue'
    for node in G.nodes()
]

# Draw the graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1000,
    node_color=node_colors,
    font_size=12
)

# Display the graph title
plt.title("Breadth First Search")

# Show the graph window
plt.show()