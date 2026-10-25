---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/graph/EulerTour.py
    title: algorithm_library/python/graph/EulerTour.py
  - icon: ':warning:'
    path: algorithm_library/python/graph/LCA.py
    title: algorithm_library/python/graph/LCA.py
  - icon: ':heavy_check_mark:'
    path: algorithm_library/python/graph/SCC.py
    title: algorithm_library/python/graph/SCC.py
  - icon: ':warning:'
    path: algorithm_library/python/graph/TopologicalSort.py
    title: algorithm_library/python/graph/TopologicalSort.py
  - icon: ':warning:'
    path: algorithm_library/python/graph/maxflow.py
    title: algorithm_library/python/graph/maxflow.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import itertools\nimport random\nimport unittest\nfrom collections import\
    \ deque\n\nfrom algorithm_library.python.graph.EulerTour import EulerTour\nfrom\
    \ algorithm_library.python.graph.LCA import LCA\nfrom algorithm_library.python.graph.SCC\
    \ import SCC\nfrom algorithm_library.python.graph.TopologicalSort import TopologicalSort\n\
    from algorithm_library.python.graph.maxflow import maximum_flow\n\n\ndef tree_distances(graph,\
    \ start):\n    distances = {start: 0}\n    parents = {start: None}\n    queue\
    \ = deque([start])\n    while queue:\n        v = queue.popleft()\n        for\
    \ u, weight in graph[v]:\n            if u not in distances:\n               \
    \ distances[u] = distances[v] + weight\n                parents[u] = v\n     \
    \           queue.append(u)\n    return distances, parents\n\n\nclass TreeOptimizationTests(unittest.TestCase):\n\
    \    def test_lca_and_weighted_distances_with_different_roots(self):\n       \
    \ rng = random.Random(819)\n        for n in [1, 2, 3, 7, 8, 9, 31, 32, 33]:\n\
    \            for shape in [\"chain\", \"star\", \"random\"]:\n               \
    \ graph = [[] for _ in range(n + 1)]\n                weighted = [[] for _ in\
    \ range(n + 1)]\n                edges = []\n                for v in range(2,\
    \ n + 1):\n                    parent = v - 1 if shape == \"chain\" else 1\n \
    \                   if shape == \"random\":\n                        parent =\
    \ rng.randrange(1, v)\n                    weight = rng.randrange(-100, 101)\n\
    \                    graph[parent].append(v)\n                    graph[v].append(parent)\n\
    \                    weighted[parent].append((v, weight))\n                  \
    \  weighted[v].append((parent, weight))\n                    edges.append((parent,\
    \ v, weight))\n                for root in {1, n}:\n                    lca =\
    \ LCA(n, graph, root)\n                    tour = EulerTour(n)\n             \
    \       for u, v, weight in edges:\n                        tour.add_edge(u, v,\
    \ weight)\n                    tour.build(root)\n                    root_distances,\
    \ parents = tree_distances(weighted, root)\n                    for u in range(1,\
    \ n + 1):\n                        self.assertEqual(tour.path_sum(u), root_distances[u])\n\
    \                        ancestors = set()\n                        v = u\n  \
    \                      while v is not None:\n                            ancestors.add(v)\n\
    \                            v = parents[v]\n                        distances,\
    \ _ = tree_distances(weighted, u)\n                        for v in range(1, n\
    \ + 1):\n                            common = v\n                            while\
    \ common not in ancestors:\n                                common = parents[common]\n\
    \                            self.assertEqual(lca.lca(u, v), common)\n       \
    \                     self.assertEqual(tour.lca(u, v), common)\n             \
    \               self.assertEqual(tour.get_distance(u, v), distances[v])\n\n  \
    \  def test_linear_fenwick_build_and_point_updates(self):\n        rng = random.Random(123)\n\
    \        for n in [0, 1, 2, 3, 7, 8, 9, 63, 64, 65, 127]:\n            values\
    \ = [rng.randrange(-100, 101) for _ in range(n)]\n            tour = EulerTour(1)\n\
    \            tour.edge_cost = values[:]\n            tour._build_fentree()\n \
    \           self.assertEqual(tour.edge_cost, values)\n            if values:\n\
    \                values[0] = 0\n            for r in range(n + 1):\n         \
    \       self.assertEqual(tour.fen.sum0(r), sum(values[:r]))\n            if n:\n\
    \                for _ in range(10):\n                    i = rng.randrange(n)\n\
    \                    delta = rng.randrange(-100, 101)\n                    tour.fen.add(i,\
    \ delta)\n                    values[i] += delta\n                    self.assertEqual(tour.fen.sum0(i\
    \ + 1), sum(values[: i + 1]))\n                    self.assertEqual(tour.fen.sum0(n),\
    \ sum(values))\n\n\nclass SCCOptimizationTests(unittest.TestCase):\n    def check_components(self,\
    \ n, edges):\n        graph = SCC(n)\n        reach = [[i == j for j in range(n)]\
    \ for i in range(n)]\n        for u, v in edges:\n            graph.addEdge(u,\
    \ v)\n            reach[u][v] = True\n        for k in range(n):\n           \
    \ for i in range(n):\n                for j in range(n):\n                   \
    \ reach[i][j] |= reach[i][k] and reach[k][j]\n        groups = graph.build_scc()\n\
    \        self.assertEqual(sorted(v for group in groups for v in group), list(range(n)))\n\
    \        ids = [None] * n\n        for i, group in enumerate(groups):\n      \
    \      self.assertTrue(group)\n            for v in group:\n                ids[v]\
    \ = i\n        for i in range(n):\n            for j in range(n):\n          \
    \      self.assertEqual(ids[i] == ids[j], reach[i][j] and reach[j][i])\n     \
    \   expected_dag = [[] for _ in groups]\n        for u, v in edges:\n        \
    \    self.assertLessEqual(ids[u], ids[v])\n            if ids[u] != ids[v]:\n\
    \                expected_dag[ids[u]].append(ids[v])\n        self.assertEqual(graph.build_dag(),\
    \ expected_dag)\n\n    def test_all_directed_graphs_on_three_vertices(self):\n\
    \        pairs = list(itertools.product(range(3), repeat=2))\n        for mask\
    \ in range(1 << len(pairs)):\n            edges = [edge for i, edge in enumerate(pairs)\
    \ if mask >> i & 1]\n            self.check_components(3, edges)\n\n    def test_empty_disconnected_and_parallel_edges(self):\n\
    \        self.check_components(0, [])\n        self.check_components(7, [(0, 1),\
    \ (0, 1), (1, 0), (1, 2), (3, 3), (4, 5)])\n\n    def test_random_graphs(self):\n\
    \        rng = random.Random(941)\n        for _ in range(100):\n            n\
    \ = rng.randrange(1, 10)\n            edges = [(rng.randrange(n), rng.randrange(n))\
    \ for _ in range(3 * n)]\n            self.check_components(n, edges)\n\n    def\
    \ test_long_chain_and_cycle(self):\n        n = 5000\n        graph = SCC(n)\n\
    \        for v in range(n - 1):\n            graph.addEdge(v, v + 1)\n       \
    \ self.assertEqual(graph.build_scc(), [[v] for v in range(n)])\n        graph.addEdge(n\
    \ - 1, 0)\n        self.assertEqual(graph.build_scc(), [list(range(n))])\n\n\n\
    class TopologicalSortOptimizationTests(unittest.TestCase):\n    def test_all_directed_graphs_on_three_vertices(self):\n\
    \        pairs = list(itertools.product(range(1, 4), repeat=2))\n        permutations\
    \ = list(itertools.permutations(range(1, 4)))\n        for mask in range(1 <<\
    \ len(pairs)):\n            edges = [edge for i, edge in enumerate(pairs) if mask\
    \ >> i & 1]\n            graph = [[] for _ in range(4)]\n            for u, v\
    \ in edges:\n                graph[u].append(v)\n            valid = []\n    \
    \        for order in permutations:\n                index = {v: i for i, v in\
    \ enumerate(order)}\n                if all(index[u] < index[v] for u, v in edges):\n\
    \                    valid.append(order)\n            result = TopologicalSort(3,\
    \ graph)\n            if valid:\n                self.assertIn(tuple(result),\
    \ valid)\n            else:\n                self.assertEqual(result, [])\n\n\
    \    def test_fifo_order_and_parallel_edges(self):\n        graph = [[], [3, 3],\
    \ [3], [4], []]\n        self.assertEqual(TopologicalSort(4, graph), [1, 2, 3,\
    \ 4])\n        self.assertEqual(TopologicalSort(4, [[], [], [], [], []]), [1,\
    \ 2, 3, 4])\n        self.assertEqual(TopologicalSort(0, [[]]), [])\n\n\nclass\
    \ MaximumFlowOptimizationTests(unittest.TestCase):\n    def flow_graph(self, n,\
    \ edges):\n        graph = maximum_flow(n - 1)\n        for u, v, capacity in\
    \ edges:\n            graph.add_edge(u, v, capacity)\n        return graph\n\n\
    \    def test_random_networks_against_all_cuts(self):\n        rng = random.Random(927)\n\
    \        for _ in range(200):\n            n = rng.randrange(2, 8)\n         \
    \   edges = [\n                (rng.randrange(n), rng.randrange(n), rng.randrange(11))\n\
    \                for _ in range(4 * n)\n            ]\n            expected =\
    \ min(\n                sum(c for u, v, c in edges if mask >> u & 1 and not mask\
    \ >> v & 1)\n                for mask in range(1 << n)\n                if mask\
    \ & 1 and not mask >> (n - 1) & 1\n            )\n            graph = self.flow_graph(n,\
    \ edges)\n            self.assertEqual(graph.maxflow(0, n - 1), expected)\n  \
    \          self.assertEqual(graph.maxflow(0, n - 1), 0)\n\n    def test_matching_requires_residual_rerouting(self):\n\
    \        edges = [(0, 1, 1), (0, 2, 1), (1, 3, 1), (1, 4, 1), (2, 3, 1)]\n   \
    \     edges += [(3, 5, 1), (4, 5, 1)]\n        self.assertEqual(self.flow_graph(6,\
    \ edges).maxflow(0, 5), 2)\n\n    def test_large_capacities_parallel_and_antiparallel_edges(self):\n\
    \        big = 10**30\n        edges = [(0, 1, big), (0, 1, 3), (1, 0, 7), (1,\
    \ 2, big + 3)]\n        self.assertEqual(self.flow_graph(3, edges).maxflow(0,\
    \ 2), big + 3)\n\n    def test_adding_edges_after_a_flow(self):\n        graph\
    \ = self.flow_graph(3, [(0, 1, 2), (1, 2, 2)])\n        self.assertEqual(graph.maxflow(0,\
    \ 2), 2)\n        graph.add_edge(0, 2, 3)\n        self.assertEqual(graph.maxflow(0,\
    \ 2), 3)\n\n    def test_long_path_does_not_need_recursion(self):\n        n =\
    \ 5000\n        edges = [(v, v + 1, 7) for v in range(n - 1)]\n        self.assertEqual(self.flow_graph(n,\
    \ edges).maxflow(0, n - 1), 7)\n\n\nif __name__ == \"__main__\":\n    unittest.main()\n"
  dependsOn:
  - algorithm_library/python/graph/EulerTour.py
  - algorithm_library/python/graph/LCA.py
  - algorithm_library/python/graph/SCC.py
  - algorithm_library/python/graph/TopologicalSort.py
  - algorithm_library/python/graph/maxflow.py
  isVerificationFile: false
  path: tests/graph/test_graph_optimizations.py
  requiredBy: []
  timestamp: '2026-10-20 12:13:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/graph/test_graph_optimizations.py
layout: document
redirect_from:
- /library/tests/graph/test_graph_optimizations.py
- /library/tests/graph/test_graph_optimizations.py.html
title: tests/graph/test_graph_optimizations.py
---
