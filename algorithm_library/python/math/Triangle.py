def triangle_area2(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]):
    """
    三角形ABCの面積の2倍を返す。
    座標が整数なら結果も整数。
    """
    ax, ay = a
    bx, by = b
    cx, cy = c
    return abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))


def triangle_area(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]):
    """
    三角形ABCの面積を返す。
    """
    return triangle_area2(a, b, c) / 2
