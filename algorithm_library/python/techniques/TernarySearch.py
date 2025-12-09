def ternary_search_float(f, left, right, eps=1e-9, maximize=False):
    """
    f が [left, right] 上で 凸 or 凹 だと仮定して、
    その最小値（または最大値）を 3 分探索で求める。
    maximize=False: 最小値を探す
    maximize=True : 最大値を探す
    返り値: (最適解の範囲の左端, 右端, f(中点))
    """
    while right - left > eps:
        m1 = (2 * left + right) / 3
        m2 = (left + 2 * right) / 3
        f1 = f(m1)
        f2 = f(m2)

        if not maximize:
            if f1 > f2:
                left = m1
            else:
                right = m2
        else:
            if f1 < f2:
                left = m1
            else:
                right = m2

        if right - left < eps:
            break

    x = (left + right) / 2
    return left, right, f(x)


def ternary_search_int(f, left, right, eps, maximize=False):
    """
    f: int -> 値 を返す一峰性関数（山 or 谷）
    [left, right] の整数範囲で、f の最大値 or 最小値を探す。
    maximize=True  なら最大値を探す
    maximize=False なら最小値を探す

    戻り値: (arg_opt, f(arg_opt))
    """

    while right - left > eps:
        m1 = (2 * left + right) // 3
        m2 = (left + 2 * right) // 3

        f1 = f(m1)
        f2 = f(m2)

        if not maximize:
            if f1 > f2:
                left = m1
            else:
                right = m2
        else:
            if f1 < f2:
                left = m1
            else:
                right = m2

    # 残った [left, right] を愚直に見る
    best_x = left
    best_val = f(left)
    for x in range(left + 1, right + 1):
        val = f(x)
        if (maximize and val > best_val) or (not maximize and val < best_val):
            best_val = val
            best_x = x

    return best_x, best_val
