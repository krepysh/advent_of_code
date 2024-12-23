from collections import defaultdict

edges = [line.split('-') for line in open(0).read().splitlines()]

graph = defaultdict(set)

for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

triplets = []
for a, b in edges:
    intersection = set(graph[a]) & set(graph[b])
    if intersection:
        for edge in intersection:
            if edge[0] == "t":
                triplets.append(tuple(sorted((a, b, edge))))
triplets.sort()


# print(len(set(triplets)))


def bron_kerbosch(graph, current_clique, potential_nodes, excluded_nodes, cliques):
    if not potential_nodes and not excluded_nodes:
        cliques.append(current_clique)
    for node in list(potential_nodes):
        bron_kerbosch(
            graph,
            current_clique | {node},
            potential_nodes & graph[node],
            excluded_nodes & graph[node],
            cliques
        )
        potential_nodes.remove(node)
        excluded_nodes.add(node)


cliques = []
bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
party = max(cliques, key=len)
party = list(party)
party.sort()
print(",".join(party))
