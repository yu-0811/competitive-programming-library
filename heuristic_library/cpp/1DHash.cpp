// 一次元 Zobrist Hash
// 盤面の長さ、盤面の値の種類数をテンプレート引数として受け取る
// もうちょっといい感じにできそう、特に getValueIndex の部分
// LEN: 盤面のサイズ
// NumValue: 値のバリエーションの数（配列の確保サイズ）
// MIN_VAL: 値の最小値（これを使ってオフセットする）
template<int LEN, int NumValue, int MIN_VAL = 0> 
struct ZobristHash1D {
private:
    array<array<HashType, NumValue>, LEN> table;

    // 値をインデックスに変換
    static constexpr int getValueIndex(int value) {
        int index = value - MIN_VAL;
        assert(index >= 0 && index < NumValue); 
        
        return index;
    }

public:
    // コンストラクタ：オブジェクト生成時にハッシュテーブルを乱数で初期化する
    ZobristHash1D() {
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
    // pos: 変化したマスの位置
    // old_value: 変化前の値
    // new_value: 変化後の値
    // クラス内部に追加・修正
    HashType update_hash(HashType current_hash, int pos, int old_value, int new_value) const {
        current_hash ^= table[pos][getValueIndex(old_value)];
        current_hash ^= table[pos][getValueIndex(new_value)];
        return current_hash;
    }
};
// TODO
using HashType = uint32_t; 
const int LEN = 50; // 盤面の長さ
const int MIN_VAL = 0; // 盤面の値の最小値
const int NumValue = 100000; // 盤面の値のバリエーション数
ZobristHash1D<LEN, NumValue, MIN_VAL> zobrist_hash;