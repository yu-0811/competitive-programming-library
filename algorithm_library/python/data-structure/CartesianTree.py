class CartesianTree:
    def __init__(self, A):
        n = len(A)
        self.root = 0
        self.left = [-1] * n
        self.right = [-1] * n
        self.parent = [-1] * n
        st = [-1] * n
        st[0] = 0
        st_top = 0
        for i in range(1, n):
            if A[st[st_top]] > A[i]:  # pop してから push
                while st_top >= 1 and A[st[st_top - 1]] > A[i]:
                    st_top -= 1
                # st_top > 0 なら A[st[top-1]] <= A[i] < A[st[top]]
                # st[st_top] を左の子、st[st_top-1] を親にする
                self.left[i] = st[st_top]
                self.parent[self.left[i]] = i
                if st_top == 0:
                    self.root = i
                else:
                    self.parent[i] = st[st_top - 1]
                    self.right[self.parent[i]] = i
                st[st_top] = i
            else:  # push するだけ
                self.parent[i] = st[st_top]
                self.right[self.parent[i]] = i
                st_top += 1
                st[st_top] = i
