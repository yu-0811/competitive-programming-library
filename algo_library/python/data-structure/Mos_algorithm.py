def mos_algorithm(data, queries):
    """
    data : list of int : 元の配列
    queries : list of tuple : クエリのリスト
    """
    from math import sqrt, ceil
    n = len(data)
    b = ceil(sqrt(n))  # bukectのサイズ及び個数
    # [l,r)の半開区間で考える
    L = 0
    R = 0
    # queryを格納する用
    bucket = [list() for _ in range((b + 1))]

    ########################################
    # 状態を初期化する処理を書く
    ans = 0
    ########################################

    def _add(i, ans):
        # i番目の要素を含めて考えるときへstatesを更新
        ########################################

        return ans
        ########################################

    def _delete(i, ans):
        # i番目の要素を除いて考えるときへstatesを更新
        ########################################

        return ans
        ########################################

    upper = len(queries)
    upper_upper = upper * (n + 1)

    for idx, (l, r) in enumerate(queries):  # queryをbucketに格納
        bucket[l // b].append(idx + l*upper + r*upper_upper)

    for i in range(len(bucket)):
        if i%2==0: bucket[i].sort()
        else: bucket[i].sort(reverse=True)

    ret = [-1] * len(queries)
    for b in bucket:
        for lri in b:  # クエリに答えていく
            i = lri % upper
            r = lri // upper_upper
            l = (lri % upper_upper) // upper
            
            # クエリ[l,r)に対してstatesを更新する
            while R < r:  # rまで伸長
                ans = _add(R,ans)
                R += 1
            while R > r:  # rまで短縮
                R -= 1
                ans = _delete(R,ans)
                
            while L < l:  # lまで短縮
                ans = _delete(L,ans)
                L += 1
            while L > l:  # lまで伸長
                L -= 1
                ans = _add(L,ans)
            
            ########################################
            # クエリに答える作業をここで書く
            # ret[i] に i 番目のクエリの答えを格納する
            ret[i] = ans
            ########################################
    return ret