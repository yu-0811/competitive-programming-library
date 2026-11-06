# problem: https://judge.yosupo.jp/problem/ordered_set
# include: algorithm_library/python/data_structure/SortedMultiset.py


def main():
    N, Q = map(int, readline().split())
    s = SortedMultiset(map(int, readline().split()))
    ans = []
    for _ in range(Q):
        t, x = map(int, readline().split())
        if t == 0:
            if x not in s:
                s.add(x)
        elif t == 1:
            s.discard(x)
        elif t == 2:
            ans.append(str(s[x - 1] if x <= len(s) else -1))
        elif t == 3:
            ans.append(str(s.index_right(x)))
        elif t == 4:
            y = s.lt(x + 1)
            ans.append(str(y if y is not None else -1))
        else:
            y = s.gt(x - 1)
            ans.append(str(y if y is not None else -1))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
