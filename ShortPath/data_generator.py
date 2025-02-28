import random
import string

from ShortPath import constants
from ShortPath import Graph


def generate_vertices(size=constants.MAX_NUM_VERTEX):
    return [''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for _ in range(size)]

def generate_edges(vertices, limit=constants.MAX_WEIGHT):
    edges = set()

    # Make sure that the graph is convexed with a initial minimum generator tree
    connected = set([vertices[0]])
    unconnected = set(vertices[1:])

    while unconnected:
        v1 = random.choice(list(connected))
        v2 = random.choice(list(unconnected))
        weight = random.randint(1, limit)
        edges.add((v1, v2, weight))
        connected.add(v2)
        unconnected.remove(v2)

    # Add more edges to complete the graph
    while len(edges) < len(vertices) + len(vertices)*0.2:
        v1, v2 = random.sample(vertices, 2)
        weight = random.randint(1, limit)
        if (v1, v2, weight) not in edges and (v2, v1, weight) not in edges:
            edges.add((v1, v2, weight))

    return list(edges)


def get_graph(size):
    vertices = generate_vertices(size)
    edges = generate_edges(vertices)
    return Graph.Graph(vertices, edges, directed=True)




