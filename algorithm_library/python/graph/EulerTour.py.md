---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class segtree():\n  def __init__(self,V,OP,E):\n      self.n=len(V)\n   \
    \   self.op=OP\n      self.e=E\n      self.log=(self.n-1).bit_length()\n     \
    \ self.size=1<<self.log\n      self.data=[E for i in range(2*self.size)]\n   \
    \   for i in range(self.n): self.data[self.size+i]=V[i]\n      for i in range(self.size-1,0,-1):self._update(i)\n\
    \  def set(self,p,x): \n      assert 0<=p and p<self.n\n      p+=self.size\n \
    \     self.data[p]=x\n      for i in range(1,self.log+1):self._update(p>>i)\n\
    \  def add(self,p,x): \n      assert 0<=p and p<self.n\n      p+=self.size\n \
    \     self.data[p] += x\n      for i in range(1,self.log+1):self._update(p>>i)\n\
    \  def get(self,p):\n      assert 0<=p and p<self.n\n      return self.data[p+self.size]\n\
    \  def prod(self,l,r):\n      assert 0<=l and l<=r and r<=self.n\n      sml=self.e;\
    \ smr=self.e\n      l+=self.size; r+=self.size\n      while(l<r):\n          if\
    \ (l&1):sml=self.op(sml,self.data[l]);l+=1\n          if (r&1):smr=self.op(self.data[r-1],smr);r-=1\n\
    \          l>>=1;r>>=1\n      return self.op(sml,smr)\n  def _update(self,k):\n\
    \      self.data[k]=self.op(self.data[2*k],self.data[2*k+1])\n  def __str__(self):\n\
    \      return str([self.get(i) for i in range(self.n)])\n  \nclass fenwick_tree():\n\
    \    def __init__(self,N,data):\n        self.n=N\n        self.data=[0 for i\
    \ in range(N)]\n    def add(self,p,x):\n        assert 0<=p<self.n,\"0<=p<n,p={0},n={1}\"\
    .format(p,self.n)\n        p+=1\n        while(p<=self.n):\n            self.data[p-1]+=x\n\
    \            p+=p& -p\n    def sum(self,l,r):\n        assert (0<=l and l<=r and\
    \ r<=self.n),\"0<=l<=r<=n,l={0},r={1},n={2}\".format(l,r,self.n)\n        return\
    \ self.sum0(r)-self.sum0(l)\n    def sum0(self,r):\n        s=0\n        while(r>0):\n\
    \            s+=self.data[r-1]\n            r-=r&-r\n        return s\n\nclass\
    \ EulerTour:\n    def __init__(self, N:int):\n        self.N = N\n        self.G\
    \ = [[] for _ in range(N+1)]\n        self._in = [-1]*(N+1) # \u5404\u9802\u70B9\
    \u306E\u8A2A\u554F\u958B\u59CB\u6642\u523B\n        self._out = [-1]*(N+1) # \u5404\
    \u9802\u70B9\u306E\u8A2A\u554F\u7D42\u4E86\u6642\u523B\n        self.edge_cnt\
    \ = 0\n        self.edge_cost = []\n        # \u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\
    \u30FC\u3067\u306E\u8A2A\u554F\u9806\n        self.vartex_order = []\n       \
    \ self.edge_order = []\n        self.depth = [-1]\n        \n    def add_edge(self,\
    \ u:int, v:int, w:int):\n        self.edge_cnt += 1\n        self.G[u].append((v,\
    \ w, self.edge_cnt))\n        self.G[v].append((u, w, self.edge_cnt))\n    \n\
    \    def _dfs(self, v:int):\n        stack = []\n        stack.append((\"f\",\
    \ v, 0, 0))\n        while stack:\n            state, v, w, idx = stack.pop()\n\
    \            if state == \"f\": # \u884C\u304D\u304C\u3051\n                if\
    \ self.vis[v]: \n                    stack.pop()\n                    continue\n\
    \                self.vis[v] = True\n                self.depth.append(self.depth[-1]+1)\n\
    \                self.edge_order.append(idx)\n                self.edge_cost.append(w)\n\
    \                self._in[v] = len(self.edge_order)-1\n                self._out[v]\
    \ = len(self.edge_order)-1\n                self.vartex_order.append(v)\n    \
    \            for u, w, edge_idx in self.G[v]:\n                    if self.vis[u]:\
    \ continue\n                    stack.append((\"b\", v, w, edge_idx))\n      \
    \              stack.append((\"f\", u, w, edge_idx))\n            else: # \u5E30\
    \u308A\u304C\u3051\n                self.depth.append(self.depth[-1]-1)\n    \
    \            self.vartex_order.append(-v)\n                self.edge_order.append(-idx)\n\
    \                self.edge_cost.append(-w)\n                self._out[v] = len(self.edge_order)-1\n\
    \n    def _euler_tour(self, root:int):\n        # edge_cost \u5185\u3067\u8FBA\
    \ i \u304C\u4F55\u756A\u76EE\u306B\u767B\u5834\u3059\u308B\u304B(+\u3068-\u3067\
    \u305D\u308C\u305E\u308C)\n        self.edge_idx_plus = [-1] * (self.edge_cnt+1)\n\
    \        self.edge_idx_minus = [-1] * (self.edge_cnt+1)\n        self.vis = [False]*(self.N+1)\n\
    \        self.step = 0\n        self._dfs(root)\n        \n    def _build_fentree(self):\n\
    \        self.fen = fenwick_tree(len(self.edge_cost))\n        for i in range(1,\
    \ len(self.edge_cost)):\n            self.fen.add(i, self.edge_cost[i])\n    \
    \    \n    def _build_lca(self):\n        # lca \u7528\u306E\u30BB\u30B0\u6728\
    \u306E\u69CB\u7BC9\n        inf = pow(10,18)\n        e = [inf,inf]\n        def\
    \ operate(a,b): \n            if a[0] < b[0]: return a\n            else: return\
    \ b\n        s = [[d,abs(v)] for d, v in zip(self.depth, self.vartex_order)]\n\
    \        self.lca_seg = segtree(s, operate, e)\n        \n    def build(self,\
    \ root:int):\n        self.root = root\n        self._euler_tour(root)\n     \
    \   self.depth.pop(0)\n        self._build_fentree()\n        self._build_lca()\n\
    \        \n    # u \u3092\u6839\u3068\u3059\u308B\u90E8\u5206\u6728\u306E\u8FBA\
    \u306E\u30B3\u30B9\u30C8\u306E\u548C\n    def subtree_sum(self, u:int):\n    \
    \    return self.fen.sum0(self._in[u]+1)\n    \n    # \u6839\u304B\u3089 u \u3078\
    \u306E\u30D1\u30B9\u306E\u30B3\u30B9\u30C8\u306E\u548C\n    def path_sum(self,\
    \ u:int):\n        return self.fen.sum0(self._in[u]+1)\n    \n    # lca(u, v)\n\
    \    def lca(self, u:int, v:int):\n        in_u, in_v = self._in[u], self._in[v]\n\
    \        if in_u > in_v: in_u, in_v = in_v, in_u\n        lca_idx = self.lca_seg.prod(in_u,\
    \ in_v+1)[1]\n        return lca_idx\n    \n    # \u30D1\u30B9 u - v \u306E\u30B3\
    \u30B9\u30C8\u306E\u548C\n    def get_distance(self, u:int, v:int):\n        lca_idx\
    \ = self.lca(u, v)\n        return self.subtree_sum(u) + self.subtree_sum(v) -\
    \ 2*self.subtree_sum(lca_idx)"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/EulerTour.py
  requiredBy: []
  timestamp: '2025-12-05 18:59:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/EulerTour.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/EulerTour.py
- /library/algorithm_library/python/graph/EulerTour.py.html
title: algorithm_library/python/graph/EulerTour.py
---
