import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E"])
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("A", "C"), ("B", "D"), ("B", "E")])

all_dfs = []
all_bfs = []

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                all_dfs.append(path + [next_vertex])
            else:
                stack.append((next_vertex, path + [next_vertex]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                all_bfs.append(path + [next_vertex])
            else:
                queue.append((next_vertex, path + [next_vertex]))

# Пошук шляхів за допомогою DFS та BFS
start_node = "A"
end_node = "D"
dfs_paths(G, start_node, end_node)
bfs_paths(G, start_node, end_node)

print("Шляхи між А і D, знайдені за допомогою BFS:", all_bfs)
print("Шляхи між А і D, знайдені за допомогою DFS:", all_dfs)
