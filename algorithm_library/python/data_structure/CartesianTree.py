class CartesianTree:
    def __init__(s, A):
        n = len(A)
        left = s.left = [-1] * n
        right = s.right = [-1] * n
        parent = s.parent = [-1] * n
        stack = []
        for i in range(n):
            last = -1
            while stack and A[stack[-1]] > A[i]:
                last = stack.pop()
            if stack:
                p = parent[i] = stack[-1]
                right[p] = i
            if last >= 0:
                left[i] = last
                parent[last] = i
            stack.append(i)
        s.root = stack[0]
