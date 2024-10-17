import igraph as ig


def get_degree(edge_list, vertex):
    return len([e for e in edge_list if vertex in e])

def shiftLbyn(arr, n=0):
    return arr[n::] + arr[:n:]

def shiftRbyn(arr, n=0):
    return arr[n:len(arr):] + arr[0:n:]

def generate_graph(node_size, edge_size):
    g = ig.Graph.Erdos_Renyi(n=node_size, m=edge_size)
    edges = []
    for e in g.es():
        edges.append((e.source, e.target))
    return edges

def rank_utility(edges, vertex):
    rel = [1 if vertex in edge else 0 for edge in edges]
    utility = [rel[i] * (1 / (i + 1)) for i in range(len(rel))]
    return sum(utility)

def get_list_of_edges(g):
    edges = []
    for e in g.es():
        edges.append((e.source, e.target))

    edges = sorted(edges, key=lambda x: x[0])
    return edges