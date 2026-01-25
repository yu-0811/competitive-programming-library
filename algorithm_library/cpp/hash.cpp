// 使用例https://atcoder.jp/contests/abc440/submissions/72666963

// 64bit整数用の高品質なミキシング関数
// (SplitMix64の定数などを使用)
uint64_t mix(uint64_t x) {
    x += 0x9e3779b97f4a7c15;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
    return x ^ (x >> 31);
}

// vectorを受け取ってハッシュを返す関数
uint64_t get_vector_hash(const vector<int>& vec) {
    uint64_t seed = vec.size();
    for (const auto& val : vec) {
        seed ^= mix(static_cast<uint64_t>(val)) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
    }
    return seed;
}