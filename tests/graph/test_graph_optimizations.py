import itertools
import random
import unittest
from collections import deque

from algorithm_library.python.graph.EulerTour import EulerTour
from algorithm_library.python.graph.LCA import LCA
from algorithm_library.python.graph.SCC import SCC
from algorithm_library.python.graph.TopologicalSort import TopologicalSort
from algorithm_library.python.graph.maxflow import maximum_flow


def tree_distances(graph, start):
    distances = {start: 0}
    parents = {start: None}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for u, weight in graph[v]:
            if u not in distances:
                distances[u] = distances[v] + weight
                parents[u] = v
                queue.append(u)
    return distances, parents


class TreeOptimizationTests(unittest.TestCase):
    def test_lca_and_weighted_distances_with_different_roots(self):
        rng = random.Random(819)
        for n in [1, 2, 3, 7, 8, 9, 31, 32, 33]:
            for shape in ["chain", "star", "random"]:
                graph = [[] for _ in range(n + 1)]
                weighted = [[] for _ in range(n + 1)]
                edges = []
                for v in range(2, n + 1):
                    parent = v - 1 if shape == "chain" else 1
                    if shape == "random":
                        parent = rng.randrange(1, v)
                    weight = rng.randrange(-100, 101)
                    graph[parent].append(v)
                    graph[v].append(parent)
                    weighted[parent].append((v, weight))
                    weighted[v].append((parent, weight))
                    edges.append((parent, v, weight))
                for root in {1, n}:
                    lca = LCA(n, graph, root)
                    tour = EulerTour(n)
                    for u, v, weight in edges:
                        tour.add_edge(u, v, weight)
                    tour.build(root)
                    root_distances, parents = tree_distances(weighted, root)
                    for u in range(1, n + 1):
                        self.assertEqual(tour.path_sum(u), root_distances[u])
                        ancestors = set()
                        v = u
                        while v is not None:
                            ancestors.add(v)
                            v = parents[v]
                        distances, _ = tree_distances(weighted, u)
                        for v in range(1, n + 1):
                            common = v
                            while common not in ancestors:
                                common = parents[common]
                            self.assertEqual(lca.lca(u, v), common)
                            self.assertEqual(tour.lca(u, v), common)
                            self.assertEqual(tour.get_distance(u, v), distances[v])

    def test_linear_fenwick_build_and_point_updates(self):
        rng = random.Random(123)
        for n in [0, 1, 2, 3, 7, 8, 9, 63, 64, 65, 127]:
            values = [rng.randrange(-100, 101) for _ in range(n)]
            tour = EulerTour(1)
            tour.edge_cost = values[:]
            tour._build_fentree()
            self.assertEqual(tour.edge_cost, values)
            if values:
                values[0] = 0
            for r in range(n + 1):
                self.assertEqual(tour.fen.sum0(r), sum(values[:r]))
            if n:
                for _ in range(10):
                    i = rng.randrange(n)
                    delta = rng.randrange(-100, 101)
                    tour.fen.add(i, delta)
                    values[i] += delta
                    self.assertEqual(tour.fen.sum0(i + 1), sum(values[: i + 1]))
                    self.assertEqual(tour.fen.sum0(n), sum(values))


class SCCOptimizationTests(unittest.TestCase):
    def check_components(self, n, edges):
        graph = SCC(n)
        reach = [[i == j for j in range(n)] for i in range(n)]
        for u, v in edges:
            graph.addEdge(u, v)
            reach[u][v] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reach[i][j] |= reach[i][k] and reach[k][j]
        groups = graph.build_scc()
        self.assertEqual(sorted(v for group in groups for v in group), list(range(n)))
        ids = [None] * n
        for i, group in enumerate(groups):
            self.assertTrue(group)
            for v in group:
                ids[v] = i
        for i in range(n):
            for j in range(n):
                self.assertEqual(ids[i] == ids[j], reach[i][j] and reach[j][i])
        expected_dag = [[] for _ in groups]
        for u, v in edges:
            self.assertLessEqual(ids[u], ids[v])
            if ids[u] != ids[v]:
                expected_dag[ids[u]].append(ids[v])
        self.assertEqual(graph.build_dag(), expected_dag)

    def test_all_directed_graphs_on_three_vertices(self):
        pairs = list(itertools.product(range(3), repeat=2))
        for mask in range(1 << len(pairs)):
            edges = [edge for i, edge in enumerate(pairs) if mask >> i & 1]
            self.check_components(3, edges)

    def test_empty_disconnected_and_parallel_edges(self):
        self.check_components(0, [])
        self.check_components(7, [(0, 1), (0, 1), (1, 0), (1, 2), (3, 3), (4, 5)])

    def test_random_graphs(self):
        rng = random.Random(941)
        for _ in range(100):
            n = rng.randrange(1, 10)
            edges = [(rng.randrange(n), rng.randrange(n)) for _ in range(3 * n)]
            self.check_components(n, edges)

    def test_long_chain_and_cycle(self):
        n = 5000
        graph = SCC(n)
        for v in range(n - 1):
            graph.addEdge(v, v + 1)
        self.assertEqual(graph.build_scc(), [[v] for v in range(n)])
        graph.addEdge(n - 1, 0)
        self.assertEqual(graph.build_scc(), [list(range(n))])


class TopologicalSortOptimizationTests(unittest.TestCase):
    def test_all_directed_graphs_on_three_vertices(self):
        pairs = list(itertools.product(range(1, 4), repeat=2))
        permutations = list(itertools.permutations(range(1, 4)))
        for mask in range(1 << len(pairs)):
            edges = [edge for i, edge in enumerate(pairs) if mask >> i & 1]
            graph = [[] for _ in range(4)]
            for u, v in edges:
                graph[u].append(v)
            valid = []
            for order in permutations:
                index = {v: i for i, v in enumerate(order)}
                if all(index[u] < index[v] for u, v in edges):
                    valid.append(order)
            result = TopologicalSort(3, graph)
            if valid:
                self.assertIn(tuple(result), valid)
            else:
                self.assertEqual(result, [])

    def test_fifo_order_and_parallel_edges(self):
        graph = [[], [3, 3], [3], [4], []]
        self.assertEqual(TopologicalSort(4, graph), [1, 2, 3, 4])
        self.assertEqual(TopologicalSort(4, [[], [], [], [], []]), [1, 2, 3, 4])
        self.assertEqual(TopologicalSort(0, [[]]), [])


class MaximumFlowOptimizationTests(unittest.TestCase):
    def flow_graph(self, n, edges):
        graph = maximum_flow(n - 1)
        for u, v, capacity in edges:
            graph.add_edge(u, v, capacity)
        return graph

    def test_random_networks_against_all_cuts(self):
        rng = random.Random(927)
        for _ in range(200):
            n = rng.randrange(2, 8)
            edges = [
                (rng.randrange(n), rng.randrange(n), rng.randrange(11))
                for _ in range(4 * n)
            ]
            expected = min(
                sum(c for u, v, c in edges if mask >> u & 1 and not mask >> v & 1)
                for mask in range(1 << n)
                if mask & 1 and not mask >> (n - 1) & 1
            )
            graph = self.flow_graph(n, edges)
            self.assertEqual(graph.maxflow(0, n - 1), expected)
            self.assertEqual(graph.maxflow(0, n - 1), 0)

    def test_matching_requires_residual_rerouting(self):
        edges = [(0, 1, 1), (0, 2, 1), (1, 3, 1), (1, 4, 1), (2, 3, 1)]
        edges += [(3, 5, 1), (4, 5, 1)]
        self.assertEqual(self.flow_graph(6, edges).maxflow(0, 5), 2)

    def test_large_capacities_parallel_and_antiparallel_edges(self):
        big = 10**30
        edges = [(0, 1, big), (0, 1, 3), (1, 0, 7), (1, 2, big + 3)]
        self.assertEqual(self.flow_graph(3, edges).maxflow(0, 2), big + 3)

    def test_adding_edges_after_a_flow(self):
        graph = self.flow_graph(3, [(0, 1, 2), (1, 2, 2)])
        self.assertEqual(graph.maxflow(0, 2), 2)
        graph.add_edge(0, 2, 3)
        self.assertEqual(graph.maxflow(0, 2), 3)

    def test_long_path_does_not_need_recursion(self):
        n = 5000
        edges = [(v, v + 1, 7) for v in range(n - 1)]
        self.assertEqual(self.flow_graph(n, edges).maxflow(0, n - 1), 7)


if __name__ == "__main__":
    unittest.main()
