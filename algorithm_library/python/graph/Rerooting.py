# 全方位木DP
class rerooting:
    def __init__(
        self,
        n: int,
        edges: list[tuple[int, int]],
        e: int,
        merge: callable,
        calc_node_value: callable,
        calc_ans: callable,
    ):
        self.n = n
        self.e = e
        self.merge = merge
        self.calc_node_value = calc_node_value
        self.calc_ans = calc_ans
        # g[i] = i と隣接する頂点のリスト
        g = self.g = [[] for _ in range(n + 1)]
        # rev[i][j] = g[i][j](iのj番目の隣接頂点)にとって、iが何番目の隣接頂点か
        # g[g[i][j]][rev[i][j]] == i である
        rev = self.rev = [[] for _ in range(n + 1)]
        for a, b in edges:
            rev[a].append(len(g[b]))
            rev[b].append(len(g[a]))
            g[a].append(b)
            g[b].append(a)
        # dp[i] = iの子の部分木の値
        # dp[i][j] = i を親とし、g[i][j]を根とした部分木の値
        self.dp = [[e] * len(row) for row in g]
        # ans[i] = i を根としたときの求めたい値
        self.ans = [e] * (n + 1)

    # root から DFS して、子の部分木の値を計算
    def _dfs1(self, root):
        g, rev, dp = self.g, self.rev, self.dp
        e, merge, add = self.e, self.merge, self.calc_node_value
        par = self.par = [-1] * (self.n + 1)
        order = self.order = []  # DFSでの訪問順
        stack = [root]
        while stack:
            v = stack.pop()
            order.append(v)
            for u in g[v]:
                if u != par[v]:
                    par[u] = v
                    stack.append(u)
        # 訪問順を逆順にして、子から値を計算していく
        for v in reversed(order[1:]):
            p, x = par[v], e
            for i, u in enumerate(g[v]):
                if u == p:
                    j = rev[v][i]
                else:
                    x = merge(x, dp[v][i])
            # v を根とした部分木の値を親側に記録
            dp[p][j] = add(x, v)

    # 親の部分木の値を使って、自分を根とした部分木の値を計算
    def _dfs2(self):
        g, rev, dp = self.g, self.rev, self.dp
        e, merge, add = self.e, self.merge, self.calc_node_value
        par, ans, answer = self.par, self.ans, self.calc_ans
        for v in self.order:
            val, idx, p = dp[v], rev[v], par[v]
            # 子の部分木の値の左からの累積
            left = e
            # 子の部分木の値の右からの累積
            # right[i] = merge(dp[v][i+1], dp[v][i+2], ..., dp[v][len(g[v])-1])
            right = [e] * len(val)
            for i in range(len(val) - 2, -1, -1):
                right[i] = merge(val[i + 1], right[i + 1])
            for j, u in enumerate(g[v]):
                if u != p:
                    # u が親、v が根の部分木の値を計算(u を考慮しないときの値)
                    # maerge(left, right[j]) で u 以外の v の子の値を計算
                    res = add(merge(left, right[j]), v)
                    # いま親とした頂点の配列に記録
                    dp[u][idx[j]] = res
                # left を更新
                left = merge(left, val[j])
            # v を根としたときの求めたい値を計算
            ans[v] = answer(left, v)

    def run(self, root=1):
        self._dfs1(root)
        self._dfs2()
        return self.ans


"""
e = 頂点に持たせる値(関数のaに渡される)の単位元
merge(a, b) = 部分木の値 a, b をマージする関数
calc_node_value(a, v) = すべての子部分木の値をマージした値 a から頂点 v を根としたときの計算に使う値(DPの値)を計算する関数
calc_ans(a, v) = すべての子部分木の値をマージした値 a から頂点 v を根としたときの求めたいものを計算する関数
"""

# e =
# def merge(a,b):
#   return
# def calc_node_value(a,v):
#   return
# def calc_ans(a,v):
#     return


# rr = rerooting(N, edges, e, merge, calc_node_value, calc_ans)
