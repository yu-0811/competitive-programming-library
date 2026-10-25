---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/math/AngularSort.py
    title: algorithm_library/python/math/AngularSort.py
  - icon: ':warning:'
    path: algorithm_library/python/techniques/CmpSort.py
    title: algorithm_library/python/techniques/CmpSort.py
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
  code: "import itertools\nimport random\nimport unittest\nfrom functools import cmp_to_key\n\
    \nfrom algorithm_library.python.math.AngularSort import compare\nfrom algorithm_library.python.techniques.CmpSort\
    \ import cmp_sort\n\n\ndef integer_compare(a, b):\n    return a - b\n\n\nclass\
    \ CmpSortTests(unittest.TestCase):\n    def check_sort(self, values, cmp):\n \
    \       expected = sorted(values, key=cmp_to_key(cmp))\n        actual = values[:]\n\
    \        self.assertIs(cmp_sort(actual, cmp), actual)\n        self.assertEqual(actual,\
    \ expected)\n\n    def test_exhaustive_short_lists(self):\n        for n in range(8):\n\
    \            for values in itertools.product(range(3), repeat=n):\n          \
    \      self.check_sort(list(values), integer_compare)\n\n    def test_run_boundaries_and_input_orders(self):\n\
    \        rng = random.Random(42)\n        for n in [0, 1, 2, 15, 16, 17, 31, 32,\
    \ 33, 63, 64, 65, 127, 257, 4097]:\n            for values in [\n            \
    \    list(range(n)),\n                list(range(n - 1, -1, -1)),\n          \
    \      [7] * n,\n                [rng.randrange(-10, 11) for _ in range(n)],\n\
    \                list(range(0, n, 2)) + list(range(1, n, 2)),\n              \
    \  [i % 17 for i in range(n)],\n            ]:\n                self.check_sort(values,\
    \ integer_compare)\n                self.check_sort(values, lambda a, b: b - a)\n\
    \n    def test_opaque_items_and_stability(self):\n        rng = random.Random(314)\n\
    \        # \u8F9E\u66F8\u540C\u58EB\u306E\u9806\u5E8F\u6BD4\u8F03\u306F\u3067\u304D\
    \u306A\u3044\u3002\u540C\u9806\u4F4D\u306E\u5143\u306E\u9806\u5E8F\u3082\u691C\
    \u8A3C\u3059\u308B\u3002\n        for keys in [\n            [rng.randrange(10)\
    \ for _ in range(2049)],\n            [i // 3 for i in range(257, -1, -1)],\n\
    \            [0] * 257,\n        ]:\n            values = [{\"key\": key, \"index\"\
    : i} for i, key in enumerate(keys)]\n            self.check_sort(values, lambda\
    \ a, b: a[\"key\"] - b[\"key\"])\n\n    def test_angular_sort_and_collinear_stability(self):\n\
    \        rng = random.Random(2718)\n        values = [(1, 0), (1, 1), (0, 1),\
    \ (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]\n        values = [(x * k, y *\
    \ k) for k in range(1, 41) for x, y in values]\n        rng.shuffle(values)\n\
    \        self.check_sort(values, compare)\n        for limit in [10**9, 10**30]:\n\
    \            values = [\n                (rng.randrange(-limit, limit + 1), rng.randrange(-limit,\
    \ limit + 1))\n                for _ in range(2049)\n            ]\n         \
    \   self.check_sort([p for p in values if p != (0, 0)], compare)\n\n    def test_sorted_and_strictly_reversed_use_linear_comparisons(self):\n\
    \        for values in [list(range(10000)), list(range(9999, -1, -1)), [1] * 10000]:\n\
    \            calls = 0\n\n            def counted(a, b):\n                nonlocal\
    \ calls\n                calls += 1\n                return a - b\n\n        \
    \    actual = values[:]\n            cmp_sort(actual, counted)\n            self.assertEqual(actual,\
    \ sorted(values))\n            self.assertEqual(calls, len(values) - 1)\n\n\n\
    if __name__ == \"__main__\":\n    unittest.main()\n"
  dependsOn:
  - algorithm_library/python/math/AngularSort.py
  - algorithm_library/python/techniques/CmpSort.py
  isVerificationFile: false
  path: tests/math/test_cmp_sort.py
  requiredBy: []
  timestamp: '2026-10-25 21:47:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/math/test_cmp_sort.py
layout: document
redirect_from:
- /library/tests/math/test_cmp_sort.py
- /library/tests/math/test_cmp_sort.py.html
title: tests/math/test_cmp_sort.py
---
