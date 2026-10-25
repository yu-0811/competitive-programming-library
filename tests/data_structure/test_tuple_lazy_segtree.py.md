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
    \n)\nTupleLazySegtree = runpy.run_path(str(LIBRARY / \"TupleLazySegtree.py\"))[\n\
    \    \"TupleLazySegtree\"\n]\n\n\ndef affine_tree(values, mod=None):\n    def\
    \ normalize(x):\n        return x if mod is None else x % mod\n\n    def op(x,\
    \ y):\n        return normalize(x[0] + y[0]), x[1] + y[1]\n\n    def mp(f, x):\n\
    \        return normalize(f[0] * x[0] + f[1] * x[1]), x[1]\n\n    def comp(f,\
    \ g):\n        return normalize(f[0] * g[0]), normalize(f[0] * g[1] + f[1])\n\n\
    \    return TupleLazySegtree(\n        v=[(normalize(x), 1) for x in values],\n\
    \        op=op,\n        e=(0, 0),\n        mp=mp,\n        comp=comp,\n     \
    \   ide=(1, 0),\n    )\n\n\nclass TupleLazySegtreeTests(unittest.TestCase):\n\
    \    def test_random_affine_updates_sets_and_queries(self):\n        rng = random.Random(20261020)\n\
    \        for mod in [1, 97, 998244353]:\n            for n in [0, 1, 2, 3, 7,\
    \ 8, 9, 31, 32, 33]:\n                values = [rng.randrange(mod) for _ in range(n)]\n\
    \                tree = affine_tree(values, mod)\n                for _ in range(160):\n\
    \                    kind = rng.randrange(5)\n                    left = rng.randrange(n\
    \ + 1)\n                    right = rng.randrange(left, n + 1)\n             \
    \       if kind == 0:\n                        b, c = rng.randrange(-100, 101),\
    \ rng.randrange(-100, 101)\n                        tree.apply(left, right, (b,\
    \ c))\n                        for i in range(left, right):\n                \
    \            values[i] = (b * values[i] + c) % mod\n                    elif kind\
    \ == 1 and n:\n                        p = rng.randrange(n)\n                \
    \        x = rng.randrange(-100, 101) % mod\n                        tree.set(p,\
    \ (x, 1))\n                        values[p] = x\n                    elif kind\
    \ == 2 and n:\n                        p = rng.randrange(n)\n                \
    \        b, c = rng.randrange(-100, 101), rng.randrange(-100, 101)\n         \
    \               tree.apply_point(p, (b, c))\n                        values[p]\
    \ = (b * values[p] + c) % mod\n                    elif kind == 3 and n:\n   \
    \                     p = rng.randrange(n)\n                        self.assertEqual(tree.get(p),\
    \ (values[p], 1))\n                    self.assertEqual(tree.all_prod(), (sum(values)\
    \ % mod, n))\n                    self.assertEqual(\n                        tree.prod(left,\
    \ right),\n                        (sum(values[left:right]) % mod, right - left),\n\
    \                    )\n                self.assertEqual(str(tree), str([(x, 1)\
    \ for x in values]))\n\n    def test_composition_order_and_stale_tags(self):\n\
    \        values = list(range(16))\n        tree = affine_tree(values)\n      \
    \  for left, right, b, c in [\n            (0, 16, 2, 1),\n            (0, 16,\
    \ 3, 4),\n            (0, 8, 0, -7),\n            (4, 12, -2, 5),\n          \
    \  (0, 16, 1, 0),\n            (0, 16, 5, 2),\n        ]:\n            tree.apply(left,\
    \ right, (b, c))\n            for i in range(left, right):\n                values[i]\
    \ = b * values[i] + c\n            for p in [0, 7, 8, 15]:\n                self.assertEqual(tree.get(p),\
    \ (values[p], 1))\n        tree.set(3, (10**100, 1))\n        values[3] = 10**100\n\
    \        tree.apply(0, 16, (-1, 10**90))\n        values = [-x + 10**90 for x\
    \ in values]\n        for left in range(17):\n            for right in range(left,\
    \ 17):\n                self.assertEqual(\n                    tree.prod(left,\
    \ right),\n                    (sum(values[left:right]), right - left),\n    \
    \            )\n\n    def test_different_arities_and_float_components(self):\n\
    \        rng = random.Random(317)\n        for arity in [2]:\n            n =\
    \ 17\n            values = [\n                tuple(\n                    rng.randrange(-20,\
    \ 21) * (0.5 if j == 1 else 1)\n                    for j in range(arity)\n  \
    \              )\n                for _ in range(n)\n            ]\n         \
    \   zero = tuple(0.0 if j == 1 else 0 for j in range(arity))\n\n            def\
    \ op(x, y):\n                return tuple(a + b for a, b in zip(x, y))\n\n   \
    \         def mp(f, x):\n                return tuple(x[j] + f[j] * x[-1] for\
    \ j in range(arity)) + (x[-1],)\n\n            tree = TupleLazySegtree(\n    \
    \            [x + (1,) for x in values], op, zero + (0,), mp, op, zero\n     \
    \       )\n            for _ in range(100):\n                left = rng.randrange(n\
    \ + 1)\n                right = rng.randrange(left, n + 1)\n                tag\
    \ = tuple(\n                    rng.randrange(-5, 6) * (0.5 if j == 1 else 1)\
    \ for j in range(arity)\n                )\n                tree.apply(left, right,\
    \ tag)\n                for i in range(left, right):\n                    values[i]\
    \ = tuple(values[i][j] + tag[j] for j in range(arity))\n                left =\
    \ rng.randrange(n + 1)\n                right = rng.randrange(left, n + 1)\n \
    \               expected = tuple(\n                    sum(x[j] for x in values[left:right])\
    \ for j in range(arity)\n                ) + (right - left,)\n               \
    \ self.assertEqual(tree.prod(left, right), expected)\n\n    def test_noncommutative_products_and_searches(self):\n\
    \        values = list(\"abcdefghi\")\n\n        def op(x, y):\n            return\
    \ x[0] + y[0], x[1] + y[1]\n\n        def mp(f, x):\n            return x if f[0]\
    \ is None else (f[0] * x[1], x[1])\n\n        tree = TupleLazySegtree(\n     \
    \       [(x, 1) for x in values],\n            op,\n            (\"\", 0),\n \
    \           mp,\n            lambda f, g: g if f[0] is None else f,\n        \
    \    (None, 0),\n        )\n        for left, right, letter in [(0, 7, \"x\"),\
    \ (2, 5, \"y\"), (7, 9, \"z\")]:\n            tree.apply(left, right, (letter,\
    \ 0))\n            values[left:right] = [letter] * (right - left)\n        for\
    \ left in range(10):\n            for right in range(left, 10):\n            \
    \    text = \"\".join(values[left:right])\n                self.assertEqual(tree.prod(left,\
    \ right), (text, right - left))\n                self.assertEqual(\n         \
    \           tree.max_right(left, lambda x: text.startswith(x[0])), right\n   \
    \             )\n                self.assertEqual(\n                    tree.min_left(right,\
    \ lambda x: text.endswith(x[0])), left\n                )\n\n    def test_sum_searches_with_pending_tags(self):\n\
    \        rng = random.Random(184)\n        for n in [0, 1, 2, 7, 8, 9, 31, 32,\
    \ 33]:\n            values = [rng.randrange(10) for _ in range(n)]\n         \
    \   tree = affine_tree(values)\n            for _ in range(10):\n            \
    \    left = rng.randrange(n + 1)\n                right = rng.randrange(left,\
    \ n + 1)\n                b, c = rng.randrange(3), rng.randrange(4)\n        \
    \        tree.apply(left, right, (b, c))\n                for i in range(left,\
    \ right):\n                    values[i] = b * values[i] + c\n               \
    \ limit = rng.randrange(sum(values) + 2)\n                for left in range(n\
    \ + 1):\n                    right = left\n                    while right < n\
    \ and sum(values[left : right + 1]) <= limit:\n                        right +=\
    \ 1\n                    self.assertEqual(\n                        tree.max_right(left,\
    \ lambda x: x[0] <= limit), right\n                    )\n                for\
    \ right in range(n + 1):\n                    left = right\n                 \
    \   while left and sum(values[left - 1 : right]) <= limit:\n                 \
    \       left -= 1\n                    self.assertEqual(\n                   \
    \     tree.min_left(right, lambda x: x[0] <= limit), left\n                  \
    \  )\n\n    def test_three_component_values_and_tags(self):\n        rng = random.Random(47)\n\
    \        values = [(rng.randrange(-10, 11), rng.randrange(-10, 11)) for _ in range(17)]\n\
    \n        def op(x, y):\n            return x[0] + y[0], x[1] + y[1], x[2] + y[2]\n\
    \n        def mp(f, x):\n            b, c, d = f\n            return b * x[0]\
    \ + c * x[2], b * x[1] + d * x[2], x[2]\n\n        def comp(f, g):\n         \
    \   return f[0] * g[0], f[0] * g[1] + f[1], f[0] * g[2] + f[2]\n\n        tree\
    \ = TupleLazySegtree(\n            [(a, b, 1) for a, b in values],\n         \
    \   op,\n            (0, 0, 0),\n            mp,\n            comp,\n        \
    \    (1, 0, 0),\n        )\n        for _ in range(100):\n            left = rng.randrange(18)\n\
    \            right = rng.randrange(left, 18)\n            b, c, d = (rng.randrange(-3,\
    \ 4) for _ in range(3))\n            tree.apply(left, right, (b, c, d))\n    \
    \        for i in range(left, right):\n                a, aa = values[i]\n   \
    \             values[i] = b * a + c, b * aa + d\n            left = rng.randrange(18)\n\
    \            right = rng.randrange(left, 18)\n            self.assertEqual(\n\
    \                tree.prod(left, right),\n                (\n                \
    \    sum(x[0] for x in values[left:right]),\n                    sum(x[1] for\
    \ x in values[left:right]),\n                    right - left,\n             \
    \   ),\n            )\n\n    def test_identity_action(self):\n        tree = TupleLazySegtree(\n\
    \            [(3, 1), (-2, 1), (5, 1)],\n            lambda x, y: (x[0] + y[0],\
    \ x[1] + y[1]),\n            (0, 0),\n            lambda f, x: x,\n          \
    \  lambda f, g: (0, 0),\n            (0, 0),\n        )\n        tree.apply(0,\
    \ 3, (0, 0))\n        tree.apply_point(1, (0, 0))\n        tree.set(0, (7, 1))\n\
    \        self.assertEqual(tree.get(0), (7, 1))\n        self.assertEqual(tree.prod(0,\
    \ 3), (10, 3))\n\n    def test_unregistered_arities(self):\n        for e, identity\
    \ in [\n            ((), (0, 0)),\n            ((0,), (0, 0)),\n            ((0,)\
    \ * 4, (0, 0)),\n            ((0, 0), ()),\n            ((0, 0), (0,)),\n    \
    \        ((0, 0), (0,) * 4),\n        ]:\n            with self.subTest(e=e, identity=identity):\n\
    \                with self.assertRaises(AssertionError):\n                   \
    \ TupleLazySegtree(\n                        [], lambda x, y: x, e, lambda f,\
    \ x: x, lambda f, g: f, identity\n                    )\n\n\nif __name__ == \"\
    __main__\":\n    unittest.main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/test_tuple_lazy_segtree.py
  requiredBy: []
  timestamp: '2026-10-25 10:09:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/test_tuple_lazy_segtree.py
layout: document
redirect_from:
- /library/tests/data_structure/test_tuple_lazy_segtree.py
- /library/tests/data_structure/test_tuple_lazy_segtree.py.html
title: tests/data_structure/test_tuple_lazy_segtree.py
---
