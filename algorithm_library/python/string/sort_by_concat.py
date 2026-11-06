from algorithm_library.python.string.Z_algo import z_algo
from algorithm_library.python.techniques.CmpSort import cmp_sort


# reference: https://info.atcoder.jp/entry/algorithm_lectures/lex_min_string_concatenation
def sort_by_concat(T: list[str]) -> list[str]:
    """
    文字列配列 T = [S_1, S_2, ...] の並べ替えであり、文字列を結合 S_1 + S_2 + ... したとき辞書順最小になる順番に並べ替えて返す
    S_i+S_j を基準にソートすればいい
    T の辞書順ソートではない
    """

    # Z-array は比較で必要になったときに一度だけ構築する
    Z = [None] * len(T)

    # a, b の辞書順を返す
    def lexcmp(a: str, b: str) -> int:
        return (a > b) - (a < b)

    def cmp(x: int, y: int) -> int:
        """
        a+b < b+a なら -1, a+b == b+a なら 0, a+b > b+a なら 1
        """
        a, b = T[x], T[y]
        isrev = len(a) > len(b)
        if isrev:
            a, b = b, a
            x, y = y, x
        n, m = len(a), len(b)

        # 1. a と b[:n]
        f = lexcmp(a, b[:n])

        # 2, b[:m-n] と b[n:m]
        if f == 0 and n < m:
            zb = Z[y]
            if zb is None:
                Z[y] = zb = z_algo(b)
            k = m - n
            lcp = min(zb[n], k)
            # b[:m-n] != b[n:m] なら lcp の直後の文字で辞書順決まる
            if lcp < k:
                f = lexcmp(b[lcp], b[n + lcp])

        # 3. b[m-n:] と a
        if f == 0:
            f = lexcmp(b[m - n :], a)

        return -f if isrev else f

    return [T[i] for i in cmp_sort(list(range(len(T))), cmp)]
