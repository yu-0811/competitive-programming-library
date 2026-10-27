import random
import unittest
from collections import deque

from algorithm_library.python.graph.LCA import LCA


def rooted_tree(graph, root):
    parents = [-1] * len(graph)
    depths = [-1] * len(graph)
    depths[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depths[v] == -1:
                parents[v] = u
                depths[v] = depths[u] + 1
                queue.append(v)
    return parents, depths


def naive_lca(u, v, parents, depths):
    while depths[u] > depths[v]:
        u = parents[u]
    while depths[v] > depths[u]:
        v = parents[v]
    while u != v:
        u = parents[u]
        v = parents[v]
    return u


class LCATests(unittest.TestCase):
    def check_tree(self, n, graph, root, vertices):
        tree = LCA(n, graph, root)
        parents, depths = rooted_tree(graph, root)
        self.assertEqual(tree.depth[: len(graph)], depths)
        self.assertEqual(len(tree.depth), n + 1)
        self.assertEqual(tree.p[: len(graph)], parents)
        self.assertEqual(len(tree.p), n + 1)
        for u in vertices:
            for v in vertices:
                ancestor = v
                while ancestor != -1 and ancestor != u:
                    ancestor = parents[ancestor]
                self.assertEqual(tree.is_in_subtree(u, v), ancestor == u)
                common = naive_lca(u, v, parents, depths)
                self.assertEqual(tree.lca(u, v), common)
                distance = depths[u] + depths[v] - 2 * depths[common]
                self.assertEqual(tree.get_distance(u, v), distance)
                path = {common}
                for x in (u, v):
                    while x != common:
                        path.add(x)
                        x = parents[x]
                for a in vertices:
                    self.assertEqual(tree.is_on_path(u, v, a), a in path)

    def test_shapes_index_bases_and_roots(self):
        rng = random.Random(819)
        for n in [1, 2, 3, 7, 8, 9, 16, 17]:
            for base in [0, 1]:
                vertices = list(range(base, n + base))
                for shape in ["chain", "star", "balanced", "random"]:
                    graph = [[] for _ in range(n + base)]
                    # 頂点番号と深さの相関をなくす。
                    labels = rng.sample(vertices, n)
                    for i in range(1, n):
                        p = (
                            i - 1
                            if shape == "chain"
                            else 0
                            if shape == "star"
                            else (i - 1) // 2
                            if shape == "balanced"
                            else rng.randrange(i)
                        )
                        u, v = labels[p], labels[i]
                        graph[u].append(v)
                        graph[v].append(u)
                    for root in {labels[0], labels[-1]}:
                        with self.subTest(n=n, base=base, shape=shape, root=root):
                            self.check_tree(n, graph, root, vertices)

    def test_directed_children_and_unused_vertices(self):
        graph = [[], [4, 2], [3], [], [5], [], []]
        self.check_tree(6, graph, 1, [1, 2, 3, 4, 5])
        tree = LCA(6, graph, 1)
        self.assertEqual(tree.depth[0], -1)
        self.assertEqual(tree.depth[6], -1)
        self.assertEqual(tree.p[0], -1)
        self.assertEqual(tree.p[6], -1)

    def test_larger_relabelled_trees(self):
        rng = random.Random(20261027)
        for n in [31, 32, 33, 63, 64, 65, 127, 128, 129, 257, 1023]:
            labels = rng.sample(range(n), n)
            graph = [[] for _ in range(n)]
            for i in range(1, n):
                u, v = labels[rng.randrange(i)], labels[i]
                graph[u].append(v)
                graph[v].append(u)
            for root in [labels[0], labels[n // 2]]:
                tree = LCA(n, graph, root)
                parents, depths = rooted_tree(graph, root)
                for _ in range(1000):
                    u, v = rng.randrange(n), rng.randrange(n)
                    common = naive_lca(u, v, parents, depths)
                    self.assertEqual(tree.lca(u, v), common)
                    self.assertEqual(
                        tree.get_distance(u, v),
                        depths[u] + depths[v] - 2 * depths[common],
                    )
                    ancestor = v
                    while ancestor != -1 and ancestor != u:
                        ancestor = parents[ancestor]
                    self.assertEqual(tree.is_in_subtree(u, v), ancestor == u)

    def test_long_chain_and_shallow_tree(self):
        n = 10000
        chain = [[] for _ in range(n)]
        for v in range(1, n):
            chain[v - 1].append(v)
            chain[v].append(v - 1)
        root = n // 3
        tree = LCA(n, chain, root)
        rng = random.Random(123)
        for _ in range(1000):
            u, v = rng.randrange(n), rng.randrange(n)
            self.assertEqual(tree.lca(u, v), min(max(root, min(u, v)), max(u, v)))
            self.assertEqual(tree.get_distance(u, v), abs(u - v))
        star = [list(range(1, n))] + [[] for _ in range(n - 1)]
        tree = LCA(n, star, 0)
        self.assertEqual(tree.lca(n - 1, n - 2), 0)
        self.assertEqual(tree.p[:n], [-1] + [0] * (n - 1))


if __name__ == "__main__":
    unittest.main()
