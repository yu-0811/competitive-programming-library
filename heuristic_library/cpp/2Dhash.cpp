// 二次元 Zobrist Hash
// 盤面の高さと幅、駒の種類数をテンプレート引数として受け取る
// もうちょっといい感じにできそう、特に getValueIndex の部分
using HashType = uint32_t; // TODO
template<short Height, short Width, short NumValue>
struct ZobristHash2D {
private:
    // ハッシュ値を格納するテーブル
    array<array<array<HashType, NumValue>, Width>, Height> table;
    
    // 盤面の種類を表す値から、テーブルのインデックスに変換する
    static constexpr short getValueIndex(short value) { // <<< 変更
        if (value == -1) return 0; // 'o'
        if (value == -2) return 1; // '.'
        return 2;                       // 'x'
    }

public:
    // コンストラクタ：オブジェクト生成時にハッシュテーブルを乱数で初期化する
    ZobristHash2D() {
        for (int i = 0; i < Height; ++i) {
            for (int j = 0; j < Width; ++j) {
                for (int k = 0; k < NumValue; ++k) {
                    table[i][j][k] = Random::xorshift64(); // 32ビットでいいときは xorshift32() でも良い
                }
            }
        }
    }

    // 初期盤面からハッシュ値を計算する
    template<typename Board> // 任意の盤面の型を取れるようになる
    HashType initialize_hash(const Board& board) const {
        assert (board.size() == Height && board[0].size() == Width);
        HashType hash = 0;
        for (int i = 0; i < Height; ++i) {
            for (int j = 0; j < Width; ++j) {
                int index = getValueIndex(board[i][j]);
                hash ^= table[i][j][index];
            }
        }
        return hash;
    }

    // 1マスの変化からハッシュ値を高速に更新（差分更新）する
    // current_hash: 更新前のハッシュ値
    // r, c: 変化があったマスの座標
    // old_value: 変化前の盤面
    // new_value: 変化後の盤面
    HashType update_hash(HashType current_hash, short r, short c, short old_value, short new_value) const {
        short old_index = getValueIndex(old_value);
        short new_index = getValueIndex(new_value);
        return current_hash ^ table[r][c][old_index] ^ table[r][c][new_index];
    }
};
const short Height = N, Width = N, NumValue = 3; // TODO
ZobristHash2D<Height, Width, NumValue> zobrist_hash;