class CartesianTree:
    def __init__(s, A):
        n = len(A)
        left = s.left = [-1] * n
        right = s.right = [-1] * n
        parent = s.parent = [-1] * n
        s.root = -1
        for i, x in enumerate(A):
            p = i - 1
            while p >= 0 and A[p] > x:
                left[i] = p
                p = parent[p]
            if left[i] >= 0:
                parent[left[i]] = i
            if p >= 0:
                right[p] = i
                parent[i] = p
            else:
                s.root = i
