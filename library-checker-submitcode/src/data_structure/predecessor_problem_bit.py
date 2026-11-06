# problem: https://judge.yosupo.jp/problem/predecessor_problem
# include: algorithm_library/python/data_structure/BIT.py


def main():
    N, Q = map(int, readline().split())
    T = bytearray(readline().strip())
    bit = BIT(N)
    l = 0
    for r in range(N + 1):
        if r == N or T[r] == 48:
            if l < r:
                bit.add(l, r, 1)
            l = r + 1
    ans = []
    for _ in range(Q):
        t, k = map(int, readline().split())
        if t < 2:
            value = 1 - t
            if T[k] - 48 != value:
                bit.add(k, k + 1, 2 * value - 1)
                T[k] = 48 + value
        elif t == 2:
            ans.append(str(T[k] - 48))
        elif t == 3:
            x = bit.lower_bound(bit.SUM(k) + 1)
            ans.append(str(x if x < N else -1))
        else:
            w = bit.SUM(k + 1)
            ans.append(str(bit.lower_bound(w) if w else -1))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
