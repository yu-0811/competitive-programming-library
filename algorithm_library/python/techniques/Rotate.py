def two_dimension_list_rotate_R90(L: list[list[int]]) -> list[list[int]]:
    # 2次元リストを右に90度回転させる
    return [list(col) for col in zip(*L[::-1])]


def two_dimension_list_rotate_L90(L: list[list[int]]) -> list[list[int]]:
    # 2次元リストを左に90度回転させる
    return [list(col) for col in zip(*L)][::-1]


def tention(L: list[list[int]]) -> list[list[int]]:
    # 2次元リストを転置する
    return [list(col) for col in zip(*L)]
