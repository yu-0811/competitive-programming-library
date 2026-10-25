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
  code: "import itertools\nimport random\nimport runpy\nimport unittest\nfrom bisect\
    \ import bisect_left\nfrom pathlib import Path\n\n\nBIT = runpy.run_path(\n  \
    \  str(\n        Path(__file__).resolve().parents[2]\n        / \"algorithm_library/python/data-structure/BIT.py\"\
    \n    )\n)[\"BIT\"]\n\n\nclass BITSumTests(unittest.TestCase):\n    def test_empty_array(self):\n\
    \        bit = BIT(0)\n        self.assertEqual(bit.SUM(0), 0)\n        self.assertEqual(bit.range_sum(1,\
    \ 1), 0)\n\n    def test_random_signed_range_updates(self):\n        rng = random.Random(518)\n\
    \        for n in [1, 2, 3, 7, 8, 9, 31, 32, 33, 63, 64, 65]:\n            bit\
    \ = BIT(n)\n            values = [0] * n\n            for _ in range(80):\n  \
    \              left = rng.randrange(n + 1)\n                right = rng.randrange(left,\
    \ n + 1)\n                delta = rng.randrange(-(10**10), 10**10)\n         \
    \       bit.add(left + 1, right + 1, delta)\n                for i in range(left,\
    \ right):\n                    values[i] += delta\n                prefixes =\
    \ [0, *itertools.accumulate(values)]\n                for i, expected in enumerate(prefixes):\n\
    \                    self.assertEqual(bit.SUM(i), expected)\n                for\
    \ _ in range(5):\n                    left = rng.randrange(n + 1)\n          \
    \          right = rng.randrange(left, n + 1)\n                    self.assertEqual(\n\
    \                        bit.range_sum(left + 1, right + 1),\n               \
    \         prefixes[right] - prefixes[left],\n                    )\n\n\nclass\
    \ BITLowerBoundTests(unittest.TestCase):\n    def check_lower_bounds(self, bit,\
    \ values):\n        prefixes = list(itertools.accumulate(values))\n        for\
    \ target in [-10, 0, *range(1, sum(values) + 2)]:\n            expected = 0 if\
    \ target <= 0 else bisect_left(prefixes, target) + 1\n            self.assertEqual(bit.lower_bound(target),\
    \ expected, (values, target))\n\n    def test_empty_zero_and_sparse_arrays(self):\n\
    \        for values in [[], [0], [0, 0, 0], [3], [0, 3, 0, 0, 2, 0]]:\n      \
    \      with self.subTest(values=values):\n                bit = BIT(len(values))\n\
    \                for i, value in enumerate(values, 1):\n                    bit.add(i,\
    \ i + 1, value)\n                self.check_lower_bounds(bit, values)\n\n    def\
    \ test_range_additions_and_subtractions(self):\n        bit = BIT(8)\n       \
    \ values = [0] * 8\n        for left, right, delta in [(2, 8, 3), (1, 9, 2), (3,\
    \ 6, -4), (1, 9, -1)]:\n            bit.add(left, right, delta)\n            for\
    \ i in range(left - 1, right - 1):\n                values[i] += delta\n     \
    \       self.check_lower_bounds(bit, values)\n\n    def test_random_range_updates_around_powers_of_two(self):\n\
    \        rng = random.Random(20261020)\n        for n in [1, 2, 3, 7, 8, 9, 15,\
    \ 16, 17, 31, 32, 33]:\n            bit = BIT(n)\n            values = [0] * n\n\
    \            for _ in range(40):\n                left = rng.randrange(n)\n  \
    \              right = rng.randrange(left + 1, n + 1)\n                delta =\
    \ rng.randint(-min(values[left:right]), 5)\n                bit.add(left + 1,\
    \ right + 1, delta)\n                for i in range(left, right):\n          \
    \          values[i] += delta\n                self.check_lower_bounds(bit, values)\n\
    \n    def test_large_integer_targets(self):\n        big = 10**30\n        bit\
    \ = BIT(4)\n        bit.add(2, 4, big)\n        cases = [(1, 2), (big, 2), (big\
    \ + 1, 3), (2 * big, 3), (2 * big + 1, 5)]\n        for target, expected in cases:\n\
    \            self.assertEqual(bit.lower_bound(target), expected)\n\n\nif __name__\
    \ == \"__main__\":\n    unittest.main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/test_bit.py
  requiredBy: []
  timestamp: '2026-10-20 12:29:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/test_bit.py
layout: document
redirect_from:
- /library/tests/data_structure/test_bit.py
- /library/tests/data_structure/test_bit.py.html
title: tests/data_structure/test_bit.py
---
