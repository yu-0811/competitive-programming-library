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
    \ to the path to import SortedMultiset\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),\
    \ '..')))\n\nfrom SortedMultiset import SortedMultiset\n\ndef test_init():\n \
    \   s = SortedMultiset([1, 4, 3, 2, 5])\n    assert list(s) == [1, 2, 3, 4, 5]\n\
    \    s = SortedMultiset([1, 1, 2, 2, 3, 3])\n    assert list(s) == [1, 1, 2, 2,\
    \ 3, 3]\n    s = SortedMultiset()\n    assert list(s) == []\n    s = SortedMultiset([5,\
    \ 4, 3, 2, 1])\n    assert list(s) == [1, 2, 3, 4, 5]\n\ndef test_iter_reversed():\n\
    \    s = SortedMultiset([1, 2, 2, 3, 4, 5])\n    assert list(s) == [1, 2, 2, 3,\
    \ 4, 5]\n    assert list(reversed(s)) == [5, 4, 3, 2, 2, 1]\n\ndef test_eq():\n\
    \    s1 = SortedMultiset([1, 2, 3])\n    s2 = SortedMultiset([3, 2, 1])\n    s3\
    \ = SortedMultiset([1, 2, 4])\n    s4 = SortedMultiset([1, 2, 2, 3])\n    assert\
    \ s1 == s2\n    assert s1 != s3\n    assert s1 != s4\n    assert s1 == [1, 2,\
    \ 3]\n\ndef test_len():\n    s = SortedMultiset([1, 2, 3, 4, 5])\n    assert len(s)\
    \ == 5\n    s.add(6)\n    assert len(s) == 6\n    s.discard(1)\n    assert len(s)\
    \ == 5\n    s.add(2) # add duplicate\n    assert len(s) == 6\n    s = SortedMultiset()\n\
    \    assert len(s) == 0\n\ndef test_repr_str():\n    s = SortedMultiset([1, 2,\
    \ 2])\n    assert repr(s).startswith(\"SortedMultiset\")\n    assert str(s) ==\
    \ \"{1, 2, 2}\"\n    s = SortedMultiset()\n    assert str(s) == \"{}\"\n\ndef\
    \ test_contains():\n    s = SortedMultiset([1, 3, 5, 5, 7, 10, 20, 30])\n    assert\
    \ 1 in s\n    assert 2 not in s\n    assert 5 in s\n    assert 0 not in s\n  \
    \  assert 8 not in s\n    assert 30 in s\n    assert 31 not in s\n    s = SortedMultiset()\n\
    \    assert 1 not in s\n\ndef test_count():\n    s = SortedMultiset([1, 2, 2,\
    \ 2, 3, 3])\n    assert s.count(1) == 1\n    assert s.count(2) == 3\n    assert\
    \ s.count(3) == 2\n    assert s.count(4) == 0\n    s = SortedMultiset()\n    assert\
    \ s.count(1) == 0\n\ndef test_add():\n    s = SortedMultiset()\n    s.add(1)\n\
    \    assert list(s) == [1]\n    s.add(3)\n    assert list(s) == [1, 3]\n    s.add(2)\n\
    \    assert list(s) == [1, 2, 3]\n    s.add(2)\n    assert list(s) == [1, 2, 2,\
    \ 3]\n    assert len(s) == 4\n\ndef test_discard():\n    s = SortedMultiset([1,\
    \ 2, 2, 3, 4, 5])\n    assert s.discard(2)\n    assert list(s) == [1, 2, 3, 4,\
    \ 5]\n    assert s.discard(2)\n    assert list(s) == [1, 3, 4, 5]\n    assert\
    \ not s.discard(2)\n    assert list(s) == [1, 3, 4, 5]\n    assert s.discard(1)\n\
    \    assert list(s) == [3, 4, 5]\n    assert s.discard(5)\n    assert list(s)\
    \ == [3, 4]\n    assert len(s) == 2\n    s = SortedMultiset()\n    assert not\
    \ s.discard(1)\n\ndef test_lt_le_gt_ge():\n    s = SortedMultiset([10, 20, 30,\
    \ 30, 40, 50])\n    assert s.lt(30) == 20\n    assert s.le(30) == 30\n    assert\
    \ s.gt(30) == 40\n    assert s.ge(30) == 30\n\n    assert s.lt(35) == 30\n   \
    \ assert s.le(35) == 30\n    assert s.gt(35) == 40\n    assert s.ge(35) == 40\n\
    \n    assert s.lt(10) is None\n    assert s.le(10) == 10\n    assert s.gt(50)\
    \ is None\n    assert s.ge(50) == 50\n    \n    assert s.lt(5) is None\n    assert\
    \ s.le(5) is None\n    assert s.gt(55) is None\n    assert s.ge(55) is None\n\n\
    def test_getitem():\n    s = SortedMultiset([10, 20, 30, 30, 40, 50])\n    assert\
    \ s[0] == 10\n    assert s[2] == 30\n    assert s[3] == 30\n    assert s[5] ==\
    \ 50\n    assert s[-1] == 50\n    assert s[-3] == 30\n    assert s[-6] == 10\n\
    \    with pytest.raises(IndexError):\n        s[6]\n    with pytest.raises(IndexError):\n\
    \        s[-7]\n\ndef test_pop():\n    s = SortedMultiset([10, 20, 30, 30, 40,\
    \ 50])\n    assert s.pop(2) == 30\n    assert list(s) == [10, 20, 30, 40, 50]\n\
    \    assert s.pop() == 50 # pop(-1)\n    assert list(s) == [10, 20, 30, 40]\n\
    \    assert s.pop(0) == 10\n    assert list(s) == [20, 30, 40]\n    assert len(s)\
    \ == 3\n    with pytest.raises(IndexError):\n        s.pop(3)\n    with pytest.raises(IndexError):\n\
    \        s.pop(-4)\n\ndef test_index_index_right():\n    s = SortedMultiset([10,\
    \ 20, 30, 30, 40, 50])\n    assert s.index(30) == 2 # count < 30\n    assert s.index_right(30)\
    \ == 4 # count <= 30\n\n    assert s.index(35) == 4\n    assert s.index_right(35)\
    \ == 4\n\n    assert s.index(5) == 0\n    assert s.index_right(5) == 0\n\n   \
    \ assert s.index(55) == 6\n    assert s.index_right(55) == 6\n\ndef test_stress():\n\
    \    s = SortedMultiset()\n    py_s = []\n    for _ in range(1000):\n        val\
    \ = random.randint(0, 1000)\n        if random.random() < 0.5:\n            s.add(val)\n\
    \            py_s.append(val)\n        else:\n            if s.discard(val):\n\
    \                py_s.remove(val)\n        py_s.sort()\n        assert list(s)\
    \ == py_s\n    \n    for _ in range(1000):\n        if len(s) == 0: break\n  \
    \      idx = random.randint(0, len(s) - 1)\n        val = s.pop(idx)\n       \
    \ assert val == py_s.pop(idx)\n        assert list(s) == py_s\n\ndef test_empty_set_operations():\n\
    \    s = SortedMultiset()\n    assert s.lt(10) is None\n    assert s.le(10) is\
    \ None\n    assert s.gt(10) is None\n    assert s.ge(10) is None\n    with pytest.raises(IndexError):\n\
    \        s[0]\n    with pytest.raises(IndexError):\n        s.pop()\n\ndef test_bucket_split():\n\
    \    original_bucket_ratio = SortedMultiset.BUCKET_RATIO\n    original_split_ratio\
    \ = SortedMultiset.SPLIT_RATIO\n    try:\n        SortedMultiset.BUCKET_RATIO\
    \ = 1\n        SortedMultiset.SPLIT_RATIO = 4\n        \n        s = SortedMultiset()\n\
    \        \n        initial_elements = 10\n        for i in range(initial_elements):\n\
    \            s.add(i)\n        \n        assert list(s) == list(range(initial_elements))\n\
    \        num_buckets_before = len(s.a)\n        \n        for i in range(initial_elements,\
    \ initial_elements + 20):\n            s.add(i)\n            \n        assert\
    \ list(s) == list(range(initial_elements + 20))\n        num_buckets_after = len(s.a)\n\
    \        assert num_buckets_after > num_buckets_before\n    finally:\n       \
    \ SortedMultiset.BUCKET_RATIO = original_bucket_ratio\n        SortedMultiset.SPLIT_RATIO\
    \ = original_split_ratio\n\ndef test_bucket_merge():\n    original_bucket_ratio\
    \ = SortedMultiset.BUCKET_RATIO\n    original_split_ratio = SortedMultiset.SPLIT_RATIO\n\
    \    try:\n        SortedMultiset.BUCKET_RATIO = 1\n        SortedMultiset.SPLIT_RATIO\
    \ = 4\n        \n        s = SortedMultiset(range(100))\n        \n        num_buckets_before\
    \ = len(s.a)\n        \n        for _ in range(100):\n            s.pop(0)\n \
    \           \n        assert len(s) == 0\n        num_buckets_after = len(s.a)\n\
    \        assert num_buckets_after < num_buckets_before\n        assert num_buckets_after\
    \ == 0\n    finally:\n        SortedMultiset.BUCKET_RATIO = original_bucket_ratio\n\
    \        SortedMultiset.SPLIT_RATIO = original_split_ratio\n\ndef test_large_random_ops():\n\
    \    s = SortedMultiset()\n    py_s = []\n    N = 5000\n    for _ in range(N):\n\
    \        op = random.randint(0, 6)\n        val = random.randint(0, N)\n     \
    \   \n        if op == 0 or op == 1: # Add\n            s.add(val)\n         \
    \   py_s.append(val)\n        elif op == 2: # Discard\n            if s.discard(val):\n\
    \                py_s.remove(val)\n        elif op == 3: # Pop\n            if\
    \ len(s) > 0:\n                py_s.sort()\n                idx = random.randint(0,\
    \ len(s) - 1)\n                popped_s = s.pop(idx)\n                popped_py_s\
    \ = py_s.pop(idx)\n                assert popped_s == popped_py_s\n        elif\
    \ op == 4: # Get item\n             if len(s) > 0:\n                py_s.sort()\n\
    \                idx = random.randint(0, len(s) - 1)\n                assert s[idx]\
    \ == py_s[idx]\n        elif op == 5: # Contains\n            assert (val in s)\
    \ == (val in py_s)\n        elif op == 6: # Count\n            py_s.sort()\n \
    \           assert s.count(val) == py_s.count(val)\n\n    py_s.sort()\n    assert\
    \ list(s) == py_s\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/test/test_SortedMultiset.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/test/test_SortedMultiset.py
layout: document
redirect_from:
- /library/tatyam_set/test/test_SortedMultiset.py
- /library/tatyam_set/test/test_SortedMultiset.py.html
title: tatyam_set/test/test_SortedMultiset.py
---
