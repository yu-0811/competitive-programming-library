# problem: https://judge.yosupo.jp/problem/cartesian_tree
# include: algorithm_library/python/data-structure/CartesianTree.py


def main():
    _N = int(readline())
    tree = CartesianTree(list(map(int, readline().split())))
    parents = tree.parent
    parents[tree.root] = tree.root
    print(*parents)


if __name__ == "__main__":
    main()
