# problem: https://judge.yosupo.jp/problem/suffixarray
# include: algorithm_library/python/string/SuffixArray.py


def main():
    S = readline().decode().strip()
    print(*suffix_array(S))


if __name__ == "__main__":
    main()
