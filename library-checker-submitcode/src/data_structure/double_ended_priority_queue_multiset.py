# problem: https://judge.yosupo.jp/problem/double_ended_priority_queue
# include: algorithm_library/python/data-structure/SortedMultiset.py


def main():
    N, Q = map(int, readline().split())
    s = SortedMultiset(map(int, readline().split()))
    ans = []
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 0:
            s.add(query[1])
        else:
            ans.append(str(s.pop(0 if query[0] == 1 else -1)))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
