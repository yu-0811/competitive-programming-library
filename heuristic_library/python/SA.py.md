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
  code: "import sys\ndef input():return sys.stdin.readline().rstrip()\ndef ii(): return\
    \ int(input())\ndef ms(): return map(int, input().split())\ndef li(): return list(map(int,input().split()))\n\
    def print_err(*args): print(*args,file=sys.stderr)\nfrom random import randrange,randint,random\n\
    from time import time\nstart = time()\n\nfrom math import exp\n# \u30D1\u30E9\u30E1\
    \u30FC\u30BF ##############################\nstart_temp = 500\nend_temp = 10\n\
    time_limit = 1.85 # \u5358\u4F4D : s\n###########################################\n\
    \n# \u7DDA\u5F62\u6E29\u5EA6\u7BA1\u7406\ndef linear_temp(SA_start_time : float,\
    \ now_time : float) -> float:\n  return start_temp - (start_temp - end_temp) *\
    \ (now_time - SA_start_time) / time_limit\n\n# \u9077\u79FB\u78BA\u7387\u95A2\u6570\
    \n# \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\ndef calc_prob_maximize(now_score,\
    \ next_score, temp) -> float:\n  return 1 if now_score < next_score else exp((now_score\
    \ - next_score) / temp)\n\n# \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\
    \ndef calc_prob_minimize(now_score, next_score, temp) -> float:\n  return 1 if\
    \ now_score > next_score else exp((next_score - now_score) / temp)\n\n# \u30B0\
    \u30ED\u30FC\u30D0\u30EB\u5909\u6570 #########################\n\n##########################################\n\
    \ndef calc_score():\n\n  return\n\ndef initialize_score():\n\n  return\n\n# \u8FD1\
    \u508D\u751F\u6210 + \u30B9\u30B3\u30A2\u8A08\u7B97 + \u53D7\u5BB9\u5224\u5B9A\
    \ -> \u65B0\u3057\u3044\u30B9\u30B3\u30A2\u3092\u8FD4\u3059\ndef generate_neighbor(now_score\
    \ : int|float, temp : float):\n  # \u8FD1\u508D\u751F\u6210 ######################\n\
    \n  ################################\n  # \u30B9\u30B3\u30A2\u8A08\u7B97 ###################\n\
    \  next_score = \n  if (calc_prob_maximize(now_score, next_score, temp) > random()):\
    \ # \u53D7\u5BB9\u3059\u308B\n    # \u5FC5\u8981\u3067\u3042\u308C\u3070\u72B6\
    \u614B\u3092\u66F4\u65B0 ######\n    \n    ###############################\n \
    \   return next_score\n  else: # \u53D7\u5BB9\u3057\u306A\u3044\n    # \u72B6\u614B\
    \u3092\u5143\u306B\u623B\u3059 #############\n\n    ##############################\n\
    \    return now_score\n  \ndef SA():\n  SA_start_time = time()\n  iter = -1\n\
    \  temp = start_temp\n  # \u30B9\u30B3\u30A2\u306E\u521D\u671F\u5316\n  now_score\
    \ = initialize_score()\n  while True:\n    if (iter%500 == 0):\n      now_time\
    \ = time()\n      if (now_time - start > time_limit):\n        break\n      temp\
    \ = linear_temp(SA_start_time, now_time)\n    now_score = generate_neighbor(now_score,\
    \ temp)\n    iter += 1\n  print(\"SA DONE\", iter, file=sys.stderr)\n\nSA()\n\n\
    # \u51FA\u529B ############################\n\n##################################"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/python/SA.py
  requiredBy: []
  timestamp: '2025-11-13 20:32:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/python/SA.py
layout: document
redirect_from:
- /library/heuristic_library/python/SA.py
- /library/heuristic_library/python/SA.py.html
title: heuristic_library/python/SA.py
---
