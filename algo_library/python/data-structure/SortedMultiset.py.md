---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# tatyam set \u306E\u30B3\u30D4\u30DA\n# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py\n\
    import math\nfrom bisect import bisect_left, bisect_right\nfrom typing import\
    \ Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional\nT = TypeVar('T')\n\
    \nclass SortedMultiset(Generic[T]):\n    BUCKET_RATIO = 16\n    SPLIT_RATIO =\
    \ 24\n    \n    def __init__(self, a: Iterable[T] = []) -> None:\n        \"Make\
    \ a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)\"\n      \
    \  a = list(a)\n        n = self.size = len(a)\n        if any(a[i] > a[i + 1]\
    \ for i in range(n - 1)):\n            a.sort()\n        num_bucket = int(math.ceil(math.sqrt(n\
    \ / self.BUCKET_RATIO)))\n        self.a = [a[n * i // num_bucket : n * (i + 1)\
    \ // num_bucket] for i in range(num_bucket)]\n\n    def __iter__(self) -> Iterator[T]:\n\
    \        for i in self.a:\n            for j in i: yield j\n\n    def __reversed__(self)\
    \ -> Iterator[T]:\n        for i in reversed(self.a):\n            for j in reversed(i):\
    \ yield j\n    \n    def __eq__(self, other) -> bool:\n        return list(self)\
    \ == list(other)\n    \n    def __len__(self) -> int:\n        return self.size\n\
    \    \n    def __repr__(self) -> str:\n        return \"SortedMultiset\" + str(self.a)\n\
    \    \n    def __str__(self) -> str:\n        s = str(list(self))\n        return\
    \ \"{\" + s[1 : len(s) - 1] + \"}\"\n\n    def _position(self, x: T) -> Tuple[List[T],\
    \ int, int]:\n        \"return the bucket, index of the bucket and position in\
    \ which x should be. self must not be empty.\"\n        for i, a in enumerate(self.a):\n\
    \            if x <= a[-1]: break\n        return (a, i, bisect_left(a, x))\n\n\
    \    def __contains__(self, x: T) -> bool:\n        if self.size == 0: return\
    \ False\n        a, _, i = self._position(x)\n        return i != len(a) and a[i]\
    \ == x\n\n    def count(self, x: T) -> int:\n        \"Count the number of x.\"\
    \n        return self.index_right(x) - self.index(x)\n\n    def add(self, x: T)\
    \ -> None:\n        \"Add an element. / O(\u221AN)\"\n        if self.size ==\
    \ 0:\n            self.a = [[x]]\n            self.size = 1\n            return\n\
    \        a, b, i = self._position(x)\n        a.insert(i, x)\n        self.size\
    \ += 1\n        if len(a) > len(self.a) * self.SPLIT_RATIO:\n            mid =\
    \ len(a) >> 1\n            self.a[b:b+1] = [a[:mid], a[mid:]]\n    \n    def _pop(self,\
    \ a: List[T], b: int, i: int) -> T:\n        ans = a.pop(i)\n        self.size\
    \ -= 1\n        if not a: del self.a[b]\n        return ans\n\n    def discard(self,\
    \ x: T) -> bool:\n        \"Remove an element and return True if removed. / O(\u221A\
    N)\"\n        if self.size == 0: return False\n        a, b, i = self._position(x)\n\
    \        if i == len(a) or a[i] != x: return False\n        self._pop(a, b, i)\n\
    \        return True\n\n    def lt(self, x: T) -> Optional[T]:\n        \"Find\
    \ the largest element < x, or None if it doesn't exist.\"\n        for a in reversed(self.a):\n\
    \            if a[0] < x:\n                return a[bisect_left(a, x) - 1]\n\n\
    \    def le(self, x: T) -> Optional[T]:\n        \"Find the largest element <=\
    \ x, or None if it doesn't exist.\"\n        for a in reversed(self.a):\n    \
    \        if a[0] <= x:\n                return a[bisect_right(a, x) - 1]\n\n \
    \   def gt(self, x: T) -> Optional[T]:\n        \"Find the smallest element >\
    \ x, or None if it doesn't exist.\"\n        for a in self.a:\n            if\
    \ a[-1] > x:\n                return a[bisect_right(a, x)]\n\n    def ge(self,\
    \ x: T) -> Optional[T]:\n        \"Find the smallest element >= x, or None if\
    \ it doesn't exist.\"\n        for a in self.a:\n            if a[-1] >= x:\n\
    \                return a[bisect_left(a, x)]\n    \n    def __getitem__(self,\
    \ i: int) -> T:\n        \"Return the i-th element.\"\n        if i < 0:\n   \
    \         for a in reversed(self.a):\n                i += len(a)\n          \
    \      if i >= 0: return a[i]\n        else:\n            for a in self.a:\n \
    \               if i < len(a): return a[i]\n                i -= len(a)\n    \
    \    raise IndexError\n    \n    def pop(self, i: int = -1) -> T:\n        \"\
    Pop and return the i-th element.\"\n        if i < 0:\n            for b, a in\
    \ enumerate(reversed(self.a)):\n                i += len(a)\n                if\
    \ i >= 0: return self._pop(a, ~b, i)\n        else:\n            for b, a in enumerate(self.a):\n\
    \                if i < len(a): return self._pop(a, b, i)\n                i -=\
    \ len(a)\n        raise IndexError\n\n    def index(self, x: T) -> int:\n    \
    \    \"Count the number of elements < x.\"\n        ans = 0\n        for a in\
    \ self.a:\n            if a[-1] >= x:\n                return ans + bisect_left(a,\
    \ x)\n            ans += len(a)\n        return ans\n\n    def index_right(self,\
    \ x: T) -> int:\n        \"Count the number of elements <= x.\"\n        ans =\
    \ 0\n        for a in self.a:\n            if a[-1] > x:\n                return\
    \ ans + bisect_right(a, x)\n            ans += len(a)\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/data-structure/SortedMultiset.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/data-structure/SortedMultiset.py
layout: document
redirect_from:
- /library/algo_library/python/data-structure/SortedMultiset.py
- /library/algo_library/python/data-structure/SortedMultiset.py.html
title: algo_library/python/data-structure/SortedMultiset.py
---
