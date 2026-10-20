import unittest
from unittest.mock import patch

from algorithm_library.python.graph.Bellman_ford import bellman_ford, inf
from algorithm_library.python.graph.EulerTour import EulerTour
from algorithm_library.python.graph.LCA import LCA
import algorithm_library.python.graph.WarshallFloyd as warshall_floyd


class LCAPathTests(unittest.TestCase):
    def test_path_interior_endpoints_and_branches(self):
        # 1 - 2 - 3, with another branch 2 - 4
        graph = [[], [2], [1, 3, 4], [2], [2]]
        lca = LCA(4, graph, 1)
        for u, v in [(1, 3), (3, 1)]:
            for a in [1, 2, 3]:
                with self.subTest(u=u, v=v, a=a):
                    self.assertTrue(lca.is_on_path(u, v, a))
            self.assertFalse(lca.is_on_path(u, v, 4))
        self.assertTrue(lca.is_on_path(2, 2, 2))
        self.assertFalse(lca.is_on_path(2, 2, 1))


class EulerTourDistanceTests(unittest.TestCase):
    def test_weighted_path_sum(self):
        tour = EulerTour(4)
        tour.add_edge(1, 2, 3)
        tour.add_edge(1, 3, 5)
        tour.add_edge(3, 4, 11)
        tour.build(1)
        for u, v, expected in [(1, 2, 3), (2, 4, 19), (3, 4, 11), (4, 4, 0)]:
            with self.subTest(u=u, v=v):
                self.assertEqual(tour.get_distance(u, v), expected)
                self.assertEqual(tour.get_distance(v, u), expected)

    def test_single_vertex_and_zero_or_negative_weights(self):
        tour = EulerTour(1)
        tour.build(1)
        self.assertEqual(tour.get_distance(1, 1), 0)

        tour = EulerTour(3)
        tour.add_edge(1, 2, 0)
        tour.add_edge(2, 3, -7)
        tour.build(1)
        self.assertEqual(tour.get_distance(1, 3), -7)
        self.assertEqual(tour.get_distance(2, 3), -7)


class BellmanFordTests(unittest.TestCase):
    def test_unreachable_negative_edge_keeps_infinite_distance(self):
        self.assertEqual(bellman_ford([(2, 3, -1)], 3, 1), ([inf, 0, inf, inf], False))

    def test_unreachable_negative_cycle_is_ignored(self):
        edges = [(2, 3, -1), (3, 2, 0)]
        self.assertEqual(bellman_ford(edges, 3, 1), ([inf, 0, inf, inf], False))

    def test_reachable_negative_cycle_is_detected(self):
        edges = [(1, 2, 0), (2, 3, -1), (3, 2, 0)]
        self.assertTrue(bellman_ford(edges, 3, 1)[1])

    def test_negative_edges_propagate_across_multiple_passes(self):
        edges = [(3, 4, 2), (2, 3, -5), (1, 2, 7)]
        self.assertEqual(bellman_ford(edges, 4, 1), ([inf, 0, 7, 2, 4], False))

    def test_source_can_be_a_different_vertex(self):
        edges = [(3, 4, -5), (1, 2, -7)]
        self.assertEqual(bellman_ford(edges, 4, 3), ([inf, inf, inf, 0, -5], False))


class WarshallFloydTests(unittest.TestCase):
    def distances(self, graph):
        with patch.multiple(
            warshall_floyd, N=len(graph) - 1, G=graph, inf=inf, create=True
        ):
            return warshall_floyd.WarshallFloyd()

    def test_one_sided_edges_produce_undirected_paths(self):
        dist = self.distances([[], [(2, 4)], [(3, 6)], [], []])
        self.assertEqual(dist[1][2], 4)
        self.assertEqual(dist[2][1], 4)
        self.assertEqual(dist[1][3], 10)
        self.assertEqual(dist[3][1], 10)
        self.assertEqual(dist[1][4], inf)

    def test_parallel_edges_keep_the_smallest_cost(self):
        dist = self.distances([[], [(2, 1), (2, 9), (2, 3)], []])
        self.assertEqual(dist[1][2], 1)
        self.assertEqual(dist[2][1], 1)

    def test_edges_can_be_supplied_from_both_endpoints(self):
        dist = self.distances([[], [(2, 7)], [(1, 7), (3, 2)], [(2, 2)]])
        self.assertEqual(dist[1][3], 9)
        self.assertEqual(dist[3][1], 9)


if __name__ == "__main__":
    unittest.main()
