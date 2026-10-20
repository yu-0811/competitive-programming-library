# O(|S|)
# Z[i] := S[0:|S|) と S[i:|S|) の最長共通接頭辞の長さ
def z_algo(S):
    n = len(S)
    Z = [0] * n
    Z[0] = n
    i, j = 1, 0
    while i < n:
        # 一致する限り延長する
        while i + j < n and S[j] == S[i + j]:
            j += 1
        Z[i] = j

        # 一文字も一致しないならコピーできないので次に進む
        if j == 0:
            i += 1
            continue

        k = 1
        # k+Z[k]>j なら1回目の登場の際にはみ出してしまっている
        # k+Z[k]=j なら2回目の登場の際にはみ出す可能性がある
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        # まだ未確定なところまで i を進める
        i += k
        # j を i に合わせる
        j -= k

    return Z


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

    def merge_sort(arr: list[int]):
        # arr の要素は T のインデックス
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if cmp(left[i], right[j]) <= 0:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])
        return res

    return [T[i] for i in merge_sort(list(range(len(T))))]
