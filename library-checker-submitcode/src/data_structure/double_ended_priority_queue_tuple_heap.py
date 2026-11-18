# problem: https://judge.yosupo.jp/problem/double_ended_priority_queue
# include: algorithm_library/python/data_structure/TupleHeap.py


def main():
    N, Q = map(int, readline().split())
    records = [{"value": x, "alive": True} for x in map(int, readline().split())]
    lo = TupleHeap(1, ((r["value"], r) for r in records))
    # -value を上位・下位に分け、先頭2成分の辞書順で最大値を探す。
    # 末尾の dict は、同じ値が複数あっても比較しない。
    hi = TupleHeap(2, ((*divmod(-r["value"], 1 << 16), r) for r in records))
    ans = []
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 0:
            x = query[1]
            record = {"value": x, "alive": True}
            lo.push((x, record))
            hi.push((*divmod(-x, 1 << 16), record))
        else:
            heap = lo if query[0] == 1 else hi
            while not heap.top()[-1]["alive"]:
                heap.pop()
            record = heap.pop()[-1]
            record["alive"] = False
            ans.append(str(record["value"]))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
