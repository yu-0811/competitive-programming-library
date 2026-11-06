# problem: https://judge.yosupo.jp/problem/deque
# include: algorithm_library/python/data_structure/BucketList.py


def main():
    Q = int(readline())
    a = BucketList()
    ans = []
    for _ in range(Q):
        query = list(map(int, readline().split()))
        t = query[0]
        if t == 0:
            a.insert(0, query[1])
        elif t == 1:
            a.append(query[1])
        elif t == 2:
            a.pop(0)
        elif t == 3:
            a.pop()
        else:
            ans.append(str(a[query[1]]))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
