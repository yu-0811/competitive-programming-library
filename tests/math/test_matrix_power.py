import random
import unittest

from algorithm_library.python.math.MatrixPower import mat_mul, mat_pow


def reference_mul(a, b, mod):
    return [
        [sum(row[k] * b[k][j] for k in range(len(b))) % mod for j in range(len(b[0]))]
        for row in a
    ]


class MatrixPowerTests(unittest.TestCase):
    def test_rectangular_products_and_block_boundaries(self):
        rng = random.Random(42)
        for k in [1, 2, 7, 8, 9, 15, 16, 17, 31, 32, 33]:
            for mod in [1, 7, 998244353, (1 << 90) + 7]:
                a = [
                    [rng.randrange(-2 * mod, 2 * mod) for _ in range(k)]
                    for _ in range(3)
                ]
                b = [
                    [rng.randrange(-2 * mod, 2 * mod) for _ in range(5)]
                    for _ in range(k)
                ]
                self.assertEqual(mat_mul(a, b, mod), reference_mul(a, b, mod))

    def test_powers_against_repeated_multiplication(self):
        rng = random.Random(314)
        for n in [1, 2, 3, 8, 9]:
            for mod in [1, 7, 998244353]:
                a = [
                    [rng.randrange(-2 * mod, 2 * mod) for _ in range(n)]
                    for _ in range(n)
                ]
                expected = [[int(i == j) for j in range(n)] for i in range(n)]
                for exponent in range(34):
                    self.assertEqual(mat_pow(a, exponent, mod), expected)
                    expected = reference_mul(a, expected, mod)

    def test_input_and_result_do_not_share_rows(self):
        for exponent in [0, 1, 2, 3, 8]:
            a = [[-1, 12], [5, 9]]
            original = [row[:] for row in a]
            result = mat_pow(a, exponent, 7)
            self.assertEqual(a, original)
            result[0][0] = 100
            self.assertEqual(a, original)


if __name__ == "__main__":
    unittest.main()
