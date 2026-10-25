---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/math/MatrixPower.py
    title: algorithm_library/python/math/MatrixPower.py
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
  code: "import random\nimport unittest\n\nfrom algorithm_library.python.math.MatrixPower\
    \ import mat_mul, mat_pow\n\n\ndef reference_mul(a, b, mod):\n    return [\n \
    \       [sum(row[k] * b[k][j] for k in range(len(b))) % mod for j in range(len(b[0]))]\n\
    \        for row in a\n    ]\n\n\nclass MatrixPowerTests(unittest.TestCase):\n\
    \    def test_rectangular_products_and_block_boundaries(self):\n        rng =\
    \ random.Random(42)\n        for k in [1, 2, 7, 8, 9, 15, 16, 17, 31, 32, 33]:\n\
    \            for mod in [1, 7, 998244353, (1 << 90) + 7]:\n                a =\
    \ [\n                    [rng.randrange(-2 * mod, 2 * mod) for _ in range(k)]\n\
    \                    for _ in range(3)\n                ]\n                b =\
    \ [\n                    [rng.randrange(-2 * mod, 2 * mod) for _ in range(5)]\n\
    \                    for _ in range(k)\n                ]\n                self.assertEqual(mat_mul(a,\
    \ b, mod), reference_mul(a, b, mod))\n\n    def test_powers_against_repeated_multiplication(self):\n\
    \        rng = random.Random(314)\n        for n in [1, 2, 3, 8, 9]:\n       \
    \     for mod in [1, 7, 998244353]:\n                a = [\n                 \
    \   [rng.randrange(-2 * mod, 2 * mod) for _ in range(n)]\n                   \
    \ for _ in range(n)\n                ]\n                expected = [[int(i ==\
    \ j) for j in range(n)] for i in range(n)]\n                for exponent in range(34):\n\
    \                    self.assertEqual(mat_pow(a, exponent, mod), expected)\n \
    \                   expected = reference_mul(a, expected, mod)\n\n    def test_input_and_result_do_not_share_rows(self):\n\
    \        for exponent in [0, 1, 2, 3, 8]:\n            a = [[-1, 12], [5, 9]]\n\
    \            original = [row[:] for row in a]\n            result = mat_pow(a,\
    \ exponent, 7)\n            self.assertEqual(a, original)\n            result[0][0]\
    \ = 100\n            self.assertEqual(a, original)\n\n\nif __name__ == \"__main__\"\
    :\n    unittest.main()\n"
  dependsOn:
  - algorithm_library/python/math/MatrixPower.py
  isVerificationFile: false
  path: tests/math/test_matrix_power.py
  requiredBy: []
  timestamp: '2026-10-25 10:02:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/math/test_matrix_power.py
layout: document
redirect_from:
- /library/tests/math/test_matrix_power.py
- /library/tests/math/test_matrix_power.py.html
title: tests/math/test_matrix_power.py
---
