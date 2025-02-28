import unittest
import string
from ShortPath import constants
from ShortPath import Graph
from ShortPath.data_generator import generate_vertices, generate_edges, get_graph


class TestGraphGenerator(unittest.TestCase):

    def test_generate_vertices(self):
        """Verify that the vertices are unique,
        have the correct length and are composed
        of the correct characters."""
        vertices = generate_vertices(10)
        self.assertEqual(len(vertices), 10)
        self.assertEqual(len(set(vertices)), 10)
        for vertex in vertices:
            self.assertTrue(
                all(char in string.ascii_uppercase + string.digits for char in vertex)
            )
            self.assertEqual(len(vertex), 8)

    def test_generate_edges(self):
        """Verify that the edges are unique, have the correct length"""
        vertices = generate_vertices(10)
        edges = generate_edges(vertices, 20)

        self.assertGreaterEqual(len(edges), 9)  # at least 9 edges
        self.assertLessEqual(len(edges), 15)

        graph_map = {v: set() for v in vertices}
        for v1, v2, weight in edges:
            self.assertIn(v1, vertices)
            self.assertIn(v2, vertices)
            self.assertTrue(1 <= weight <= 20)
            graph_map[v1].add(v2)
            graph_map[v2].add(v1)

        # Verify that the graph is connected with BFS
        visited = set()
        stack = [vertices[0]]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph_map[node] - visited)

        self.assertEqual(len(visited), len(vertices))

    def test_get_graph(self):
        """Verify that the graph is correctly generated"""
        graph = get_graph(constants.MAX_NUM_VERTEX)
        self.assertIsInstance(graph, Graph.Graph)
        self.assertEqual(len(graph.vertexes), constants.MAX_NUM_VERTEX)
        self.assertGreaterEqual(len(graph.relations), constants.MAX_NUM_VERTEX - 1)


if __name__ == "__main__":
    unittest.main()
