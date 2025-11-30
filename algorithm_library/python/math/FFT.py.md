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
    - https://github.com/atcoder/ac-library/blob/master/document_ja/convolution.md
    - https://github.com/shakayami/ACL-for-python/blob/master/convolution.py
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\nshakayami \u88FD ACL \u3092\u305D\u306E\u307E\u307E\u7A83\u76D7\n\
    https://github.com/shakayami/ACL-for-python/blob/master/convolution.py\n\u672C\
    \u5BB6ACL\u30C9\u30AD\u30E5\u30E1\u30F3\u30C8 : https://github.com/atcoder/ac-library/blob/master/document_ja/convolution.md\n\
    \"\"\"\n\nclass FFT():\n    def primitive_root_constexpr(self,m):\n        if\
    \ m==2:return 1\n        if m==167772161:return 3\n        if m==469762049:return\
    \ 3\n        if m==754974721:return 11\n        if m==998244353:return 3\n   \
    \     divs=[0]*20\n        divs[0]=2\n        cnt=1\n        x=(m-1)//2\n    \
    \    while(x%2==0):x//=2\n        i=3\n        while(i*i<=x):\n            if\
    \ (x%i==0):\n                divs[cnt]=i\n                cnt+=1\n           \
    \     while(x%i==0):\n                    x//=i\n            i+=2\n        if\
    \ x>1:\n            divs[cnt]=x\n            cnt+=1\n        g=2\n        while(1):\n\
    \            ok=True\n            for i in range(cnt):\n                if pow(g,(m-1)//divs[i],m)==1:\n\
    \                    ok=False\n                    break\n            if ok:\n\
    \                return g\n            g+=1\n    def bsf(self,x):\n        res=0\n\
    \        while(x%2==0):\n            res+=1\n            x//=2\n        return\
    \ res\n    rank2=0\n    root=[]\n    iroot=[]\n    rate2=[]\n    irate2=[]\n \
    \   rate3=[]\n    irate3=[]\n    \n    def __init__(self,MOD):\n        self.mod=MOD\n\
    \        self.g=self.primitive_root_constexpr(self.mod)\n        self.rank2=self.bsf(self.mod-1)\n\
    \        self.root=[0 for i in range(self.rank2+1)]\n        self.iroot=[0 for\
    \ i in range(self.rank2+1)]\n        self.rate2=[0 for i in range(self.rank2)]\n\
    \        self.irate2=[0 for i in range(self.rank2)]\n        self.rate3=[0 for\
    \ i in range(self.rank2-1)]\n        self.irate3=[0 for i in range(self.rank2-1)]\n\
    \        self.root[self.rank2]=pow(self.g,(self.mod-1)>>self.rank2,self.mod)\n\
    \        self.iroot[self.rank2]=pow(self.root[self.rank2],self.mod-2,self.mod)\n\
    \        for i in range(self.rank2-1,-1,-1):\n            self.root[i]=(self.root[i+1]**2)%self.mod\n\
    \            self.iroot[i]=(self.iroot[i+1]**2)%self.mod\n        prod=1;iprod=1\n\
    \        for i in range(self.rank2-1):\n            self.rate2[i]=(self.root[i+2]*prod)%self.mod\n\
    \            self.irate2[i]=(self.iroot[i+2]*iprod)%self.mod\n            prod=(prod*self.iroot[i+2])%self.mod\n\
    \            iprod=(iprod*self.root[i+2])%self.mod\n        prod=1;iprod=1\n \
    \       for i in range(self.rank2-2):\n            self.rate3[i]=(self.root[i+3]*prod)%self.mod\n\
    \            self.irate3[i]=(self.iroot[i+3]*iprod)%self.mod\n            prod=(prod*self.iroot[i+3])%self.mod\n\
    \            iprod=(iprod*self.root[i+3])%self.mod\n    def butterfly(self,a):\n\
    \        n=len(a)\n        h=(n-1).bit_length()\n        \n        LEN=0\n   \
    \     while(LEN<h):\n            if (h-LEN==1):\n                p=1<<(h-LEN-1)\n\
    \                rot=1\n                for s in range(1<<LEN):\n            \
    \        offset=s<<(h-LEN)\n                    for i in range(p):\n         \
    \               l=a[i+offset]\n                        r=a[i+offset+p]*rot\n \
    \                       a[i+offset]=(l+r)%self.mod\n                        a[i+offset+p]=(l-r)%self.mod\n\
    \                    rot*=self.rate2[(~s & -~s).bit_length()-1]\n            \
    \        rot%=self.mod\n                LEN+=1\n            else:\n          \
    \      p=1<<(h-LEN-2)\n                rot=1\n                imag=self.root[2]\n\
    \                for s in range(1<<LEN):\n                    rot2=(rot*rot)%self.mod\n\
    \                    rot3=(rot2*rot)%self.mod\n                    offset=s<<(h-LEN)\n\
    \                    for i in range(p):\n                        a0=a[i+offset]\n\
    \                        a1=a[i+offset+p]*rot\n                        a2=a[i+offset+2*p]*rot2\n\
    \                        a3=a[i+offset+3*p]*rot3\n                        a1na3imag=(a1-a3)%self.mod*imag\n\
    \                        a[i+offset]=(a0+a2+a1+a3)%self.mod\n                \
    \        a[i+offset+p]=(a0+a2-a1-a3)%self.mod\n                        a[i+offset+2*p]=(a0-a2+a1na3imag)%self.mod\n\
    \                        a[i+offset+3*p]=(a0-a2-a1na3imag)%self.mod\n        \
    \            rot*=self.rate3[(~s & -~s).bit_length()-1]\n                    rot%=self.mod\n\
    \                LEN+=2\n                \n    def butterfly_inv(self,a):\n  \
    \      n=len(a)\n        h=(n-1).bit_length()\n        LEN=h\n        while(LEN):\n\
    \            if (LEN==1):\n                p=1<<(h-LEN)\n                irot=1\n\
    \                for s in range(1<<(LEN-1)):\n                    offset=s<<(h-LEN+1)\n\
    \                    for i in range(p):\n                        l=a[i+offset]\n\
    \                        r=a[i+offset+p]\n                        a[i+offset]=(l+r)%self.mod\n\
    \                        a[i+offset+p]=(l-r)*irot%self.mod\n                 \
    \   irot*=self.irate2[(~s & -~s).bit_length()-1]\n                    irot%=self.mod\n\
    \                LEN-=1\n            else:\n                p=1<<(h-LEN)\n   \
    \             irot=1\n                iimag=self.iroot[2]\n                for\
    \ s in range(1<<(LEN-2)):\n                    irot2=(irot*irot)%self.mod\n  \
    \                  irot3=(irot*irot2)%self.mod\n                    offset=s<<(h-LEN+2)\n\
    \                    for i in range(p):\n                        a0=a[i+offset]\n\
    \                        a1=a[i+offset+p]\n                        a2=a[i+offset+2*p]\n\
    \                        a3=a[i+offset+3*p]\n                        a2na3iimag=(a2-a3)*iimag%self.mod\n\
    \                        a[i+offset]=(a0+a1+a2+a3)%self.mod\n                \
    \        a[i+offset+p]=(a0-a1+a2na3iimag)*irot%self.mod\n                    \
    \    a[i+offset+2*p]=(a0+a1-a2-a3)*irot2%self.mod\n                        a[i+offset+3*p]=(a0-a1-a2na3iimag)*irot3%self.mod\n\
    \                    irot*=self.irate3[(~s & -~s).bit_length()-1]\n          \
    \          irot%=self.mod\n                LEN-=2\n                \n    \n  \
    \  def convolution(self, a : list[int], b : list[int]) -> list[int]:\n       \
    \ \"\"\"\n        res[i] = \u03A3_{j=0}^{i} a[j]b[i-j] (0-indexed)\n        \u308F\
    \u304B\u308A\u3084\u3059\u304F\u3044\u3046\u3068\u3001\u30A4\u30F3\u30C7\u30C3\
    \u30AF\u30B9\u306E\u548C\u304C i \u306B\u306A\u308B\u3088\u3046\u306A a, b \u306E\
    \u7A4D\u306E\u7DCF\u548C\n        ex. a = [1, 2, 3], b = [4, 5, 6]\n        res\
    \ = [1*4, 1*5 + 2*4, 1*6 + 2*5 + 3*4, 2*6 + 3*5, 3*6] \n        = [4, 13, 28,\
    \ 27, 18]\n        (\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u3067\u3044\u3046\u3068\
    \u3001res[0] = a[0]*b[0], res[1] = a[0]*b[1] + a[1]*b[0], ...)\n        \n   \
    \     \u6642\u9593\u8A08\u7B97\u91CF\n        L = |a| + |b| \u3068\u3057\u3066\
    \u3001O(L log L + log mod)\n        \"\"\"\n        n=len(a);m=len(b)\n      \
    \  if not(a) or not(b):\n            return []\n        if min(n,m)<=40:\n   \
    \         res=[0]*(n+m-1)\n            for i in range(n):\n                for\
    \ j in range(m):\n                    res[i+j]+=a[i]*b[j]\n                  \
    \  res[i+j]%=self.mod\n            return res\n        z=1<<((n+m-2).bit_length())\n\
    \        a=a+[0]*(z-n)\n        b=b+[0]*(z-m)\n        self.butterfly(a)\n   \
    \     self.butterfly(b)\n        c=[(a[i]*b[i])%self.mod for i in range(z)]\n\
    \        self.butterfly_inv(c)\n        iz=pow(z,self.mod-2,self.mod)\n      \
    \  for i in range(n+m-1):\n            c[i]=(c[i]*iz)%self.mod\n        return\
    \ c[:n+m-1]"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/FFT.py
  requiredBy: []
  timestamp: '2025-11-30 11:50:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/FFT.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/FFT.py
- /library/algorithm_library/python/math/FFT.py.html
title: algorithm_library/python/math/FFT.py
---
