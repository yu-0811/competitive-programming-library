"""
PackedTupleHeap(arity=2, bits=20, values=None): 整数タプルの辞書順最小ヒープ。
arity: タプルの長さ
values: list[tuple[int, ...]]（例: [(1, 2, 3)]）。省略時の None は空。
bits: 第2成分以降の範囲を表す int または整数の列。3要素 (a, b, c) の場合:
  bits=8       → b, c は各 0～255。
  bits=(8, 12) → b は 0～255、c は 0～4095。
先頭の a は指定しない、負数も可。各成分の最大値が M（0以上）なら、必要なビット数は M.bit_length()。
h = PackedTupleHeap(3, bits=(8, 12), values=[(-1, 2, 3)])
h.push((0, 4, 5))     # 追加。渡すタプルの長さは常に arity
h.top(); h.pop()      # 最小値の参照 / 取り出し（空なら IndexError）
len(h); bool(h)       # 要素数 / 非空か
while h: print(h.pop())  # 空になるまで取り出す
"""

from heapq import heapify, heappop, heappush


class PackedTupleHeap:
    def __init__(
        s,
        arity: int = 2,
        bits: int | list[int] = 20,
        values: list[tuple[int, ...]] | None = None,
    ) -> None:
        s.bits = (bits,) * (arity - 1) if isinstance(bits, int) else tuple(bits)
        s.q = [s._pack(x) for x in values or ()]
        heapify(s.q)

    def __len__(s):
        return len(s.q)

    def _pack(s, x):
        x = tuple(x)
        v = x[0]
        for a, b in zip(x[1:], s.bits):
            v = (v << b) | a
        return v

    def _unpack(s, v):
        x = []
        for b in reversed(s.bits):
            x.append(v & ((1 << b) - 1))
            v >>= b
        return (v, *reversed(x))

    def top(s):
        return s._unpack(s.q[0])

    def push(s, x):
        heappush(s.q, s._pack(x))

    def pop(s):
        return s._unpack(heappop(s.q))
