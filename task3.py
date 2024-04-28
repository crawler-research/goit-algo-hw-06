def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            # Отримання ваги ребра
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


import networkx as nx
G = nx.Graph()
weighted_edges = [("A", "B", 1), ("B", "C", 2), ("C", "D", 3), ("D", "E", 4), ("A", "C", 6), ("B", "D", 7), ("B", "E", 8)]
G.add_weighted_edges_from(weighted_edges)


shortest_paths = {node: dijkstra(G, node) for node in G.nodes()}
for start_node, paths in shortest_paths.items():
    print(f"Від {start_node}:")
    for end_node, distance in paths.items():
        print(f"{end_node}: {distance}")


