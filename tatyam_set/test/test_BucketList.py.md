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
  code: "import pytest\nimport sys\nimport os\nimport random\n\n# Add the parent directory\
    \ to the path to import BucketList\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),\
    \ '..')))\n\nfrom BucketList import BucketList\n\ndef test_init():\n    bl = BucketList([1,\
    \ 2, 3, 4, 5])\n    assert list(bl) == [1, 2, 3, 4, 5]\n    bl = BucketList(\"\
    hello\")\n    assert list(bl) == ['h', 'e', 'l', 'l', 'o']\n    bl = BucketList()\n\
    \    assert list(bl) == []\n\ndef test_iter_reversed():\n    data = [1, 2, 3,\
    \ 4, 5]\n    bl = BucketList(data)\n    assert list(bl) == data\n    assert list(reversed(bl))\
    \ == list(reversed(data))\n\ndef test_eq():\n    bl1 = BucketList([1, 2, 3])\n\
    \    bl2 = BucketList([1, 2, 3])\n    bl3 = BucketList([1, 2, 4])\n    l1 = [1,\
    \ 2, 3]\n    assert bl1 == bl2\n    assert bl1 != bl3\n    assert bl1 == l1\n\n\
    def test_len():\n    data = [1, 2, 3, 4, 5]\n    bl = BucketList(data)\n    assert\
    \ len(bl) == 5\n    bl.append(6)\n    assert len(bl) == 6\n    bl.pop()\n    assert\
    \ len(bl) == 5\n    bl.clear()\n    assert len(bl) == 0\n\ndef test_repr_str():\n\
    \    bl = BucketList([1, 2, 3])\n    assert repr(bl).startswith(\"BucketList\"\
    )\n    assert str(bl) == \"[1, 2, 3]\"\n    bl = BucketList()\n    assert str(bl)\
    \ == \"[]\"\n\ndef test_contains():\n    bl = BucketList([1, 3, 5, 7, 10, 20,\
    \ 30])\n    assert 1 in bl\n    assert 2 not in bl\n    assert 30 in bl\n    assert\
    \ 31 not in bl\n    bl = BucketList()\n    assert 1 not in bl\n\ndef test_insert():\n\
    \    bl = BucketList()\n    bl.insert(0, 10)\n    assert list(bl) == [10]\n  \
    \  bl.insert(0, 5)\n    assert list(bl) == [5, 10]\n    bl.insert(1, 7)\n    assert\
    \ list(bl) == [5, 7, 10]\n    bl.insert(3, 12)\n    assert list(bl) == [5, 7,\
    \ 10, 12]\n    bl.insert(-1, 11)\n    assert list(bl) == [5, 7, 10, 11, 12]\n\
    \    with pytest.raises(IndexError):\n        bl.insert(100, 1)\n    with pytest.raises(IndexError):\n\
    \        bl.insert(-100, 1)\n\ndef test_append_extend():\n    bl = BucketList()\n\
    \    bl.append(1)\n    assert list(bl) == [1]\n    bl.append(2)\n    assert list(bl)\
    \ == [1, 2]\n    bl.extend([3, 4, 5])\n    assert list(bl) == [1, 2, 3, 4, 5]\n\
    \    bl.extend([])\n    assert list(bl) == [1, 2, 3, 4, 5]\n\ndef test_getitem():\n\
    \    bl = BucketList([10, 20, 30, 40, 50])\n    assert bl[0] == 10\n    assert\
    \ bl[2] == 30\n    assert bl[4] == 50\n    assert bl[-1] == 50\n    assert bl[-3]\
    \ == 30\n    assert bl[-5] == 10\n    with pytest.raises(IndexError):\n      \
    \  bl[5]\n    with pytest.raises(IndexError):\n        bl[-6]\n\ndef test_pop():\n\
    \    bl = BucketList([10, 20, 30, 40, 50])\n    assert bl.pop(2) == 30\n    assert\
    \ list(bl) == [10, 20, 40, 50]\n    assert bl.pop() == 50\n    assert list(bl)\
    \ == [10, 20, 40]\n    assert bl.pop(0) == 10\n    assert list(bl) == [20, 40]\n\
    \    assert len(bl) == 2\n    with pytest.raises(IndexError):\n        bl.pop(2)\n\
    \    with pytest.raises(IndexError):\n        bl.pop(-3)\n\ndef test_count():\n\
    \    bl = BucketList([1, 2, 2, 3, 2, 4])\n    assert bl.count(1) == 1\n    assert\
    \ bl.count(2) == 3\n    assert bl.count(5) == 0\n\ndef test_index():\n    bl =\
    \ BucketList([1, 2, 3, 2, 1])\n    assert bl.index(1) == 0\n    assert bl.index(2)\
    \ == 1\n    assert bl.index(3) == 2\n    with pytest.raises(ValueError):\n   \
    \     bl.index(4)\n\ndef test_remove():\n    bl = BucketList([1, 2, 3, 2, 1])\n\
    \    bl.remove(2)\n    assert list(bl) == [1, 3, 2, 1]\n    bl.remove(1)\n   \
    \ assert list(bl) == [3, 2, 1]\n    with pytest.raises(ValueError):\n        bl.remove(4)\n\
    \ndef test_clear():\n    bl = BucketList([1, 2, 3])\n    bl.clear()\n    assert\
    \ len(bl) == 0\n    assert list(bl) == []\n    assert bl.a == []\n\ndef test_reverse():\n\
    \    data = [1, 2, 3, 4, 5, 6]\n    bl = BucketList(data)\n    bl.reverse()\n\
    \    data.reverse()\n    assert list(bl) == data\n    bl.reverse()\n    data.reverse()\n\
    \    assert list(bl) == data\n\ndef test_copy():\n    bl1 = BucketList([1, 2,\
    \ 3])\n    bl2 = bl1.copy()\n    assert bl1 == bl2\n    assert bl1 is not bl2\n\
    \    bl2.append(4)\n    assert list(bl1) == [1, 2, 3]\n    assert list(bl2) ==\
    \ [1, 2, 3, 4]\n\ndef test_empty_list_operations():\n    bl = BucketList()\n \
    \   with pytest.raises(IndexError):\n        bl[0]\n    with pytest.raises(IndexError):\n\
    \        bl.pop()\n    with pytest.raises(ValueError):\n        bl.index(1)\n\
    \    with pytest.raises(ValueError):\n        bl.remove(1)\n    assert bl.count(1)\
    \ == 0\n    assert (1 in bl) is False\n\ndef test_bucket_split_and_merge():\n\
    \    original_bucket_ratio = BucketList.BUCKET_RATIO\n    original_split_ratio\
    \ = BucketList.SPLIT_RATIO\n    try:\n        BucketList.BUCKET_RATIO = 1\n  \
    \      BucketList.SPLIT_RATIO = 4\n        \n        bl = BucketList()\n     \
    \   \n        # Test split\n        num_buckets_before = len(bl.a)\n        for\
    \ i in range(30):\n            bl.append(i)\n        num_buckets_after = len(bl.a)\n\
    \        assert num_buckets_after > num_buckets_before\n        assert list(bl)\
    \ == list(range(30))\n\n        # Test merge\n        num_buckets_before = len(bl.a)\n\
    \        for _ in range(30):\n            bl.pop()\n        num_buckets_after\
    \ = len(bl.a)\n        assert num_buckets_after < num_buckets_before\n       \
    \ assert len(bl) == 0\n        assert num_buckets_after == 0\n\n    finally:\n\
    \        BucketList.BUCKET_RATIO = original_bucket_ratio\n        BucketList.SPLIT_RATIO\
    \ = original_split_ratio\n\ndef test_large_random_ops():\n    bl = BucketList()\n\
    \    py_l = []\n    N = 2000\n    for _ in range(N):\n        op = random.randint(0,\
    \ 8)\n        \n        if op == 0: # append\n            val = random.randint(0,\
    \ N)\n            bl.append(val)\n            py_l.append(val)\n        elif op\
    \ == 1: # insert\n            val = random.randint(0, N)\n            idx = random.randint(0,\
    \ len(py_l))\n            bl.insert(idx, val)\n            py_l.insert(idx, val)\n\
    \        elif op == 2: # pop\n            if py_l:\n                idx = random.randint(0,\
    \ len(py_l) - 1)\n                assert bl.pop(idx) == py_l.pop(idx)\n      \
    \  elif op == 3: # getitem\n             if py_l:\n                idx = random.randint(0,\
    \ len(py_l) - 1)\n                assert bl[idx] == py_l[idx]\n        elif op\
    \ == 4: # contains\n            val = random.randint(0, N)\n            assert\
    \ (val in bl) == (val in py_l)\n        elif op == 5: # count\n            val\
    \ = random.randint(0, N)\n            assert bl.count(val) == py_l.count(val)\n\
    \        elif op == 6: # remove\n            if py_l:\n                val = random.choice(py_l)\n\
    \                bl.remove(val)\n                py_l.remove(val)\n        elif\
    \ op == 7: # index\n            if py_l:\n                val = random.choice(py_l)\n\
    \                assert bl.index(val) == py_l.index(val)\n        elif op == 8:\
    \ # reverse\n            bl.reverse()\n            py_l.reverse()\n\n    assert\
    \ list(bl) == py_l\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/test/test_BucketList.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/test/test_BucketList.py
layout: document
redirect_from:
- /library/tatyam_set/test/test_BucketList.py
- /library/tatyam_set/test/test_BucketList.py.html
title: tatyam_set/test/test_BucketList.py
---
