import itertools
import random
import unittest
from collections import deque

from algorithm_library.python.graph.EulerTour import EulerTour


def rooted_tree(graph, root):
    parents = {root: root}
    depths = {root: 0}
    distances = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for u, weight in graph[v]:
            if u in parents:
                continue
            parents[u] = v
            depths[u] = depths[v] + 1
            distances[u] = distances[v] + weight
            queue.append(u)
    return parents, depths, distances


def naive_lca(u, v, parents, depths):
    while depths[u] > depths[v]:
        u = parents[u]
    while depths[v] > depths[u]:
        v = parents[v]
    while u != v:
        u, v = parents[u], parents[v]
    return u


class EulerTourTests(unittest.TestCase):
    def test_zero_based_vertices_and_tree_sizes(self):
        rng = random.Random(20261026)
        for n in [1, 2, 8, 9, 16, 17, 32, 33, 127, 128, 129, 257]:
            for shape in ["chain", "star", "random"]:
                edges = []
                graph = [[] for _ in range(n)]
                for v in range(1, n):
                    parent = v - 1 if shape == "chain" else 0
                    if shape == "random":
                        parent = rng.randrange(v)
                    weight = rng.randrange(-100, 101)
                    edges.append((parent, v, weight))
                    graph[parent].append((v, weight))
                    graph[v].append((parent, weight))
                rng.shuffle(edges)
                for root in {0, n // 2, n - 1}:
                    with self.subTest(n=n, shape=shape, root=root):
                        tour = EulerTour(n)
                        for u, v, weight in edges:
                            tour.add_edge(u, v, weight)
                        tour.build(root)
                        parents, depths, distances = rooted_tree(graph, root)
                        self.assertEqual(len(tour.depth), 2 * n - 1)
                        self.assertEqual(sorted(tour.es), list(range(1 - n, n)))
                        for v in range(n):
                            self.assertEqual(tour.path_sum(v), distances[v])
                            self.assertEqual(tour.depth[tour._in[v]], depths[v])
                        queries = (
                            itertools.product(range(n), repeat=2)
                            if n <= 33
                            else [
                                (rng.randrange(n), rng.randrange(n))
                                for _ in range(2000)
                            ]
                        )
                        for u, v in queries:
                            expected = naive_lca(u, v, parents, depths)
                            self.assertEqual(tour.lca(u, v), expected)
                            self.assertEqual(
                                tour.get_distance(u, v),
                                distances[u] + distances[v] - 2 * distances[expected],
                            )

    def test_weight_updates_keep_lca_valid(self):
        rng = random.Random(924)
        n = 65
        edges = [(rng.randrange(v), v, rng.randrange(-100, 101)) for v in range(1, n)]
        for root in [0, n // 2, n - 1]:
            tour = EulerTour(n)
            for u, v, weight in edges:
                tour.add_edge(u, v, weight)
            tour.build(root)
            weights = [weight for _, _, weight in edges]
            for _ in range(10):
                edge = rng.randrange(n - 1)
                delta = rng.randrange(-100, 101)
                weights[edge] += delta
                tour.fen.add(tour.es.index(edge + 1), delta)
                tour.fen.add(tour.es.index(-edge - 1), -delta)
                graph = [[] for _ in range(n)]
                for (u, v, _), weight in zip(edges, weights):
                    graph[u].append((v, weight))
                    graph[v].append((u, weight))
                parents, depths, distances = rooted_tree(graph, root)
                for v in range(n):
                    self.assertEqual(tour.path_sum(v), distances[v])
                for _ in range(100):
                    u, v = rng.randrange(n), rng.randrange(n)
                    expected = naive_lca(u, v, parents, depths)
                    self.assertEqual(tour.lca(u, v), expected)
                    self.assertEqual(
                        tour.get_distance(u, v),
                        distances[u] + distances[v] - 2 * distances[expected],
                    )

    def test_deep_chain_without_recursion(self):
        n = 20000
        root = n // 2
        tour = EulerTour(n)
        for v in range(1, n):
            tour.add_edge(v - 1, v, 1)
        tour.build(root)
        for u, v in [(0, n - 1), (0, root), (0, 1), (n - 2, n - 1), (root, root)]:
            self.assertEqual(tour.lca(u, v), min(max(root, min(u, v)), max(u, v)))
            self.assertEqual(tour.get_distance(u, v), abs(u - v))


if __name__ == "__main__":
    unittest.main()
