---
data:
  _extendedDependsOn: []
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
  code: "import random\nimport runpy\nimport unittest\nfrom pathlib import Path\n\n\
    \nLIBRARY = (\n    Path(__file__).resolve().parents[2] / \"algorithm_library/python/data-structure\"\
    \n)\nTupleSegtree = runpy.run_path(str(LIBRARY / \"TupleSegtree.py\"))[\"TupleSegtree\"\
    ]\n\n\nclass TupleSegtreeTests(unittest.TestCase):\n    def test_random_updates_queries_and_searches(self):\n\
    \        rng = random.Random(20261025)\n        for arity in [2, 3]:\n       \
    \     e = (0,) * arity\n\n            def op(x, y):\n                return tuple(a\
    \ + b for a, b in zip(x, y))\n\n            for n in [0, 1, 2, 3, 7, 8, 9, 31,\
    \ 32, 33]:\n                values = [tuple(rng.randrange(10) for _ in e) for\
    \ _ in range(n)]\n                tree = TupleSegtree(v=values, op=op, e=e)\n\
    \                for _ in range(120):\n                    if n:\n           \
    \             p = rng.randrange(n)\n                        x = tuple(rng.randrange(10)\
    \ for _ in e)\n                        if rng.randrange(2):\n                \
    \            tree.set(p, x)\n                            values[p] = x\n     \
    \                   else:\n                            tree.add(p, x)\n      \
    \                      values[p] = op(values[p], x)\n                        self.assertEqual(tree.get(p),\
    \ values[p])\n                    left = rng.randrange(n + 1)\n              \
    \      right = rng.randrange(left, n + 1)\n                    self.assertEqual(\n\
    \                        tree.prod(left, right),\n                        tuple(\n\
    \                            sum(x[j] for x in values[left:right]) for j in range(arity)\n\
    \                        ),\n                    )\n                    self.assertEqual(\n\
    \                        tree.all_prod(),\n                        tuple(sum(x[j]\
    \ for x in values) for j in range(arity)),\n                    )\n          \
    \          limit = rng.randrange(sum(x[0] for x in values) + 2)\n            \
    \        expected_right = left\n                    total = 0\n              \
    \      while (\n                        expected_right < n\n                 \
    \       and total + values[expected_right][0] <= limit\n                    ):\n\
    \                        total += values[expected_right][0]\n                \
    \        expected_right += 1\n                    self.assertEqual(\n        \
    \                tree.max_right(left, lambda x: x[0] <= limit), expected_right\n\
    \                    )\n                    expected_left = right\n          \
    \          total = 0\n                    while (\n                        expected_left\
    \ and total + values[expected_left - 1][0] <= limit\n                    ):\n\
    \                        expected_left -= 1\n                        total +=\
    \ values[expected_left][0]\n                    self.assertEqual(\n          \
    \              tree.min_left(right, lambda x: x[0] <= limit), expected_left\n\
    \                    )\n                self.assertEqual(str(tree), str(values))\n\
    \n    def test_noncommutative_products_and_searches(self):\n        values = list(\"\
    abcdefghi\")\n        tree = TupleSegtree(\n            [(x, 1) for x in values],\n\
    \            lambda x, y: (x[0] + y[0], x[1] + y[1]),\n            (\"\", 0),\n\
    \        )\n        for p, letter in [(0, \"z\"), (4, \"x\"), (8, \"y\")]:\n \
    \           tree.set(p, (letter, 1))\n            values[p] = letter\n       \
    \     for left in range(10):\n                for right in range(left, 10):\n\
    \                    text = \"\".join(values[left:right])\n                  \
    \  self.assertEqual(tree.prod(left, right), (text, right - left))\n          \
    \          self.assertEqual(\n                        tree.max_right(left, lambda\
    \ x: text.startswith(x[0])), right\n                    )\n                  \
    \  self.assertEqual(\n                        tree.min_left(right, lambda x: text.endswith(x[0])),\
    \ left\n                    )\n\n    def test_float_and_large_integer_components(self):\n\
    \        values = [(10**100, 0.5, -3), (-(10**100), -1.5, 8), (7, 2.0, -5)]\n\
    \        tree = TupleSegtree(\n            values, lambda x, y: tuple(a + b for\
    \ a, b in zip(x, y)), (0, 0.0, 0)\n        )\n        values[0] = (0, 0.0, 0)\n\
    \        self.assertEqual(tree.get(0), (10**100, 0.5, -3))\n        tree.add(1,\
    \ (10**100, 0.5, -2))\n        self.assertEqual(tree.get(1), (0, -1.0, 6))\n \
    \       self.assertEqual(tree.all_prod(), (10**100 + 7, 1.5, -2))\n        self.assertEqual(tree.prod(1,\
    \ 3), (7, 1.0, 1))\n\n    def test_unregistered_arities(self):\n        for arity\
    \ in [0, 1, 4]:\n            with self.subTest(arity=arity):\n               \
    \ with self.assertRaises(AssertionError):\n                    TupleSegtree([],\
    \ lambda x, y: x, (0,) * arity)\n\n\nif __name__ == \"__main__\":\n    unittest.main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/test_tuple_segtree.py
  requiredBy: []
  timestamp: '2026-10-25 10:09:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/test_tuple_segtree.py
layout: document
redirect_from:
- /library/tests/data_structure/test_tuple_segtree.py
- /library/tests/data_structure/test_tuple_segtree.py.html
title: tests/data_structure/test_tuple_segtree.py
---
