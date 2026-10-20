# problem: https://judge.yosupo.jp/problem/number_of_substrings
# include: algorithm_library/python/string/SuffixArray.py


def main():
    S = readline().decode().strip()
    sa = suffix_array(S)
    print(len(S) * (len(S) + 1) // 2 - sum(lcp_array(S, sa)))


if __name__ == "__main__":
    main()
