def mos_algorithm(data, queries):
    """
    data : list of int : 元の配列
    queries : list of tuple : クエリのリスト
    クエリは 0-indexed で半開区間[l,r)
    """
    from math import sqrt, ceil
    n = len(data)
    q = len(queries)
    B = ceil(sqrt(3)*n / (sqrt(2)*sqrt(q))) # bukectのサイズ(nyaanさんの記事より)
    L,R = 0,0
    # queryの順番を格納する用
    order = [-1] * q

    ########################################
    # 状態を初期化する処理を書く

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

    # クエリの解答順
    # (ceil(l/B), r*-1^{ceil(l/B)}) の昇順にするのが最速ぽい
    for idx, (l,r) in enumerate(queries):
        order[idx] = ((l//B)<<40)+((r if (l//B)&1 else -r)<<20)+idx
    order.sort()

    mask = (1<<20)-1
    ret = [-1] * q
    for lri in order:  # クエリに答えていく
        i = lri & mask
        l,r = queries[i]
        
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