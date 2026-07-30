
import networkx as nx

import matplotlib.pyplot as plt


G = nx.Graph()


edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('C', 'G'),
    ('E', 'H')
]


G.add_edges_from(edges)


visited = []


def dfs(node):
    
    if node not in visited:

    
        visited.append(node)

        
        for neighbour in sorted(G.neighbors(node)):
            dfs(neighbour)


dfs('A')


print("DFS Traversal:", visited)


pos = nx.spring_layout(G, seed=42)


node_colors = [
    'red' if node in visited else 'lightblue'
    for node in G.nodes()
]

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1000,
    node_color=node_colors,
    font_size=12
)

plt.title("Depth First Search (DFS)")

plt.show()