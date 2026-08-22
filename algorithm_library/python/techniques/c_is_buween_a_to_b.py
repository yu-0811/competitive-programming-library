# https://atcoder.jp/contests/abc367/editorial/10712
def c_is_buween_a_to_b(a, b, c):
    return (a - b) * (b - c) * (c - a) > 0
