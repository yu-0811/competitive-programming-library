---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/graph/Bellman_ford.py
    title: algorithm_library/python/graph/Bellman_ford.py
  - icon: ':warning:'
    path: algorithm_library/python/graph/EulerTour.py
    title: algorithm_library/python/graph/EulerTour.py
  - icon: ':warning:'
    path: algorithm_library/python/graph/LCA.py
    title: algorithm_library/python/graph/LCA.py
  - icon: ':warning:'
    path: algorithm_library/python/graph/WarshallFloyd.py
    title: algorithm_library/python/graph/WarshallFloyd.py
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
  code: "import unittest\nfrom unittest.mock import patch\n\nfrom algorithm_library.python.graph.Bellman_ford\
    \ import bellman_ford, inf\nfrom algorithm_library.python.graph.EulerTour import\
    \ EulerTour\nfrom algorithm_library.python.graph.LCA import LCA\nimport algorithm_library.python.graph.WarshallFloyd\
    \ as warshall_floyd\n\n\nclass LCAPathTests(unittest.TestCase):\n    def test_path_interior_endpoints_and_branches(self):\n\
    \        # 1 - 2 - 3, with another branch 2 - 4\n        graph = [[], [2], [1,\
    \ 3, 4], [2], [2]]\n        lca = LCA(4, graph, 1)\n        for u, v in [(1, 3),\
    \ (3, 1)]:\n            for a in [1, 2, 3]:\n                with self.subTest(u=u,\
    \ v=v, a=a):\n                    self.assertTrue(lca.is_on_path(u, v, a))\n \
    \           self.assertFalse(lca.is_on_path(u, v, 4))\n        self.assertTrue(lca.is_on_path(2,\
    \ 2, 2))\n        self.assertFalse(lca.is_on_path(2, 2, 1))\n\n\nclass EulerTourDistanceTests(unittest.TestCase):\n\
    \    def test_weighted_path_sum(self):\n        tour = EulerTour(4)\n        tour.add_edge(1,\
    \ 2, 3)\n        tour.add_edge(1, 3, 5)\n        tour.add_edge(3, 4, 11)\n   \
    \     tour.build(1)\n        for u, v, expected in [(1, 2, 3), (2, 4, 19), (3,\
    \ 4, 11), (4, 4, 0)]:\n            with self.subTest(u=u, v=v):\n            \
    \    self.assertEqual(tour.get_distance(u, v), expected)\n                self.assertEqual(tour.get_distance(v,\
    \ u), expected)\n\n    def test_single_vertex_and_zero_or_negative_weights(self):\n\
    \        tour = EulerTour(1)\n        tour.build(1)\n        self.assertEqual(tour.get_distance(1,\
    \ 1), 0)\n\n        tour = EulerTour(3)\n        tour.add_edge(1, 2, 0)\n    \
    \    tour.add_edge(2, 3, -7)\n        tour.build(1)\n        self.assertEqual(tour.get_distance(1,\
    \ 3), -7)\n        self.assertEqual(tour.get_distance(2, 3), -7)\n\n\nclass BellmanFordTests(unittest.TestCase):\n\
    \    def test_unreachable_negative_edge_keeps_infinite_distance(self):\n     \
    \   self.assertEqual(bellman_ford([(2, 3, -1)], 3, 1), ([inf, 0, inf, inf], False))\n\
    \n    def test_unreachable_negative_cycle_is_ignored(self):\n        edges = [(2,\
    \ 3, -1), (3, 2, 0)]\n        self.assertEqual(bellman_ford(edges, 3, 1), ([inf,\
    \ 0, inf, inf], False))\n\n    def test_reachable_negative_cycle_is_detected(self):\n\
    \        edges = [(1, 2, 0), (2, 3, -1), (3, 2, 0)]\n        self.assertTrue(bellman_ford(edges,\
    \ 3, 1)[1])\n\n    def test_negative_edges_propagate_across_multiple_passes(self):\n\
    \        edges = [(3, 4, 2), (2, 3, -5), (1, 2, 7)]\n        self.assertEqual(bellman_ford(edges,\
    \ 4, 1), ([inf, 0, 7, 2, 4], False))\n\n    def test_source_can_be_a_different_vertex(self):\n\
    \        edges = [(3, 4, -5), (1, 2, -7)]\n        self.assertEqual(bellman_ford(edges,\
    \ 4, 3), ([inf, inf, inf, 0, -5], False))\n\n\nclass WarshallFloydTests(unittest.TestCase):\n\
    \    def distances(self, graph):\n        with patch.multiple(\n            warshall_floyd,\
    \ N=len(graph) - 1, G=graph, inf=inf, create=True\n        ):\n            return\
    \ warshall_floyd.WarshallFloyd()\n\n    def test_one_sided_edges_produce_undirected_paths(self):\n\
    \        dist = self.distances([[], [(2, 4)], [(3, 6)], [], []])\n        self.assertEqual(dist[1][2],\
    \ 4)\n        self.assertEqual(dist[2][1], 4)\n        self.assertEqual(dist[1][3],\
    \ 10)\n        self.assertEqual(dist[3][1], 10)\n        self.assertEqual(dist[1][4],\
    \ inf)\n\n    def test_parallel_edges_keep_the_smallest_cost(self):\n        dist\
    \ = self.distances([[], [(2, 1), (2, 9), (2, 3)], []])\n        self.assertEqual(dist[1][2],\
    \ 1)\n        self.assertEqual(dist[2][1], 1)\n\n    def test_edges_can_be_supplied_from_both_endpoints(self):\n\
    \        dist = self.distances([[], [(2, 7)], [(1, 7), (3, 2)], [(2, 2)]])\n \
    \       self.assertEqual(dist[1][3], 9)\n        self.assertEqual(dist[3][1],\
    \ 9)\n\n\nif __name__ == \"__main__\":\n    unittest.main()\n"
  dependsOn:
  - algorithm_library/python/graph/Bellman_ford.py
  - algorithm_library/python/graph/EulerTour.py
  - algorithm_library/python/graph/LCA.py
  - algorithm_library/python/graph/WarshallFloyd.py
  isVerificationFile: false
  path: tests/graph/test_graph_regressions.py
  requiredBy: []
  timestamp: '2026-10-20 12:07:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/graph/test_graph_regressions.py
layout: document
redirect_from:
- /library/tests/graph/test_graph_regressions.py
- /library/tests/graph/test_graph_regressions.py.html
title: tests/graph/test_graph_regressions.py
---
