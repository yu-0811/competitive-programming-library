# problem: https://judge.yosupo.jp/problem/longest_common_substring
# include: algorithm_library/python/string/SuffixArray.py


def main():
    S = readline().decode().strip()
    T = readline().decode().strip()
    split = len(S)
    text = S + "$" + T
    sa = suffix_array(text)
    lcp = lcp_array(text, sa)
    best = a = c = 0
    for i, length in enumerate(lcp):
        u, v = sa[i], sa[i + 1]
        if u > v:
            u, v = v, u
        if u < split < v and length > best:
            best, a, c = length, u, v - split - 1
    print(a, a + best, c, c + best)


if __name__ == "__main__":
    main()
