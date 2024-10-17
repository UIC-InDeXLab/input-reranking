import sys
sys.path.insert(1, "..")

from utils import llm_api
from utils import prompt

import numpy as np


class Edge:
    def __init__(self, source, target, weight) -> None:
        self.source = source
        self.target = target
        self.weight = weight
    
    def __str__(self) -> str:
        return f"({self.source}, {self.target}, {self.weight})"
    
    def __repr__(self) -> str:
        return self.__str__()

class Node:
    def __init__(self, id, payload) -> None:
        self.id = id
        self.payload = payload # Y_i or B_j

    def __str__(self) -> str:
        return f"({self.id}, {self.payload})"
    
    def __repr__(self) -> str:
        return self.__str__()

class BGraph:
    def __init__(self, n1, n2, m) -> None:
        self.edges = []
        self.nodes = []
        self.n1 = n1
        self.n2 = n2
        self.U = []
        self.V = []
        self.m = m
        self.adj_mat = np.array([[0 for _ in range(n1 + n2)] for _ in range(n1 + n2)])
        self.node_map = {}

    def add_edge(self, edge):
        if edge.target not in self.nodes:
            self.nodes.append(edge.target)
            self.V.append(edge.target)
            self.add_node(edge.target)
        if edge.source not in self.nodes:
            self.nodes.append(edge.source)
            self.U.append(edge.source)
            self.add_node(edge.source)
        self.edges.append(edge)
        self.adj_mat[edge.source.id][edge.target.id] = edge.weight
        self.adj_mat[edge.target.id][edge.source.id] = edge.weight

    def add_node(self, node):
        self.node_map[node.id] = node

def create_bi_graph(k, m, query, prompt, ask_score):
    print(f"[BI_GRAPH] For query: {query}")
    # k: Number of shuffles
    # m: Number of elements in each batch of prompt
    # Source: Elements
    # Target: Evaluations

    id = 0

    g = BGraph(n1=len(prompt), n2=k * len(prompt) // m, m=len(prompt) * k)

    element_nodes = {}

    for ele in prompt:
        element_nodes[ele] = Node(id=id, payload=0)
        id += 1

    for i in range(k):
        print(f"[BI_GRAPH] {i + 1} / {k} shuffles")
        arr = prompt.copy()
        np.random.shuffle(arr)
        # batches = prompt.reshape(arr, m)
        batches = arr.reshape(len(prompt) // m, m)
        for o, batch in enumerate(batches):
            print(f"[BI_GRAPH] {o + 1} / {len(arr) // m} batches")
            while True:
                try:
                    counter = 0
                    evaluation = ask_score(batch, query) # P_j's
                    while len(evaluation) != len(batch):
                        counter += 1
                        print("[BI_GRAPH] Error output, retrying...")
                        if counter >= 20:
                            print("[BI_GRAPH] ERROR Returning zero")
                            evaluation = [0 for _ in range(len(batch))]
                        else:
                            evaluation = ask_score(batch, query)
                    break
                except Exception as e:
                    print("[BI_GRAPH] Error output: ", e)
            target = Node(id=id, payload=1) # Bias is initialized with 1
            id += 1

            for j, element in enumerate(batch):
                w = evaluation[j]
                t = element
                edge = Edge(element_nodes[t], target, w)
                g.add_edge(edge)
    
    return g, element_nodes

def learn_bi_graph(g, k, m, iters=1000):
    # U <--> V
    b_j_values = []
    y_i_values = []

    for i in range(iters):
        # Y_i
        for source in g.U:
            targets_all = g.adj_mat[source.id, :]
            targets = np.where(targets_all != 0)[0]
            y_i = 0
            for target in targets:
                y_i += targets_all[target] / g.node_map[target].payload
            source.payload = y_i / k
        # B_j
        for source in g.V:
            targets_all = g.adj_mat[:, source.id]
            targets = np.where(targets_all != 0)[0]
            b_j = 0
            for target in targets:
                b_j += targets_all[target] / g.node_map[target].payload
            source.payload = b_j / m

        # Report
        avg_bj = sum([s.payload for s in g.V]) / len(g.V)
        b_j_values.append(avg_bj)
        # print("Avg Bj: ", avg_bj)
        avg_yi = sum([s.payload for s in g.U]) / len(g.U)
        y_i_values.append(avg_yi)
        # print("Avg Yi: ", avg_yi)

    return b_j_values, y_i_values