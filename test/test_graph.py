import unittest
from ShortPath import Graph


class TestGraphAlgorithms(unittest.TestCase):
    def setUp(self):
        self.vertices = ["A", "B", "C", "D"]
        self.edges = [
            ("A", "B", 1),
            ("A", "C", 4),
            ("B", "C", 2),
            ("B", "D", 5),
            ("C", "D", 1),
        ]
        self.graph = Graph.Graph(self.vertices, self.edges, directed=True)

        self.vertices1 = ["A", "B", "C", "D"]
        self.edges1 = []
        self.graph1 = Graph.Graph(self.vertices1, self.edges1, directed=True)

        self.vertices2 = []
        self.edges2 = []
        self.graph2 = Graph.Graph(self.vertices2, self.edges2, directed=True)

    def test_dijkstra(self):
        result = self.graph.dijkstra("A")
        expected_distances = {"A": 0, "B": 1, "C": 3, "D": 4}
        for v in expected_distances:
            self.assertEqual(result[v]["distance"], expected_distances[v])

    def test_dijkstra1(self):
        result = self.graph1.dijkstra("A")
        expected_distances = {
            "A": 0,
            "B": float("inf"),
            "C": float("inf"),
            "D": float("inf"),
        }
        for v in expected_distances:
            self.assertEqual(result[v]["distance"], expected_distances[v])

    def test_dijkstra2(self):
        with self.assertRaises(ValueError):
            self.graph2.dijkstra("A")

    def test_floyd_warshall(self):
        result = self.graph.floyd_warshall()
        expected_distances = {
            "A": {"A": 0, "B": 1, "C": 3, "D": 4},
            "B": {"A": float("inf"), "B": 0, "C": 2, "D": 3},
            "C": {"A": float("inf"), "B": float("inf"), "C": 0, "D": 1},
            "D": {"A": float("inf"), "B": float("inf"), "C": float("inf"), "D": 0},
        }
        self.assertEqual(result, expected_distances)

    def test_floyd_warshall1(self):
        result = self.graph1.floyd_warshall()
        expected_distances = {
            "A": {"A": 0, "B": float("inf"), "C": float("inf"), "D": float("inf")},
            "B": {"A": float("inf"), "B": 0, "C": float("inf"), "D": float("inf")},
            "C": {"A": float("inf"), "B": float("inf"), "C": 0, "D": float("inf")},
            "D": {"A": float("inf"), "B": float("inf"), "C": float("inf"), "D": 0},
        }
        self.assertEqual(result, expected_distances)

    def test_floyd_warshall2(self):
        result = self.graph2.floyd_warshall()
        expected_distances = {}
        self.assertEqual(result, expected_distances)

    def test_bellman_ford(self):
        result = self.graph.bellman_ford("A")
        expected_distances = {"A": 0, "B": 1, "C": 3, "D": 4}
        for v in expected_distances:
            self.assertEqual(result[v]["distance"], expected_distances[v])

    def test_bellman_ford_negative_cycle(self):
        vertices = ["A", "B", "C", "D"]
        edges = [("A", "B", 1), ("B", "C", -2), ("C", "D", 1), ("D", "B", -1)]
        graph = Graph.Graph(vertices, edges, directed=True)
        with self.assertRaises(ValueError):
            graph.bellman_ford("A")

    def test_bellman_ford1(self):
        result = self.graph1.bellman_ford("A")
        expected_distances = {
            "A": 0,
            "B": float("inf"),
            "C": float("inf"),
            "D": float("inf"),
        }
        for v in expected_distances:
            self.assertEqual(result[v]["distance"], expected_distances[v])

    def test_bellman_ford2(self):
        with self.assertRaises(ValueError):
            self.graph2.bellman_ford("A")


if __name__ == "__main__":
    unittest.main()
