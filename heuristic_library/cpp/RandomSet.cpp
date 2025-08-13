// 要素の追加、削除、ランダム取得を O(1) 行う固定サイズのセット 

// ---------------------------
// 値の型（例: int, short, uint16_t, int16_t など）
using ValueType = short;
// (値が取り得る) 最大の値。値の有効範囲は 0 .. MAX_VALUE
constexpr int MAX_VALUE = 1020;
// position_map に使うインデックス型。-1を使うので符号付きが便利（例: int16_t, int32_t）
using IndexType = short;
// ---------------------------
template<typename ValT = ValueType, int MaxVal = MAX_VALUE, typename IdxT = IndexType>
class RandomizedSet {
    static_assert(MaxVal >= 0, "MaxVal must be non-negative");
    static_assert(is_integral_v<ValT>, "ValT must be an integral type");
    static_assert(is_signed_v<IdxT>, "IdxT should be signed (we use -1 as sentinel)");
public:
    using value_type = ValT; using index_type = IdxT;
    static constexpr size_t CAP = static_cast<size_t>(MaxVal) + 1;
    RandomizedSet() noexcept {
        position_map.fill(static_cast<index_type>(-1));
        cur_size = 0;
    }

    // add / remove / contains は値が有効範囲内かをチェックします
    bool add(value_type v) noexcept {
        if (!is_valid_value(v)) return false;
        auto uv = to_unsigned_index(v);
        if (position_map[uv] != static_cast<index_type>(-1)) return false; // already present
        elements[cur_size] = v;
        position_map[uv] = static_cast<index_type>(cur_size);
        ++cur_size;
        return true;
    }

    bool remove(value_type v) noexcept {
        if (!is_valid_value(v)) return false;
        auto uv = to_unsigned_index(v);
        index_type pos = position_map[uv];
        if (pos == static_cast<index_type>(-1)) return false; // not present
        // swap with last
        value_type last = elements[cur_size - 1];
        elements[static_cast<size_t>(pos)] = last;
        // 更新：last の位置を pos にする
        auto ulast = to_unsigned_index(last);
        position_map[ulast] = pos;
        // clear removed
        position_map[uv] = static_cast<index_type>(-1);
        --cur_size;
        return true;
    }

    value_type getRandom() const {
        if (cur_size == 0) throw runtime_error("RandomizedSet: set is empty");
        unsigned idx = static_cast<unsigned>(Random::randrange(static_cast<unsigned>(cur_size)));
        return elements[static_cast<size_t>(idx)];
    }

    size_t size() const noexcept { return cur_size; }

    bool contains(value_type v) const noexcept {
        if (!is_valid_value(v)) return false;
        return position_map[to_unsigned_index(v)] != static_cast<index_type>(-1);
    }

    void printElements() const {
        cout << "Elements: { ";
        for (size_t i = 0; i < cur_size; ++i) cout << +elements[i] << " ";
        cout << "}\n";
    }

private:
    // 実装補助: ValT を非負の配列インデックスに変換（安全にキャスト）
    static constexpr make_unsigned_t<ValT> to_unsigned_index(ValT v) noexcept {
        return static_cast<make_unsigned_t<ValT>>(v);
    }
    // 値が有効か（範囲チェック）
    static bool is_valid_value(ValT v) noexcept {
        if constexpr (is_signed_v<ValT>) {
            if (v < 0) return false;
            return static_cast<make_unsigned_t<ValT>>(v) <= static_cast<make_unsigned_t<int>>(MaxVal);
        } else {
            return static_cast<make_unsigned_t<ValT>>(v) <= static_cast<make_unsigned_t<int>>(MaxVal);
        }
    }
    // データ
    array<value_type, CAP> elements;          // 現在要素（順序は任意）
    array<index_type, CAP> position_map;      // 値 -> index（存在しない場合 -1）
    size_t cur_size;
};
using RandSet = RandomizedSet<ValueType, MAX_VALUE, IndexType>;