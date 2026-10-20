"""Exercise generated standalone submissions against small independent oracles."""

from collections import Counter, deque
from fractions import Fraction
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "library-checker-submitcode"
MOD = 998244353


def encode(*rows):
    return "\n".join(" ".join(map(str, row)) for row in rows) + "\n"


def path_in_graph(graph, start, goal):
    parents = {start: None}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == goal:
            path = []
            while v is not None:
                path.append(v)
                v = parents[v]
            return path[::-1]
        for u in graph[v]:
            if u not in parents:
                parents[u] = v
                queue.append(u)
    return []


def naive_product(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) % MOD for j in range(len(b[0]))]
        for i in range(len(a))
    ]


class SubmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = tempfile.TemporaryDirectory(prefix="library-checker-test-")
        cls.addClassCleanup(cls.directory.cleanup)
        subprocess.run(
            [sys.executable, str(BASE / "generate.py"), "--check"],
            cwd=cls.directory.name,
            check=True,
            capture_output=True,
            text=True,
        )

    def run_submission(self, name, data):
        result = subprocess.run(
            [sys.executable, "-I", str(BASE / name)],
            input=data,
            cwd=self.directory.name,
            text=True,
            capture_output=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, f"{name}: {result.stderr}\n{data}")
        self.assertEqual(result.stderr, "", name)
        return result.stdout

    def check_numbers(self, name, data, expected):
        with self.subTest(submission=name):
            actual = self.run_submission(name, data)
            self.assertEqual(list(map(int, actual.split())), expected)

    def test_unionfind(self):
        rng = random.Random(101)
        graph = [set() for _ in range(12)]
        queries, expected = [], []
        for _ in range(100):
            t, u, v = rng.randrange(2), rng.randrange(12), rng.randrange(12)
            queries.append((t, u, v))
            if t == 0:
                graph[u].add(v)
                graph[v].add(u)
            else:
                expected.append(int(bool(path_in_graph(graph, u, v))))
        self.check_numbers(
            "graph/unionfind.py", encode((12, len(queries)), *queries), expected
        )

    def test_potential_unionfind_modulo_and_rejected_constraints(self):
        rng = random.Random(102)
        graph = [[] for _ in range(9)]

        def difference(start, goal):
            values = {start: 0}
            queue = deque([start])
            while queue:
                v = queue.popleft()
                if v == goal:
                    return values[v]
                for u, weight in graph[v]:
                    if u not in values:
                        values[u] = (values[v] + weight) % MOD
                        queue.append(u)
            return None

        queries = [
            (1, 0, 1),
            (0, 0, 1, MOD - 1),
            (0, 1, 2, 2),
            (0, 0, 2, 1),
            (0, 0, 2, 2),
            (1, 0, 2),
            (0, 3, 3, 1),
            (1, 3, 3),
        ]
        for _ in range(150):
            u, v = rng.randrange(9), rng.randrange(9)
            if rng.randrange(2):
                queries.append((1, u, v))
            else:
                queries.append(
                    (0, u, v, rng.choice([0, 1, MOD - 1, rng.randrange(MOD)]))
                )
        expected = []
        for t, u, v, *rest in queries:
            value = difference(v, u)
            if t == 1:
                expected.append(-1 if value is None else value)
            else:
                x = rest[0]
                valid = value is None or value == x
                expected.append(int(valid))
                if valid:
                    graph[v].append((u, x))
                    graph[u].append((v, -x))
        self.check_numbers(
            "graph/unionfind_with_potential.py",
            encode((9, len(queries)), *queries),
            expected,
        )

    def test_scc_partition_and_topological_order(self):
        rng = random.Random(103)
        for n in [1, 2, 9, 18]:
            edges = [
                (u, v) for u in range(n) for v in range(n) if rng.randrange(5) == 0
            ]
            edges += [(0, 0), (0, 0)]
            reachable = [[u == v for v in range(n)] for u in range(n)]
            for u, v in edges:
                reachable[u][v] = True
            for k in range(n):
                for u in range(n):
                    for v in range(n):
                        reachable[u][v] |= reachable[u][k] and reachable[k][v]
            lines = self.run_submission(
                "graph/scc.py", encode((n, len(edges)), *edges)
            ).splitlines()
            self.assertEqual(int(lines[0]), len(lines) - 1)
            components = [-1] * n
            for i, line in enumerate(lines[1:]):
                size, *vertices = map(int, line.split())
                self.assertEqual(size, len(vertices))
                self.assertGreater(size, 0)
                for v in vertices:
                    self.assertTrue(0 <= v < n)
                    self.assertEqual(components[v], -1)
                    components[v] = i
            self.assertNotIn(-1, components)
            for u in range(n):
                for v in range(n):
                    self.assertEqual(
                        components[u] == components[v],
                        reachable[u][v] and reachable[v][u],
                    )
            for u, v in edges:
                self.assertLessEqual(components[u], components[v])

    def test_lca_both_implementations(self):
        rng = random.Random(104)
        for n in [1, 2, 17, 65]:
            for chain in [False, True]:
                parents = [0] + [
                    v - 1 if chain else rng.randrange(v) for v in range(1, n)
                ]
                queries = [(rng.randrange(n), rng.randrange(n)) for _ in range(80)]
                expected = []
                for u, v in queries:
                    ancestors = {u}
                    while u:
                        u = parents[u]
                        ancestors.add(u)
                    while v not in ancestors:
                        v = parents[v]
                    expected.append(v)
                data = encode((n, len(queries)), parents[1:], *queries)
                for name in ["lca.py", "lca_euler_tour.py"]:
                    self.check_numbers(f"graph/{name}", data, expected)

    def test_jump_on_tree(self):
        rng = random.Random(105)
        for n in [1, 3, 17, 33]:
            labels = list(range(n))
            rng.shuffle(labels)
            edges = [(labels[v], labels[rng.randrange(v)]) for v in range(1, n)]
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            queries, expected = [], []
            for _ in range(100):
                u, v, k = rng.randrange(n), rng.randrange(n), rng.randrange(n + 1)
                path = path_in_graph(graph, u, v)
                queries.append((u, v, k))
                expected.append(path[k] if k < len(path) else -1)
            self.check_numbers(
                "graph/jump_on_tree.py",
                encode((n, len(queries)), *edges, *queries),
                expected,
            )

    def test_bipartite_matching_size_and_witness(self):
        rng = random.Random(106)
        for left, right in [(1, 1), (2, 3), (4, 2), (6, 6)]:
            for _ in range(4):
                edges = {
                    (u, v)
                    for u in range(left)
                    for v in range(right)
                    if rng.randrange(3) == 0
                }
                masks = {0}
                for u in range(left):
                    masks |= {
                        mask | (1 << v)
                        for mask in masks
                        for v in range(right)
                        if (u, v) in edges and not (mask >> v & 1)
                    }
                expected = max(mask.bit_count() for mask in masks)
                rows = self.run_submission(
                    "graph/bipartitematching.py",
                    encode((left, right, len(edges)), *sorted(edges)),
                ).splitlines()
                self.assertEqual(int(rows[0]), expected)
                pairs = [tuple(map(int, row.split())) for row in rows[1:]]
                self.assertEqual(len(pairs), expected)
                self.assertEqual(len({u for u, v in pairs}), expected)
                self.assertEqual(len({v for u, v in pairs}), expected)
                self.assertTrue(set(pairs) <= edges)

    def test_point_add_range_sum(self):
        rng = random.Random(107)
        for n in [1, 2, 7, 17]:
            initial = [rng.randrange(10**9) for _ in range(n)]
            values = initial[:]
            queries, expected = [], []
            for _ in range(100):
                if rng.randrange(2):
                    p, x = rng.randrange(n), rng.randrange(10**9)
                    queries.append((0, p, x))
                    values[p] += x
                else:
                    l = rng.randrange(n + 1)
                    r = rng.randrange(l, n + 1)
                    queries.append((1, l, r))
                    expected.append(sum(values[l:r]))
            data = encode((n, len(queries)), initial, *queries)
            for implementation in ["bit", "segtree"]:
                self.check_numbers(
                    f"data_structure/point_add_range_sum_{implementation}.py",
                    data,
                    expected,
                )

    def test_static_range_structures(self):
        rng = random.Random(108)
        for n in [1, 2, 7, 8, 17]:
            values = [rng.randrange(8) for _ in range(n)]
            ranges = []
            for _ in range(60):
                l = rng.randrange(n)
                ranges.append((l, rng.randrange(l + 1, n + 1)))
            data = encode((n, len(ranges)), values, *ranges)
            self.check_numbers(
                "data_structure/staticrmq.py",
                data,
                [min(values[l:r]) for l, r in ranges],
            )
            self.check_numbers(
                "data_structure/static_range_sum.py",
                data,
                [sum(values[l:r]) for l, r in ranges],
            )
            queries = [(l, r, rng.randrange(9)) for l, r in ranges] + [
                (0, 0, values[0])
            ]
            self.check_numbers(
                "data_structure/static_range_frequency.py",
                encode((n, len(queries)), values, *queries),
                [values[l:r].count(x) for l, r, x in queries],
            )

    def test_cartesian_tree(self):
        rng = random.Random(109)
        for n in [1, 2, 7, 17]:
            values = list(range(n))
            rng.shuffle(values)
            expected = [-1] * n

            def build(l, r, parent=None):
                if l == r:
                    return
                v = min(range(l, r), key=values.__getitem__)
                expected[v] = v if parent is None else parent
                build(l, v, v)
                build(v + 1, r, v)

            build(0, n)
            self.check_numbers(
                "data_structure/cartesian_tree.py", encode((n,), values), expected
            )

    def test_point_set_range_composite_order(self):
        rng = random.Random(110)
        for n in [1, 3, 9]:
            initial = [(rng.randrange(1, MOD), rng.randrange(MOD)) for _ in range(n)]
            values = initial[:]
            queries, expected = [], []
            for _ in range(100):
                if rng.randrange(3) == 0:
                    p, a, b = (
                        rng.randrange(n),
                        rng.randrange(1, MOD),
                        rng.randrange(MOD),
                    )
                    queries.append((0, p, a, b))
                    values[p] = (a, b)
                else:
                    l = rng.randrange(n)
                    r, x = rng.randrange(l + 1, n + 1), rng.randrange(MOD)
                    queries.append((1, l, r, x))
                    for a, b in values[l:r]:
                        x = (a * x + b) % MOD
                    expected.append(x)
            self.check_numbers(
                "data_structure/point_set_range_composite.py",
                encode((n, len(queries)), *initial, *queries),
                expected,
            )

    def test_range_affine_range_sum_both_implementations(self):
        rng = random.Random(111)
        for n in [1, 2, 3, 7, 8, 9, 17]:
            initial = [rng.randrange(MOD) for _ in range(n)]
            values = initial[:]
            queries, expected = [], []
            for _ in range(120):
                l = rng.randrange(n)
                r = rng.randrange(l + 1, n + 1)
                if rng.randrange(3):
                    a, b = (
                        rng.choice([0, 1, MOD - 1, rng.randrange(MOD)]),
                        rng.randrange(MOD),
                    )
                    queries.append((0, l, r, a, b))
                    for i in range(l, r):
                        values[i] = (a * values[i] + b) % MOD
                else:
                    queries.append((1, l, r))
                    expected.append(sum(values[l:r]) % MOD)
            data = encode((n, len(queries)), initial, *queries)
            for suffix in ["", "_tuple"]:
                self.check_numbers(
                    f"data_structure/range_affine_range_sum{suffix}.py", data, expected
                )

    def test_suffix_array_substrings_and_z_algorithm(self):
        rng = random.Random(112)
        strings = ["a", "aaaaaa", "banana", "abacaba", "abcabcabc"]
        strings += [
            "".join(rng.choice("abcd") for _ in range(n)) for n in [2, 17, 63, 120]
        ]
        for s in strings:
            self.check_numbers(
                "string/suffixarray.py",
                s + "\n",
                sorted(range(len(s)), key=lambda i: s[i:]),
            )
            distinct = {s[l:r] for l in range(len(s)) for r in range(l + 1, len(s) + 1)}
            self.check_numbers(
                "string/number_of_substrings.py", s + "\n", [len(distinct)]
            )
            z = []
            for i in range(len(s)):
                length = 0
                while i + length < len(s) and s[length] == s[i + length]:
                    length += 1
                z.append(length)
            self.check_numbers("string/zalgorithm.py", s + "\n", z)

    def test_longest_common_substring_witness(self):
        rng = random.Random(113)
        pairs = [("a", "b"), ("a", "a"), ("banana", "ananas"), ("aaaa", "aa")]
        pairs += [
            (
                "".join(rng.choice("abc") for _ in range(25)),
                "".join(rng.choice("abc") for _ in range(30)),
            )
            for _ in range(6)
        ]
        for s, t in pairs:
            best = max(
                (
                    r - l
                    for l in range(len(s))
                    for r in range(l + 1, len(s) + 1)
                    if s[l:r] in t
                ),
                default=0,
            )
            a, b, c, d = map(
                int,
                self.run_submission(
                    "string/longest_common_substring.py", f"{s}\n{t}\n"
                ).split(),
            )
            self.assertTrue(0 <= a <= b <= len(s))
            self.assertTrue(0 <= c <= d <= len(t))
            self.assertEqual(s[a:b], t[c:d])
            self.assertEqual(b - a, best)

    def test_convolution_including_ntt_branch(self):
        rng = random.Random(114)
        for n, m in [(1, 1), (2, 4), (40, 41), (41, 41), (63, 65), (128, 97)]:
            a = [rng.choice([0, MOD - 1, rng.randrange(MOD)]) for _ in range(n)]
            b = [rng.choice([0, MOD - 1, rng.randrange(MOD)]) for _ in range(m)]
            expected = [0] * (n + m - 1)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    expected[i + j] = (expected[i + j] + x * y) % MOD
            self.check_numbers(
                "math/convolution_mod.py", encode((n, m), a, b), expected
            )

    def test_matrix_product_and_power(self):
        rng = random.Random(115)
        for n, m, k in [(1, 1, 1), (2, 3, 4), (4, 9, 2)]:
            a = [[rng.randrange(MOD) for _ in range(m)] for _ in range(n)]
            b = [[rng.randrange(MOD) for _ in range(k)] for _ in range(m)]
            expected = naive_product(a, b)
            self.check_numbers(
                "math/matrix_product.py",
                encode((n, m, k), *a, *b),
                [x for row in expected for x in row],
            )
        for n in [1, 2, 4]:
            a = [[rng.randrange(MOD) for _ in range(n)] for _ in range(n)]
            for k in [0, 1, 2, 5, 13]:
                expected = [[int(i == j) for j in range(n)] for i in range(n)]
                for _ in range(k):
                    expected = naive_product(expected, a)
                self.check_numbers(
                    "math/pow_of_matrix.py",
                    encode((n, k), *a),
                    [x for row in expected for x in row],
                )
        self.check_numbers(
            "math/pow_of_matrix.py",
            encode((2, 10**18), (2, 0), (0, 3)),
            [pow(2, 10**18, MOD), 0, 0, pow(3, 10**18, MOD)],
        )

    def test_sort_points_by_argument_axes_origin_and_precision(self):
        rng = random.Random(116)
        points = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
        points += [(10**9, 10**9 - 1), (10**9 - 1, 10**9 - 2)]
        points += [(rng.randrange(-10, 11), rng.randrange(-10, 11)) for _ in range(100)]
        rng.shuffle(points)

        def angle_key(point):
            x, y = point
            if y < 0:
                return (0, Fraction(y, x)) if x < 0 else (1, Fraction(x, -y))
            if x > 0:
                return 2, Fraction(y, x)
            if x == y == 0:
                return 2, Fraction(0)
            if y > 0:
                return 3, Fraction(-x, y)
            return 4, Fraction(0)

        rows = self.run_submission(
            "math/sort_points_by_argument.py", encode((len(points),), *points)
        ).splitlines()
        actual = [tuple(map(int, row.split())) for row in rows]
        self.assertEqual(Counter(actual), Counter(points))
        self.assertEqual(list(map(angle_key, actual)), sorted(map(angle_key, points)))


if __name__ == "__main__":
    unittest.main()
