# problem: https://judge.yosupo.jp/problem/assignment
# include: algorithm_library/python/graph/hungarian.py


def main():
    n = int(readline())
    a = [list(map(int, readline().split())) for _ in range(n)]
    cost, p = hungarian(a)
    print(cost)
    print(*p)


if __name__ == "__main__":
    main()
