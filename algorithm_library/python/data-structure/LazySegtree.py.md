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
  code: "class lazy_segtree(): # \u3059\u3079\u3066 0-index\n  def _update(self,k):self.data[k]=self.op(self.data[2*k],self.data[2*k+1])\n\
    \  def _all_apply(self,k,f):\n      self.data[k]=self.mapping(f,self.data[k])\n\
    \      if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])\n  def _push(self,k):\n\
    \      self._all_apply(2*k,self.lz[k])\n      self._all_apply(2*k+1,self.lz[k])\n\
    \      self.lz[k]=self.identity\n  def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):\n\
    \      self.n=len(V)\n      self.log=(self.n-1).bit_length()\n      self.size=1<<self.log\n\
    \      self.data=[E for i in range(2*self.size)]\n      self.lz=[ID for i in range(self.size)]\n\
    \      self.e=E\n      self.op=OP\n      self.mapping=MAPPING\n      self.composition=COMPOSITION\n\
    \      self.identity=ID\n      for i in range(self.n):self.data[self.size+i]=V[i]\n\
    \      for i in range(self.size-1,0,-1):self._update(i)\n  \n  # \u4E00\u70B9\u66F4\
    \u65B0\n  def set(self,p,x):\n      assert 0<=p and p<self.n\n      p+=self.size\n\
    \      for i in range(self.log,0,-1):self._push(p>>i)\n      self.data[p]=x\n\
    \      for i in range(1,self.log+1):self._update(p>>i)\n      \n  # data[p] \u3092\
    \u53D6\u5F97\u3059\u308B\n  def get(self,p):\n      assert 0<=p and p<self.n\n\
    \      p+=self.size\n      for i in range(self.log,0,-1):self._push(p>>i)\n  \
    \    return self.data[p]\n    \n  # \u533A\u9593 [l,r) \u306E\u6F14\u7B97\u7D50\
    \u679C\u3092\u8FD4\u3059\n  def prod(self,l,r):\n      assert 0<=l and l<=r and\
    \ r<=self.n\n      if l==r:return self.e\n      l+=self.size\n      r+=self.size\n\
    \      for i in range(self.log,0,-1):\n          if (((l>>i)<<i)!=l):self._push(l>>i)\n\
    \          if (((r>>i)<<i)!=r):self._push(r>>i)\n      sml,smr=self.e,self.e\n\
    \      while(l<r):\n          if l&1:\n              sml=self.op(sml,self.data[l])\n\
    \              l+=1\n          if r&1:\n              r-=1\n              smr=self.op(self.data[r],smr)\n\
    \          l>>=1\n          r>>=1\n      return self.op(sml,smr)\n  \n  # \u5168\
    \u533A\u9593\u306E\u6F14\u7B97\u7D50\u679C\u3092\u8FD4\u3059\n  def all_prod(self):return\
    \ self.data[1]\n\n  # \u4E00\u70B9\u306B\u5BFE\u3057\u3066\u64CD\u4F5C\u3059\u308B\
    \n  # \u3042\u3093\u307E\u308F\u304B\u3089\u3093\n  def apply_point(self,p,f):\n\
    \      assert 0<=p and p<self.n\n      p+=self.size\n      for i in range(self.log,0,-1):self._push(p>>i)\n\
    \      self.data[p]=self.mapping(f,self.data[p])\n      for i in range(1,self.log+1):self._update(p>>i)\n\
    \n  # \u533A\u9593\u64CD\u4F5C\n  # f \u306F mapping \u306B\u4E0E\u3048\u308B\u5F15\
    \u6570\u306E f\n  def apply(self,l,r,f):\n      assert 0<=l and l<=r and r<=self.n\n\
    \      if l==r:return\n      l+=self.size\n      r+=self.size\n      for i in\
    \ range(self.log,0,-1):\n          if (((l>>i)<<i)!=l):self._push(l>>i)\n    \
    \      if (((r>>i)<<i)!=r):self._push((r-1)>>i)\n      l2,r2=l,r\n      while(l<r):\n\
    \          if (l&1):\n              self._all_apply(l,f)\n              l+=1\n\
    \          if (r&1):\n              r-=1\n              self._all_apply(r,f)\n\
    \          l>>=1\n          r>>=1\n      l,r=l2,r2\n      for i in range(1,self.log+1):\n\
    \          if (((l>>i)<<i)!=l):self._update(l>>i)\n          if (((r>>i)<<i)!=r):self._update((r-1)>>i)\n\
    \          \n  # check(operate(data[l],data[l+1],...,data[r-1])) = True\n  # \u3092\
    \u6E80\u305F\u3059\u6700\u5927\u306E r \u3092\u8FD4\u3059\n  def max_right(self,l,check):\n\
    \      assert 0<=l and l<=self.n\n      assert check(self.e)\n      if l==self.n:return\
    \ self.n\n      l+=self.size\n      for i in range(self.log,0,-1):self._push(l>>i)\n\
    \      sm=self.e\n      while(1):\n          while(l%2==0):l>>=1\n          if\
    \ not(check(self.op(sm,self.data[l]))):\n              while(l<self.size):\n \
    \                 self._push(l)\n                  l=(2*l)\n                 \
    \ if (check(self.op(sm,self.data[l]))):\n                      sm=self.op(sm,self.data[l])\n\
    \                      l+=1\n              return l-self.size\n          sm=self.op(sm,self.data[l])\n\
    \          l+=1\n          if (l&-l)==l:break\n      return self.n\n  \n  # check(operate(data[l],data[l+1],...,data[r-1]))\
    \ = True\n  # \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E l \u3092\u8FD4\u3059\n\
    \  def min_left(self,r,check):\n      assert (0<=r and r<=self.n)\n      assert\
    \ check(self.e)\n      if r==0:return 0\n      r+=self.size\n      for i in range(self.log,0,-1):self._push((r-1)>>i)\n\
    \      sm=self.e\n      while(1):\n          r-=1\n          while(r>1 and (r%2)):r>>=1\n\
    \          if not(check(self.op(self.data[r],sm))):\n              while(r<self.size):\n\
    \                  self._push(r)\n                  r=(2*r+1)\n              \
    \    if check(self.op(self.data[r],sm)):\n                      sm=self.op(self.data[r],sm)\n\
    \                      r-=1\n              return r+1-self.size\n          sm=self.op(self.data[r],sm)\n\
    \          if (r&-r)==r:break\n      return 0\n\n# data \u306E\u5358\u4F4D\u5143\
    \ne = 0\n# lazy \u306E\u5358\u4F4D\u5143\n# \u533A\u9593\u66F4\u65B0\u306A\u3089\
    \ lazy \u3068\u3057\u3066\u3068\u308A\u3048\u306A\u3044\u5024\u306B\u3059\u308B\
    \nide = 0\n\n# \u533A\u9593\u306B\u5BFE\u3057\u3066\u884C\u3044\u305F\u3044\u6F14\
    \u7B97\ndef operate(a,b):\n  return a+b\n\n# \u9045\u5EF6\u3055\u305B\u3066\u3044\
    \u305F\u64CD\u4F5C\u3092data\u306B\u4F1D\u642C\u3055\u305B\u308B\u95A2\u6570\n\
    # f \u304C\u9045\u5EF6\u3055\u305B\u305F\u64CD\u4F5C\u3001x \u304Cdata\n# ex.\
    \ \u533A\u9593\u52A0\u7B97\u306A\u3089 f+x\ndef mapping(f,x):\n  # \u533A\u9593\
    \u66F4\u65B0\u306A\u3089\n  # if f==ide: return x\n  return f+x\n\n# \u65E2\u306B\
    \u9045\u5EF6\u3055\u305B\u3066\u3044\u305F\u64CD\u4F5C\u306B\u3055\u3089\u306B\
    \u64CD\u4F5C\u3092\u8FFD\u52A0\u3059\u308B\u95A2\u6570\n# f \u304C\u8FFD\u52A0\
    \u3059\u308B\u64CD\u4F5C\u3001g \u304C\u3044\u307E\u307E\u3067\u306E\u64CD\u4F5C\
    \ndef composition(f,g): \n  # \u533A\u9593\u66F4\u65B0\u306A\u3089\n  # if f==ide:\
    \ return g\n  return f+g\n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/LazySegtree.py
  requiredBy: []
  timestamp: '2025-01-17 21:54:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/LazySegtree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/LazySegtree.py
- /library/algorithm_library/python/data-structure/LazySegtree.py.html
title: algorithm_library/python/data-structure/LazySegtree.py
---
