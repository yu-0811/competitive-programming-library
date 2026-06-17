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
    \ to the path to import SortedSet\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),\
    \ '..')))\n\nfrom SortedSet import SortedSet\n\ndef test_init():\n    s = SortedSet([1,\
    \ 4, 3, 2, 5])\n    assert list(s) == [1, 2, 3, 4, 5]\n    s = SortedSet([1, 1,\
    \ 2, 2, 3, 3])\n    assert list(s) == [1, 2, 3]\n    s = SortedSet()\n    assert\
    \ list(s) == []\n    s = SortedSet([5, 4, 3, 2, 1])\n    assert list(s) == [1,\
    \ 2, 3, 4, 5]\n\ndef test_iter_reversed():\n    s = SortedSet([1, 2, 3, 4, 5])\n\
    \    assert list(s) == [1, 2, 3, 4, 5]\n    assert list(reversed(s)) == [5, 4,\
    \ 3, 2, 1]\n\ndef test_eq():\n    s1 = SortedSet([1, 2, 3])\n    s2 = SortedSet([3,\
    \ 2, 1])\n    s3 = SortedSet([1, 2, 4])\n    assert s1 == s2\n    assert s1 !=\
    \ s3\n    assert s1 == [1, 2, 3]\n\ndef test_len():\n    s = SortedSet([1, 2,\
    \ 3, 4, 5])\n    assert len(s) == 5\n    s.add(6)\n    assert len(s) == 6\n  \
    \  s.discard(1)\n    assert len(s) == 5\n    s.add(2) # no change\n    assert\
    \ len(s) == 5\n    s = SortedSet()\n    assert len(s) == 0\n\ndef test_repr_str():\n\
    \    s = SortedSet([1, 2, 3])\n    assert repr(s).startswith(\"SortedSet\")\n\
    \    assert str(s) == \"{1, 2, 3}\"\n    s = SortedSet()\n    assert str(s) ==\
    \ \"{}\"\n\ndef test_contains():\n    s = SortedSet([1, 3, 5, 7, 10, 20, 30])\n\
    \    assert 1 in s\n    assert 2 not in s\n    assert 7 in s\n    assert 0 not\
    \ in s\n    assert 8 not in s\n    assert 30 in s\n    assert 31 not in s\n  \
    \  s = SortedSet()\n    assert 1 not in s\n\ndef test_add():\n    s = SortedSet()\n\
    \    assert s.add(1)\n    assert list(s) == [1]\n    assert s.add(3)\n    assert\
    \ list(s) == [1, 3]\n    assert s.add(2)\n    assert list(s) == [1, 2, 3]\n  \
    \  assert not s.add(2)\n    assert list(s) == [1, 2, 3]\n    assert len(s) ==\
    \ 3\n\ndef test_discard():\n    s = SortedSet([1, 2, 3, 4, 5])\n    assert s.discard(3)\n\
    \    assert list(s) == [1, 2, 4, 5]\n    assert not s.discard(3)\n    assert list(s)\
    \ == [1, 2, 4, 5]\n    assert s.discard(1)\n    assert list(s) == [2, 4, 5]\n\
    \    assert s.discard(5)\n    assert list(s) == [2, 4]\n    assert len(s) == 2\n\
    \    s = SortedSet()\n    assert not s.discard(1)\n\ndef test_lt_le_gt_ge():\n\
    \    s = SortedSet([10, 20, 30, 40, 50])\n    assert s.lt(30) == 20\n    assert\
    \ s.le(30) == 30\n    assert s.gt(30) == 40\n    assert s.ge(30) == 30\n\n   \
    \ assert s.lt(35) == 30\n    assert s.le(35) == 30\n    assert s.gt(35) == 40\n\
    \    assert s.ge(35) == 40\n\n    assert s.lt(10) is None\n    assert s.le(10)\
    \ == 10\n    assert s.gt(50) is None\n    assert s.ge(50) == 50\n    \n    assert\
    \ s.lt(5) is None\n    assert s.le(5) is None\n    assert s.gt(55) is None\n \
    \   assert s.ge(55) is None\n\ndef test_getitem():\n    s = SortedSet([10, 20,\
    \ 30, 40, 50])\n    assert s[0] == 10\n    assert s[2] == 30\n    assert s[4]\
    \ == 50\n    assert s[-1] == 50\n    assert s[-3] == 30\n    assert s[-5] == 10\n\
    \    with pytest.raises(IndexError):\n        s[5]\n    with pytest.raises(IndexError):\n\
    \        s[-6]\n\ndef test_pop():\n    s = SortedSet([10, 20, 30, 40, 50])\n \
    \   assert s.pop(2) == 30\n    assert list(s) == [10, 20, 40, 50]\n    assert\
    \ s.pop() == 50 # pop(-1)\n    assert list(s) == [10, 20, 40]\n    assert s.pop(0)\
    \ == 10\n    assert list(s) == [20, 40]\n    assert len(s) == 2\n    with pytest.raises(IndexError):\n\
    \        s.pop(2)\n    with pytest.raises(IndexError):\n        s.pop(-3)\n\n\
    def test_index_index_right():\n    s = SortedSet([10, 20, 30, 40, 50])\n    assert\
    \ s.index(30) == 2 # count < 30\n    assert s.index_right(30) == 3 # count <=\
    \ 30\n\n    assert s.index(35) == 3\n    assert s.index_right(35) == 3\n\n   \
    \ assert s.index(5) == 0\n    assert s.index_right(5) == 0\n\n    assert s.index(55)\
    \ == 5\n    assert s.index_right(55) == 5\n\ndef test_stress():\n    s = SortedSet()\n\
    \    py_s = set()\n    for _ in range(1000):\n        val = random.randint(0,\
    \ 1000)\n        if random.random() < 0.5:\n            s.add(val)\n         \
    \   py_s.add(val)\n        else:\n            s.discard(val)\n            if val\
    \ in py_s:\n                py_s.remove(val)\n        assert list(s) == sorted(list(py_s))\n\
    \    \n    for _ in range(1000):\n        if len(s) == 0: break\n        idx =\
    \ random.randint(0, len(s) - 1)\n        val = s.pop(idx)\n        py_s_list =\
    \ sorted(list(py_s))\n        assert val == py_s_list.pop(idx)\n        py_s =\
    \ set(py_s_list)\n        assert list(s) == sorted(list(py_s))\n\ndef test_empty_set_operations():\n\
    \    s = SortedSet()\n    assert s.lt(10) is None\n    assert s.le(10) is None\n\
    \    assert s.gt(10) is None\n    assert s.ge(10) is None\n    with pytest.raises(IndexError):\n\
    \        s[0]\n    with pytest.raises(IndexError):\n        s.pop()\n\ndef test_bucket_split():\n\
    \    # Force bucket splitting by setting ratios low and adding many elements\n\
    \    original_bucket_ratio = SortedSet.BUCKET_RATIO\n    original_split_ratio\
    \ = SortedSet.SPLIT_RATIO\n    try:\n        SortedSet.BUCKET_RATIO = 1\n    \
    \    SortedSet.SPLIT_RATIO = 4\n        \n        s = SortedSet()\n        \n\
    \        initial_elements = 10\n        for i in range(initial_elements):\n  \
    \          s.add(i)\n        \n        assert list(s) == list(range(initial_elements))\n\
    \        # Check number of buckets to infer if splitting happened\n        # With\
    \ BUCKET_RATIO=1, sqrt(10/1) ~= 3 buckets initially\n        # Then adding more\
    \ elements should cause splits.\n        num_buckets_before = len(s.a)\n     \
    \   \n        # Add enough elements to trigger a split\n        # Each bucket\
    \ holds ~3-4 elements. Adding more should split one.\n        for i in range(initial_elements,\
    \ initial_elements + 20):\n            s.add(i)\n            \n        assert\
    \ list(s) == list(range(initial_elements + 20))\n        num_buckets_after = len(s.a)\n\
    \        assert num_buckets_after > num_buckets_before\n    finally:\n       \
    \ SortedSet.BUCKET_RATIO = original_bucket_ratio\n        SortedSet.SPLIT_RATIO\
    \ = original_split_ratio\n\ndef test_bucket_merge():\n    # Force bucket merging\
    \ by removing elements\n    original_bucket_ratio = SortedSet.BUCKET_RATIO\n \
    \   original_split_ratio = SortedSet.SPLIT_RATIO\n    try:\n        SortedSet.BUCKET_RATIO\
    \ = 1\n        SortedSet.SPLIT_RATIO = 4\n        \n        # Re-initialize to\
    \ control bucket sizes\n        s = SortedSet(range(100))\n        \n        num_buckets_before\
    \ = len(s.a)\n        \n        # Remove elements until buckets are empty and\
    \ get deleted\n        for i in range(100):\n            s.pop(0)\n          \
    \  \n        assert len(s) == 0\n        num_buckets_after = len(s.a)\n      \
    \  assert num_buckets_after < num_buckets_before\n        assert num_buckets_after\
    \ == 0 # Should be empty\n    finally:\n        SortedSet.BUCKET_RATIO = original_bucket_ratio\n\
    \        SortedSet.SPLIT_RATIO = original_split_ratio\n\ndef test_large_random_ops():\n\
    \    s = SortedSet()\n    py_s = set()\n    N = 5000\n    for _ in range(N):\n\
    \        op = random.randint(0, 5)\n        val = random.randint(0, N)\n     \
    \   \n        if op == 0 or op == 1: # Add\n            s.add(val)\n         \
    \   py_s.add(val)\n        elif op == 2: # Discard\n            s.discard(val)\n\
    \            py_s.discard(val)\n        elif op == 3: # Pop\n            if len(s)\
    \ > 0:\n                idx = random.randint(0, len(s) - 1)\n                popped_s\
    \ = s.pop(idx)\n                py_s_list = sorted(list(py_s))\n             \
    \   popped_py_s = py_s_list.pop(idx)\n                assert popped_s == popped_py_s\n\
    \                py_s = set(py_s_list)\n        elif op == 4: # Get item\n   \
    \          if len(s) > 0:\n                idx = random.randint(0, len(s) - 1)\n\
    \                assert s[idx] == sorted(list(py_s))[idx]\n        elif op ==\
    \ 5: # Contains\n            assert (val in s) == (val in py_s)\n\n    assert\
    \ list(s) == sorted(list(py_s))\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/test/test_SortedSet.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/test/test_SortedSet.py
layout: document
redirect_from:
- /library/tatyam_set/test/test_SortedSet.py
- /library/tatyam_set/test/test_SortedSet.py.html
title: tatyam_set/test/test_SortedSet.py
---
