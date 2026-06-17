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
    - https://github.com/tatyam-prime/SortedSet/blob/main/codon/BucketList.py
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://github.com/tatyam-prime/SortedSet/blob/main/codon/BucketList.py\n\
    import math\nfrom typing import ClassVar, Generator\n\nclass BucketList[T]:\n\
    \    size: int\n    a: list[list[T]]\n    BUCKET_RATIO: ClassVar[int] = 16\n \
    \   SPLIT_RATIO: ClassVar[int] = 24\n\n    def __init__(self) -> None:\n     \
    \   self.size = 0\n        self.a = []\n\n    def __init__(self, a: Generator[T])\
    \ -> None:\n        self.__init__(list(a))\n    \n    def __init__(self, a: list[T])\
    \ -> None:\n        n = self.size = len(a)\n        num_bucket = int(math.ceil(math.sqrt(n\
    \ / self.BUCKET_RATIO)))\n        self.a = [a[n * i // num_bucket : n * (i + 1)\
    \ // num_bucket] for i in range(num_bucket)]\n\n    def __iter__(self) -> Generator[T]:\n\
    \        for i in self.a:\n            for j in i: yield j\n\n    def __reversed__(self)\
    \ -> Generator[T]:\n        for i in reversed(self.a):\n            for j in reversed(i):\
    \ yield j\n    \n    def __eq__(self, other) -> bool:\n        if len(self) !=\
    \ len(other): return False\n        for x, y in zip(self, other):\n          \
    \  if x != y: return False\n        return True\n    \n    def __ne__(self, other)\
    \ -> bool:\n        return not self.__eq__(other)\n\n    def __len__(self) ->\
    \ int:\n        return self.size\n    \n    def __bool__(self) -> bool:\n    \
    \    return self.size > 0\n\n    def __repr__(self) -> str:\n        return \"\
    BucketList\" + str(self.a)\n    \n    def __str__(self) -> str:\n        return\
    \ str(list(self))\n\n    def __contains__(self, x: T) -> bool:\n        \"Return\
    \ True if x is in the bucket list. / O(N)\"\n        for y in self:\n        \
    \    if x == y: return True\n        return False\n    \n    def _insert(self,\
    \ a: list[T], b: int, i: int, x: T) -> None:\n        a.insert(i, x)\n       \
    \ self.size += 1\n        if len(a) > len(self.a) * self.SPLIT_RATIO:\n      \
    \      mid = len(a) >> 1\n            self.a[b:b+1] = [a[:mid], a[mid:]]\n\n \
    \   def insert(self, i: int, x: T) -> None:\n        \"Insert x at the i-th position.\
    \ / O(\u221AN)\"\n        if self.size == 0:\n            if i != 0 and i != -1:\n\
    \                raise IndexError(\"index out of range\")\n            self.a\
    \ = [[x]]\n            self.size = 1\n            return\n        if i < 0:\n\
    \            for b, a in enumerate(reversed(self.a)):\n                i += len(a)\n\
    \                if i >= 0: return self._insert(a, len(self.a) + ~b, i, x)\n \
    \       else:\n            for b, a in enumerate(self.a):\n                if\
    \ i <= len(a): return self._insert(a, b, i, x)\n                i -= len(a)\n\
    \        raise IndexError(\"index out of range\")\n\n    def append(self, x: T)\
    \ -> None:\n        \"Append x to the end of the list. / amortized O(1)\"\n  \
    \      if self.size == 0:\n            self.a = [[x]]\n            self.size =\
    \ 1\n            return\n        a = self.a[-1]\n        return self._insert(a,\
    \ len(self.a) - 1, len(a), x)\n    \n    def extend(self, a: Generator[T]) ->\
    \ None:\n        for x in a: self.append(x)\n    \n    def __getitem__(self, i:\
    \ int) -> T:\n        if i < 0:\n            for a in reversed(self.a):\n    \
    \            i += len(a)\n                if i >= 0: return a[i]\n        else:\n\
    \            for a in self.a:\n                if i < len(a): return a[i]\n  \
    \              i -= len(a)\n        raise IndexError(\"index out of range\")\n\
    \n    def _pop(self, a: list[T], b: int, i: int) -> T:\n        ans = a.pop(i)\n\
    \        self.size -= 1\n        if not a: del self.a[b]\n        return ans\n\
    \    \n    def pop(self, i: int = -1) -> T:\n        \"Remove and return the i-th\
    \ element. / O(\u221AN) / O(-i) if i < 0\"\n        if i < 0:\n            for\
    \ b, a in enumerate(reversed(self.a)):\n                i += len(a)\n        \
    \        if i >= 0: return self._pop(a, ~b, i)\n        else:\n            for\
    \ b, a in enumerate(self.a):\n                if i < len(a): return self._pop(a,\
    \ b, i)\n                i -= len(a)\n        raise IndexError(\"index out of\
    \ range\")\n\n    def count(self, x: T) -> int:\n        \"Return the number of\
    \ occurrences of x. / O(N)\"\n        return sum(1 for y in self if x == y)\n\n\
    \    def index(self, x: T) -> int:\n        \"Return the index of the first occurrence\
    \ of x, raise ValueError if not found. / O(N)\"\n        for i, y in enumerate(self):\n\
    \            if x == y: return i\n        raise ValueError(\"value not in list\"\
    )\n\n    def remove(self, x: T) -> None:\n        \"Remove the first occurrence\
    \ of x, raise ValueError if not found. / O(N)\"\n        self.pop(self.index(x))\n\
    \n    def clear(self) -> None:\n        self.a = []\n        self.size = 0\n\n\
    \    def reverse(self) -> None:\n        self.a.reverse()\n        for a in self.a:\
    \ a.reverse()\n\n    def copy(self):\n        return BucketList(self)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/codon/BucketList.py
  requiredBy: []
  timestamp: '2026-06-17 12:49:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/codon/BucketList.py
layout: document
redirect_from:
- /library/tatyam_set/codon/BucketList.py
- /library/tatyam_set/codon/BucketList.py.html
title: tatyam_set/codon/BucketList.py
---
