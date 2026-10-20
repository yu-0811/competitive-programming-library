def run_length_compression(S: str):
    res = []
    tmp = S[0]
    it = iter(S)
    next(it)
    cnt = 1
    for s in it:
        if s == tmp:
            cnt += 1
        else:
            res.append((tmp, cnt))
            tmp = s
            cnt = 1
    res.append((tmp, cnt))
    return res
