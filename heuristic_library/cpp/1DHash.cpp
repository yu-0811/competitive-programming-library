// 一次元 Zobrist Hash
// 盤面の長さ、盤面の値の種類数をテンプレート引数として受け取る
// もうちょっといい感じにできそう、特に getValueIndex の部分
using HashType = uint32_t; // TODO
template<short LEN, short NumValue>
struct ZobristHash2D {
private:
    // ハッシュ値を格納するテーブル
    array<array<HashType, NumValue>, LEN> table;
    
    // 盤面の種類を表す値から、テーブルのインデックスに変換する
    static constexpr short getValueIndex(short value) {
        return value + 100;
    }

public:
    // コンストラクタ：オブジェクト生成時にハッシュテーブルを乱数で初期化する
    ZobristHash2D() {
        for (int i = 0; i < LEN; ++i) {
            for (int k = 0; k < NumValue; ++k) {
                table[i][k] = Random::xorshift64(); // 32ビットでいいときは xorshift32() でも良い
            }
        }
    }

    // 初期盤面からハッシュ値を計算する
    template<typename Board> // 任意の盤面の型を取れるようになる
    HashType initialize_hash(const Board& board) const {
        assert (board.size() == LEN);
        HashType hash = 0;
        for (int i = 0; i < LEN; ++i) {
            int index = getValueIndex(board[i]);
            hash ^= table[i][index];
        }
        return hash;
    }

    // 1マスの変化からハッシュ値を高速に更新（差分更新）する
    // current_hash: 更新前のハッシュ値
    HashType update_hash(HashType& current_hash, const short (&X)[100], Action& action) const {
        HashType new_hash = current_hash;
        auto pi = input.P[action.turn];
        new_hash = new_hash ^ table[pi][getValueIndex(X[pi])] ^ table[pi][getValueIndex(X[pi] + action.dx)];
        auto qi = input.Q[action.turn];
        new_hash = new_hash ^ table[qi][getValueIndex(X[qi])] ^ table[qi][getValueIndex(X[qi] + action.dx)];
        auto ri = input.R[action.turn];
        new_hash = new_hash ^ table[ri][getValueIndex(X[ri])] ^ table[ri][getValueIndex(X[ri] + action.dx)];
        return new_hash;
    }
};
const short LEN = 100, NumValue = 200; // TODO
ZobristHash2D<LEN, NumValue> zobrist_hash;