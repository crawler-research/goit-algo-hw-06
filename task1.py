import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["A", "B", "C", "D", "E"])

G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "A"), ("A", "C"), ("B", "D"), ("B", "E")])

nx.draw(G, with_labels=True, node_size=1000, node_color='skyblue')

# Кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print("Вершини:", num_nodes)
print("Ребра:", num_edges)

# Ступінь кожної вершини
degree_dict = dict(G.degree())
for node, degree in degree_dict.items():
    print(f"Вершина {node} ступін: {degree}")



plt.show()
