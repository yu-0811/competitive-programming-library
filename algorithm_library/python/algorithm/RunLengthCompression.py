def run_length_compression(S : str):
    res = []
    tmp = S[0]
    cnt = 1
    for i in range(1,len(S)):
        if S[i]==tmp: cnt += 1
        else:
            res.append((tmp,cnt))
            tmp = S[i]; cnt = 1
    res.append((tmp,cnt))
    return res