def compare(a: tuple[int, int], b: tuple[int, int]):
    ax, ay = a
    bx, by = b

    # 領域判定 (0: 上半平面 [0, 180度), 1: 下半平面 [180, 360度))
    # ay < 0 または (ay == 0 かつ ax < 0) の場合が下半平面
    ah = 1 if (ay < 0 or (ay == 0 and ax < 0)) else 0
    bh = 1 if (by < 0 or (by == 0 and bx < 0)) else 0
    # 領域が異なる場合上半平面を優先
    if ah != bh:
        return -1 if ah < bh else 1

    # 外積計算 (ax*by - ay*bx)
    # 正なら反時計回り(aが先)、負なら時計回り(bが先)
    cross = ax * by - ay * bx
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0


def is_same_angle(p1, p2):
    """
    2点 p1, p2 が原点から見て同じ偏角（同じ方向）にあるか判定する。
    ※原点(0,0)が含まれる場合はFalse
    """
    ax, ay = p1
    bx, by = p2

    # 1. 外積が0でなければ、そもそも同一直線上にない
    if ax * by - ay * bx != 0:
        return False

    # 2. 内積が正でなければ、逆向き（180度反対）または原点を含んでいる
    #    内積 > 0 ならば同じ向き
    if ax * bx + ay * by > 0:
        return True

    return False


# 使用例
# A = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
# A.sort(key=cmp_to_key(compare))
