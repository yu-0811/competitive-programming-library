# problem: https://judge.yosupo.jp/problem/sort_points_by_argument
# include: algorithm_library/python/math/AngularSort.py
# include: algorithm_library/python/techniques/CmpSort.py


def main():
    N = int(readline())
    lower, zeros, upper = [], [], []
    for _ in range(N):
        point = tuple(map(int, readline().split()))
        if point == (0, 0):
            zeros.append(point)
        elif point[1] < 0:
            lower.append(point)
        else:
            upper.append(point)
    # The library starts at angle 0; the problem uses (-pi, pi], with arg(0)=0.
    cmp_sort(lower, compare)
    cmp_sort(upper, compare)
    points = lower + zeros + upper
    sys.stdout.write("\n".join(f"{x} {y}" for x, y in points) + "\n")


if __name__ == "__main__":
    main()
