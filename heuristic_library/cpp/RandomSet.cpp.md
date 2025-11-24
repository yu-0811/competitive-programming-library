---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"heuristic_library/cpp/RandomSet.cpp\"\n// \u8981\u7D20\u306E\
    \u8FFD\u52A0\u3001\u524A\u9664\u3001\u30E9\u30F3\u30C0\u30E0\u53D6\u5F97\u3092\
    \ O(1) \u884C\u3046\u56FA\u5B9A\u30B5\u30A4\u30BA\u306E\u30BB\u30C3\u30C8 \n\n\
    // ---------------------------\n// \u5024\u306E\u578B\uFF08\u4F8B: int, short,\
    \ uint16_t, int16_t \u306A\u3069\uFF09\nusing ValueType = short;\n// (\u5024\u304C\
    \u53D6\u308A\u5F97\u308B) \u6700\u5927\u306E\u5024\u3002\u5024\u306E\u6709\u52B9\
    \u7BC4\u56F2\u306F 0 .. MAX_VALUE\nconstexpr int MAX_VALUE = 1020;\n// position_map\
    \ \u306B\u4F7F\u3046\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u578B\u3002-1\u3092\u4F7F\
    \u3046\u306E\u3067\u7B26\u53F7\u4ED8\u304D\u304C\u4FBF\u5229\uFF08\u4F8B: int16_t,\
    \ int32_t\uFF09\nusing IndexType = short;\n// ---------------------------\ntemplate<typename\
    \ ValT = ValueType, int MaxVal = MAX_VALUE, typename IdxT = IndexType>\nclass\
    \ RandomizedSet {\n    static_assert(MaxVal >= 0, \"MaxVal must be non-negative\"\
    );\n    static_assert(is_integral_v<ValT>, \"ValT must be an integral type\");\n\
    \    static_assert(is_signed_v<IdxT>, \"IdxT should be signed (we use -1 as sentinel)\"\
    );\npublic:\n    using value_type = ValT; using index_type = IdxT;\n    static\
    \ constexpr size_t CAP = static_cast<size_t>(MaxVal) + 1;\n    RandomizedSet()\
    \ noexcept {\n        position_map.fill(static_cast<index_type>(-1));\n      \
    \  cur_size = 0;\n    }\n\n    // add / remove / contains \u306F\u5024\u304C\u6709\
    \u52B9\u7BC4\u56F2\u5185\u304B\u3092\u30C1\u30A7\u30C3\u30AF\u3057\u307E\u3059\
    \n    bool add(value_type v) noexcept {\n        if (!is_valid_value(v)) return\
    \ false;\n        auto uv = to_unsigned_index(v);\n        if (position_map[uv]\
    \ != static_cast<index_type>(-1)) return false; // already present\n        elements[cur_size]\
    \ = v;\n        position_map[uv] = static_cast<index_type>(cur_size);\n      \
    \  ++cur_size;\n        return true;\n    }\n\n    bool remove(value_type v) noexcept\
    \ {\n        if (!is_valid_value(v)) return false;\n        auto uv = to_unsigned_index(v);\n\
    \        index_type pos = position_map[uv];\n        if (pos == static_cast<index_type>(-1))\
    \ return false; // not present\n        // swap with last\n        value_type\
    \ last = elements[cur_size - 1];\n        elements[static_cast<size_t>(pos)] =\
    \ last;\n        // \u66F4\u65B0\uFF1Alast \u306E\u4F4D\u7F6E\u3092 pos \u306B\
    \u3059\u308B\n        auto ulast = to_unsigned_index(last);\n        position_map[ulast]\
    \ = pos;\n        // clear removed\n        position_map[uv] = static_cast<index_type>(-1);\n\
    \        --cur_size;\n        return true;\n    }\n\n    value_type getRandom()\
    \ const {\n        if (cur_size == 0) throw runtime_error(\"RandomizedSet: set\
    \ is empty\");\n        unsigned idx = static_cast<unsigned>(Random::randrange(static_cast<unsigned>(cur_size)));\n\
    \        return elements[static_cast<size_t>(idx)];\n    }\n\n    size_t size()\
    \ const noexcept { return cur_size; }\n\n    bool contains(value_type v) const\
    \ noexcept {\n        if (!is_valid_value(v)) return false;\n        return position_map[to_unsigned_index(v)]\
    \ != static_cast<index_type>(-1);\n    }\n\n    void printElements() const {\n\
    \        cout << \"Elements: { \";\n        for (size_t i = 0; i < cur_size; ++i)\
    \ cout << +elements[i] << \" \";\n        cout << \"}\\n\";\n    }\n\nprivate:\n\
    \    // \u5B9F\u88C5\u88DC\u52A9: ValT \u3092\u975E\u8CA0\u306E\u914D\u5217\u30A4\
    \u30F3\u30C7\u30C3\u30AF\u30B9\u306B\u5909\u63DB\uFF08\u5B89\u5168\u306B\u30AD\
    \u30E3\u30B9\u30C8\uFF09\n    static constexpr make_unsigned_t<ValT> to_unsigned_index(ValT\
    \ v) noexcept {\n        return static_cast<make_unsigned_t<ValT>>(v);\n    }\n\
    \    // \u5024\u304C\u6709\u52B9\u304B\uFF08\u7BC4\u56F2\u30C1\u30A7\u30C3\u30AF\
    \uFF09\n    static bool is_valid_value(ValT v) noexcept {\n        if constexpr\
    \ (is_signed_v<ValT>) {\n            if (v < 0) return false;\n            return\
    \ static_cast<make_unsigned_t<ValT>>(v) <= static_cast<make_unsigned_t<int>>(MaxVal);\n\
    \        } else {\n            return static_cast<make_unsigned_t<ValT>>(v) <=\
    \ static_cast<make_unsigned_t<int>>(MaxVal);\n        }\n    }\n    // \u30C7\u30FC\
    \u30BF\n    array<value_type, CAP> elements;          // \u73FE\u5728\u8981\u7D20\
    \uFF08\u9806\u5E8F\u306F\u4EFB\u610F\uFF09\n    array<index_type, CAP> position_map;\
    \      // \u5024 -> index\uFF08\u5B58\u5728\u3057\u306A\u3044\u5834\u5408 -1\uFF09\
    \n    size_t cur_size;\n};\nusing RandSet = RandomizedSet<ValueType, MAX_VALUE,\
    \ IndexType>;\n"
  code: "// \u8981\u7D20\u306E\u8FFD\u52A0\u3001\u524A\u9664\u3001\u30E9\u30F3\u30C0\
    \u30E0\u53D6\u5F97\u3092 O(1) \u884C\u3046\u56FA\u5B9A\u30B5\u30A4\u30BA\u306E\
    \u30BB\u30C3\u30C8 \n\n// ---------------------------\n// \u5024\u306E\u578B\uFF08\
    \u4F8B: int, short, uint16_t, int16_t \u306A\u3069\uFF09\nusing ValueType = short;\n\
    // (\u5024\u304C\u53D6\u308A\u5F97\u308B) \u6700\u5927\u306E\u5024\u3002\u5024\
    \u306E\u6709\u52B9\u7BC4\u56F2\u306F 0 .. MAX_VALUE\nconstexpr int MAX_VALUE =\
    \ 1020;\n// position_map \u306B\u4F7F\u3046\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\
    \u578B\u3002-1\u3092\u4F7F\u3046\u306E\u3067\u7B26\u53F7\u4ED8\u304D\u304C\u4FBF\
    \u5229\uFF08\u4F8B: int16_t, int32_t\uFF09\nusing IndexType = short;\n// ---------------------------\n\
    template<typename ValT = ValueType, int MaxVal = MAX_VALUE, typename IdxT = IndexType>\n\
    class RandomizedSet {\n    static_assert(MaxVal >= 0, \"MaxVal must be non-negative\"\
    );\n    static_assert(is_integral_v<ValT>, \"ValT must be an integral type\");\n\
    \    static_assert(is_signed_v<IdxT>, \"IdxT should be signed (we use -1 as sentinel)\"\
    );\npublic:\n    using value_type = ValT; using index_type = IdxT;\n    static\
    \ constexpr size_t CAP = static_cast<size_t>(MaxVal) + 1;\n    RandomizedSet()\
    \ noexcept {\n        position_map.fill(static_cast<index_type>(-1));\n      \
    \  cur_size = 0;\n    }\n\n    // add / remove / contains \u306F\u5024\u304C\u6709\
    \u52B9\u7BC4\u56F2\u5185\u304B\u3092\u30C1\u30A7\u30C3\u30AF\u3057\u307E\u3059\
    \n    bool add(value_type v) noexcept {\n        if (!is_valid_value(v)) return\
    \ false;\n        auto uv = to_unsigned_index(v);\n        if (position_map[uv]\
    \ != static_cast<index_type>(-1)) return false; // already present\n        elements[cur_size]\
    \ = v;\n        position_map[uv] = static_cast<index_type>(cur_size);\n      \
    \  ++cur_size;\n        return true;\n    }\n\n    bool remove(value_type v) noexcept\
    \ {\n        if (!is_valid_value(v)) return false;\n        auto uv = to_unsigned_index(v);\n\
    \        index_type pos = position_map[uv];\n        if (pos == static_cast<index_type>(-1))\
    \ return false; // not present\n        // swap with last\n        value_type\
    \ last = elements[cur_size - 1];\n        elements[static_cast<size_t>(pos)] =\
    \ last;\n        // \u66F4\u65B0\uFF1Alast \u306E\u4F4D\u7F6E\u3092 pos \u306B\
    \u3059\u308B\n        auto ulast = to_unsigned_index(last);\n        position_map[ulast]\
    \ = pos;\n        // clear removed\n        position_map[uv] = static_cast<index_type>(-1);\n\
    \        --cur_size;\n        return true;\n    }\n\n    value_type getRandom()\
    \ const {\n        if (cur_size == 0) throw runtime_error(\"RandomizedSet: set\
    \ is empty\");\n        unsigned idx = static_cast<unsigned>(Random::randrange(static_cast<unsigned>(cur_size)));\n\
    \        return elements[static_cast<size_t>(idx)];\n    }\n\n    size_t size()\
    \ const noexcept { return cur_size; }\n\n    bool contains(value_type v) const\
    \ noexcept {\n        if (!is_valid_value(v)) return false;\n        return position_map[to_unsigned_index(v)]\
    \ != static_cast<index_type>(-1);\n    }\n\n    void printElements() const {\n\
    \        cout << \"Elements: { \";\n        for (size_t i = 0; i < cur_size; ++i)\
    \ cout << +elements[i] << \" \";\n        cout << \"}\\n\";\n    }\n\nprivate:\n\
    \    // \u5B9F\u88C5\u88DC\u52A9: ValT \u3092\u975E\u8CA0\u306E\u914D\u5217\u30A4\
    \u30F3\u30C7\u30C3\u30AF\u30B9\u306B\u5909\u63DB\uFF08\u5B89\u5168\u306B\u30AD\
    \u30E3\u30B9\u30C8\uFF09\n    static constexpr make_unsigned_t<ValT> to_unsigned_index(ValT\
    \ v) noexcept {\n        return static_cast<make_unsigned_t<ValT>>(v);\n    }\n\
    \    // \u5024\u304C\u6709\u52B9\u304B\uFF08\u7BC4\u56F2\u30C1\u30A7\u30C3\u30AF\
    \uFF09\n    static bool is_valid_value(ValT v) noexcept {\n        if constexpr\
    \ (is_signed_v<ValT>) {\n            if (v < 0) return false;\n            return\
    \ static_cast<make_unsigned_t<ValT>>(v) <= static_cast<make_unsigned_t<int>>(MaxVal);\n\
    \        } else {\n            return static_cast<make_unsigned_t<ValT>>(v) <=\
    \ static_cast<make_unsigned_t<int>>(MaxVal);\n        }\n    }\n    // \u30C7\u30FC\
    \u30BF\n    array<value_type, CAP> elements;          // \u73FE\u5728\u8981\u7D20\
    \uFF08\u9806\u5E8F\u306F\u4EFB\u610F\uFF09\n    array<index_type, CAP> position_map;\
    \      // \u5024 -> index\uFF08\u5B58\u5728\u3057\u306A\u3044\u5834\u5408 -1\uFF09\
    \n    size_t cur_size;\n};\nusing RandSet = RandomizedSet<ValueType, MAX_VALUE,\
    \ IndexType>;"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/RandomSet.cpp
  requiredBy: []
  timestamp: '2025-11-24 14:08:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/RandomSet.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/RandomSet.cpp
- /library/heuristic_library/cpp/RandomSet.cpp.html
title: heuristic_library/cpp/RandomSet.cpp
---
