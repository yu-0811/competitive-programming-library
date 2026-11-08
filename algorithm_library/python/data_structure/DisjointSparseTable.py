class DisjointSparseTable:
    def __init__(s, arr, op):
        """
        arr: 配列
        op: 演算 (結合律を満たすこと)
        """
        s.n = n = len(arr)
        s.arr = arr[:]
        s.op = op

        s.max_k = n.bit_length()
        s.table = [[0] * n for _ in range(s.max_k)]

        for k in range(s.max_k):
            half = 1 << k
            row = s.table[k]
            for start in range(0, n, 2 * half):
                mid = min(start + half, n)
                end = min(start + 2 * half, n)
                # 左半分の接尾辞と右半分の接頭辞を、順序を保って累積する。
                cur = row[mid - 1] = arr[mid - 1]
                for i in range(mid - 2, start - 1, -1):
                    cur = op(arr[i], cur)
                    row[i] = cur
                if mid < end:
                    cur = row[mid] = arr[mid]
                    for i in range(mid + 1, end):
                        cur = op(cur, arr[i])
                        row[i] = cur

    def query(s, l, r):
        assert 0 <= l < r <= s.n
        if r - l == 1:
            return s.arr[l]

        # クエリに答えるために使うレベル k を求める
        k = (l ^ (r - 1)).bit_length() - 1
        row = s.table[k]
        return s.op(row[l], row[r - 1])
