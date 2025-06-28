# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
        return True
    
    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True
    
    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

# Translate from : https://atcoder.jp/contests/abc330/editorial/7754
class RangeSet:
    def __init__(self):
        self.TINF = 10**18 + 1  # 十分大きな値
        self.sum = 0
        self.st = SortedSet()
        self.st.add((-self.TINF, -self.TINF))
        self.st.add((self.TINF, self.TINF))
    
    # [l, r) がカバーされているか
    def covered(self, l, r=None):
        if r is None: r = l + 1
        assert l <= r
        if l == r: return True
        
        # bisect_leftではなくupper_boundの前の要素を取る
        itr = self.st.le((l, self.TINF))
        if itr is None: return False
        
        range_l, range_r = itr
        return range_l <= l and r <= range_r
    
    # [l, r) がカバーされているならカバーしている区間を返す
    def covered_by(self, l, r=None):
        if r is None: r = l + 1
        assert l <= r
        if l == r: return (-self.TINF, -self.TINF)
        
        itr = self.st.le((l, self.TINF))
        if itr is None: return (-self.TINF, -self.TINF)
        
        range_l, range_r = itr
        if range_l <= l and r <= range_r:
            return (range_l, range_r)
        return (-self.TINF, -self.TINF)
    
    # [l, r) を挿入し、増分を返す
    def insert(self, l, r=None):
        if r is None: r = l + 1
        assert l <= r
        if l == r: return 0
        
        itr = self.st.le((l, self.TINF))
        if itr is None: return 0
        
        range_l, range_r = itr
        if range_l <= l and r <= range_r: return 0
        
        sum_erased = 0
        
        # 左側と重なる区間を処理
        if range_l <= l <= range_r:
            l = range_l
            sum_erased += range_r - range_l
            self.st.discard(itr)
            itr = self.st.ge((l, -self.TINF))
        else:
            itr = self.st.gt(itr)
        
        # 完全に含まれる区間を削除
        while itr is not None and itr[1] <= r:
            range_l, range_r = itr
            sum_erased += range_r - range_l
            self.st.discard(itr)
            itr = self.st.ge((range_r, -self.TINF))
        
        # 右側と重なる区間を処理
        if itr is not None and itr[0] <= r:
            range_l, range_r = itr
            sum_erased += range_r - range_l
            r = range_r
            self.st.discard(itr)
        
        self.st.add((l, r))
        self.sum += r - l - sum_erased
        return r - l - sum_erased
    
    # [l, r) を削除し、減少量を返す
    def erase(self, l, r=None):
        if r is None: r = l + 1
        assert l <= r
        if l == r: return 0
        
        itr = self.st.le((l, self.TINF))
        if itr is None: return 0
        
        range_l, range_r = itr
        
        # 完全に含まれる場合
        if range_l <= l and r <= range_r:
            self.st.discard(itr)
            if range_l < l:
                self.st.add((range_l, l))
            if r < range_r:
                self.st.add((r, range_r))
            self.sum -= r - l
            return r - l
        
        ret = 0
        
        # 左側と重なる区間を処理
        if range_l <= l < range_r:
            ret += range_r - l
            self.st.discard(itr)
            if range_l < l:
                self.st.add((range_l, l))
            itr = self.st.ge((l, -self.TINF))
        else:
            itr = self.st.gt(itr)
        
        # 完全に含まれる区間を削除
        while itr is not None and itr[1] <= r:
            range_l, range_r = itr
            ret += range_r - range_l
            self.st.discard(itr)
            itr = self.st.ge((range_l, -self.TINF))
        
        # 右側と重なる区間を処理
        if itr is not None and itr[0] < r:
            range_l, range_r = itr
            ret += r - range_l
            self.st.discard(itr)
            self.st.add((r, range_r))
        
        self.sum -= ret
        return ret
    
    def size(self):
        return len(self.st) - 2
    
    def mex(self, x=0):
        itr = self.st.le((x, self.TINF))
        if itr is None: return x
        
        range_l, range_r = itr
        if range_l <= x < range_r:
            return range_r
        else:
            return x
    
    def sum_all(self):
        return self.sum
    
    def get(self):
        result = set()
        for range_l, range_r in self.st:
            if abs(range_l) == self.TINF:
                continue
            result.add((range_l, range_r))
        return result
    
    def dump(self):
        print("RangeSet:", end="")
        for range_l, range_r in sorted(self.st):
            if abs(range_l) == self.TINF:
                continue
            print(f"[{range_l},{range_r}),", end="")
        print()
        