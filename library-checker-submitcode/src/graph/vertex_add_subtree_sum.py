# problem: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
# include: algorithm_library/python/graph/VertexAddSubtreeSum.py


def main():
    n, q = map(int, readline().split())
    # 値とクエリは非負整数なので、split で小さな bytes を大量に作らず読む。
    data = sys.stdin.buffer.read()
    i = 0
    values = [0] * n
    for v in range(n):
        x = 0
        c = data[i]
        while c >= 48:
            x = x * 10 + c - 48
            i += 1
            c = data[i]
        i += 1
        values[v] = x
    parents = [-1] * n
    for v in range(1, n):
        x = 0
        c = data[i]
        while c >= 48:
            x = x * 10 + c - 48
            i += 1
            c = data[i]
        i += 1
        parents[v] = x
    if n == 1:
        i += 1  # N = 1 のときの空の親配列の行
    tree = VertexAddSubtreeSum(parents, values)
    add = tree.add
    subtree_sum = tree.subtree_sum
    ans = []
    for _ in range(q):
        t = data[i]
        i += 2
        v = 0
        c = data[i]
        while c >= 48:
            v = v * 10 + c - 48
            i += 1
            c = data[i]
        i += 1
        if t == 48:
            x = 0
            c = data[i]
            while c >= 48:
                x = x * 10 + c - 48
                i += 1
                c = data[i]
            i += 1
            add(v, x)
        else:
            ans.append(subtree_sum(v))
    # 回答は整数のまま持ち、文字列化の一時領域を小さく保つ。
    for i in range(0, len(ans), 8192):
        sys.stdout.write("\n".join(map(str, ans[i:i + 8192])) + "\n")


if __name__ == "__main__":
    main()
