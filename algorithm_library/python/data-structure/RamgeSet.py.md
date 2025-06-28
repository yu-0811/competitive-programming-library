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
    - https://atcoder.jp/contests/abc330/editorial/7754
    - https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py\nimport\
    \ math\nfrom bisect import bisect_left, bisect_right\nfrom typing import Generic,\
    \ Iterable, Iterator, List, Tuple, TypeVar, Optional\nT = TypeVar('T')\n\nclass\
    \ SortedSet(Generic[T]):\n    BUCKET_RATIO = 16\n    SPLIT_RATIO = 24\n    \n\
    \    def __init__(self, a: Iterable[T] = []) -> None:\n        \"Make a new SortedSet\
    \ from iterable. / O(N) if sorted and unique / O(N log N)\"\n        a = list(a)\n\
    \        n = len(a)\n        if any(a[i] > a[i + 1] for i in range(n - 1)):\n\
    \            a.sort()\n        if any(a[i] >= a[i + 1] for i in range(n - 1)):\n\
    \            a, b = [], a\n            for x in b:\n                if not a or\
    \ a[-1] != x:\n                    a.append(x)\n        n = self.size = len(a)\n\
    \        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))\n     \
    \   self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]\n\
    \n    def __iter__(self) -> Iterator[T]:\n        for i in self.a:\n         \
    \   for j in i: yield j\n\n    def __reversed__(self) -> Iterator[T]:\n      \
    \  for i in reversed(self.a):\n            for j in reversed(i): yield j\n   \
    \ \n    def __eq__(self, other) -> bool:\n        return list(self) == list(other)\n\
    \    \n    def __len__(self) -> int:\n        return self.size\n    \n    def\
    \ __repr__(self) -> str:\n        return \"SortedSet\" + str(self.a)\n    \n \
    \   def __str__(self) -> str:\n        s = str(list(self))\n        return \"\
    {\" + s[1 : len(s) - 1] + \"}\"\n\n    def _position(self, x: T) -> Tuple[List[T],\
    \ int, int]:\n        \"return the bucket, index of the bucket and position in\
    \ which x should be. self must not be empty.\"\n        for i, a in enumerate(self.a):\n\
    \            if x <= a[-1]: break\n        return (a, i, bisect_left(a, x))\n\n\
    \    def __contains__(self, x: T) -> bool:\n        if self.size == 0: return\
    \ False\n        a, _, i = self._position(x)\n        return i != len(a) and a[i]\
    \ == x\n\n    def add(self, x: T) -> bool:\n        \"Add an element and return\
    \ True if added. / O(\u221AN)\"\n        if self.size == 0:\n            self.a\
    \ = [[x]]\n            self.size = 1\n            return True\n        a, b, i\
    \ = self._position(x)\n        if i != len(a) and a[i] == x: return False\n  \
    \      a.insert(i, x)\n        self.size += 1\n        if len(a) > len(self.a)\
    \ * self.SPLIT_RATIO:\n            mid = len(a) >> 1\n            self.a[b:b+1]\
    \ = [a[:mid], a[mid:]]\n        return True\n    \n    def _pop(self, a: List[T],\
    \ b: int, i: int) -> T:\n        ans = a.pop(i)\n        self.size -= 1\n    \
    \    if not a: del self.a[b]\n        return ans\n\n    def discard(self, x: T)\
    \ -> bool:\n        \"Remove an element and return True if removed. / O(\u221A\
    N)\"\n        if self.size == 0: return False\n        a, b, i = self._position(x)\n\
    \        if i == len(a) or a[i] != x: return False\n        self._pop(a, b, i)\n\
    \        return True\n    \n    def lt(self, x: T) -> Optional[T]:\n        \"\
    Find the largest element < x, or None if it doesn't exist.\"\n        for a in\
    \ reversed(self.a):\n            if a[0] < x:\n                return a[bisect_left(a,\
    \ x) - 1]\n\n    def le(self, x: T) -> Optional[T]:\n        \"Find the largest\
    \ element <= x, or None if it doesn't exist.\"\n        for a in reversed(self.a):\n\
    \            if a[0] <= x:\n                return a[bisect_right(a, x) - 1]\n\
    \n    def gt(self, x: T) -> Optional[T]:\n        \"Find the smallest element\
    \ > x, or None if it doesn't exist.\"\n        for a in self.a:\n            if\
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
    \ len(a)\n        raise IndexError\n    \n    def index(self, x: T) -> int:\n\
    \        \"Count the number of elements < x.\"\n        ans = 0\n        for a\
    \ in self.a:\n            if a[-1] >= x:\n                return ans + bisect_left(a,\
    \ x)\n            ans += len(a)\n        return ans\n\n    def index_right(self,\
    \ x: T) -> int:\n        \"Count the number of elements <= x.\"\n        ans =\
    \ 0\n        for a in self.a:\n            if a[-1] > x:\n                return\
    \ ans + bisect_right(a, x)\n            ans += len(a)\n        return ans\n\n\
    # Translate from : https://atcoder.jp/contests/abc330/editorial/7754\nclass RangeSet:\n\
    \    def __init__(self):\n        self.TINF = 10**18 + 1  # \u5341\u5206\u5927\
    \u304D\u306A\u5024\n        self.sum = 0\n        self.st = SortedSet()\n    \
    \    self.st.add((-self.TINF, -self.TINF))\n        self.st.add((self.TINF, self.TINF))\n\
    \    \n    # [l, r) \u304C\u30AB\u30D0\u30FC\u3055\u308C\u3066\u3044\u308B\u304B\
    \n    def covered(self, l, r=None):\n        if r is None: r = l + 1\n       \
    \ assert l <= r\n        if l == r: return True\n        \n        # bisect_left\u3067\
    \u306F\u306A\u304Fupper_bound\u306E\u524D\u306E\u8981\u7D20\u3092\u53D6\u308B\n\
    \        itr = self.st.le((l, self.TINF))\n        if itr is None: return False\n\
    \        \n        range_l, range_r = itr\n        return range_l <= l and r <=\
    \ range_r\n    \n    # [l, r) \u304C\u30AB\u30D0\u30FC\u3055\u308C\u3066\u3044\
    \u308B\u306A\u3089\u30AB\u30D0\u30FC\u3057\u3066\u3044\u308B\u533A\u9593\u3092\
    \u8FD4\u3059\n    def covered_by(self, l, r=None):\n        if r is None: r =\
    \ l + 1\n        assert l <= r\n        if l == r: return (-self.TINF, -self.TINF)\n\
    \        \n        itr = self.st.le((l, self.TINF))\n        if itr is None: return\
    \ (-self.TINF, -self.TINF)\n        \n        range_l, range_r = itr\n       \
    \ if range_l <= l and r <= range_r:\n            return (range_l, range_r)\n \
    \       return (-self.TINF, -self.TINF)\n    \n    # [l, r) \u3092\u633F\u5165\
    \u3057\u3001\u5897\u5206\u3092\u8FD4\u3059\n    def insert(self, l, r=None):\n\
    \        if r is None: r = l + 1\n        assert l <= r\n        if l == r: return\
    \ 0\n        \n        itr = self.st.le((l, self.TINF))\n        if itr is None:\
    \ return 0\n        \n        range_l, range_r = itr\n        if range_l <= l\
    \ and r <= range_r: return 0\n        \n        sum_erased = 0\n        \n   \
    \     # \u5DE6\u5074\u3068\u91CD\u306A\u308B\u533A\u9593\u3092\u51E6\u7406\n \
    \       if range_l <= l <= range_r:\n            l = range_l\n            sum_erased\
    \ += range_r - range_l\n            self.st.discard(itr)\n            itr = self.st.ge((l,\
    \ -self.TINF))\n        else:\n            itr = self.st.gt(itr)\n        \n \
    \       # \u5B8C\u5168\u306B\u542B\u307E\u308C\u308B\u533A\u9593\u3092\u524A\u9664\
    \n        while itr is not None and itr[1] <= r:\n            range_l, range_r\
    \ = itr\n            sum_erased += range_r - range_l\n            self.st.discard(itr)\n\
    \            itr = self.st.ge((range_r, -self.TINF))\n        \n        # \u53F3\
    \u5074\u3068\u91CD\u306A\u308B\u533A\u9593\u3092\u51E6\u7406\n        if itr is\
    \ not None and itr[0] <= r:\n            range_l, range_r = itr\n            sum_erased\
    \ += range_r - range_l\n            r = range_r\n            self.st.discard(itr)\n\
    \        \n        self.st.add((l, r))\n        self.sum += r - l - sum_erased\n\
    \        return r - l - sum_erased\n    \n    # [l, r) \u3092\u524A\u9664\u3057\
    \u3001\u6E1B\u5C11\u91CF\u3092\u8FD4\u3059\n    def erase(self, l, r=None):\n\
    \        if r is None: r = l + 1\n        assert l <= r\n        if l == r: return\
    \ 0\n        \n        itr = self.st.le((l, self.TINF))\n        if itr is None:\
    \ return 0\n        \n        range_l, range_r = itr\n        \n        # \u5B8C\
    \u5168\u306B\u542B\u307E\u308C\u308B\u5834\u5408\n        if range_l <= l and\
    \ r <= range_r:\n            self.st.discard(itr)\n            if range_l < l:\n\
    \                self.st.add((range_l, l))\n            if r < range_r:\n    \
    \            self.st.add((r, range_r))\n            self.sum -= r - l\n      \
    \      return r - l\n        \n        ret = 0\n        \n        # \u5DE6\u5074\
    \u3068\u91CD\u306A\u308B\u533A\u9593\u3092\u51E6\u7406\n        if range_l <=\
    \ l < range_r:\n            ret += range_r - l\n            self.st.discard(itr)\n\
    \            if range_l < l:\n                self.st.add((range_l, l))\n    \
    \        itr = self.st.ge((l, -self.TINF))\n        else:\n            itr = self.st.gt(itr)\n\
    \        \n        # \u5B8C\u5168\u306B\u542B\u307E\u308C\u308B\u533A\u9593\u3092\
    \u524A\u9664\n        while itr is not None and itr[1] <= r:\n            range_l,\
    \ range_r = itr\n            ret += range_r - range_l\n            self.st.discard(itr)\n\
    \            itr = self.st.ge((range_l, -self.TINF))\n        \n        # \u53F3\
    \u5074\u3068\u91CD\u306A\u308B\u533A\u9593\u3092\u51E6\u7406\n        if itr is\
    \ not None and itr[0] < r:\n            range_l, range_r = itr\n            ret\
    \ += r - range_l\n            self.st.discard(itr)\n            self.st.add((r,\
    \ range_r))\n        \n        self.sum -= ret\n        return ret\n    \n   \
    \ def size(self):\n        return len(self.st) - 2\n    \n    def mex(self, x=0):\n\
    \        itr = self.st.le((x, self.TINF))\n        if itr is None: return x\n\
    \        \n        range_l, range_r = itr\n        if range_l <= x < range_r:\n\
    \            return range_r\n        else:\n            return x\n    \n    def\
    \ sum_all(self):\n        return self.sum\n    \n    def get(self):\n        result\
    \ = set()\n        for range_l, range_r in self.st:\n            if abs(range_l)\
    \ == self.TINF:\n                continue\n            result.add((range_l, range_r))\n\
    \        return result\n    \n    def dump(self):\n        print(\"RangeSet:\"\
    , end=\"\")\n        for range_l, range_r in sorted(self.st):\n            if\
    \ abs(range_l) == self.TINF:\n                continue\n            print(f\"\
    [{range_l},{range_r}),\", end=\"\")\n        print()\n        "
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/RamgeSet.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/RamgeSet.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/RamgeSet.py
- /library/algorithm_library/python/data-structure/RamgeSet.py.html
title: algorithm_library/python/data-structure/RamgeSet.py
---
