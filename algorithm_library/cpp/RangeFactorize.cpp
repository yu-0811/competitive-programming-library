#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

// エラトステネスの篩
// N以下の素数を列挙する
vector<int> eratosthenes(int N) {
    vector<bool> is_prime(N + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= N; ++p) {
        if (is_prime[p]) {
            for (int q = p * p; q <= N; q += p) {
                is_prime[q] = false;
            }
        }
    }
    vector<int> prime_numbers;
    for (int p = 2; p <= N; ++p) {
        if (is_prime[p]) {
            prime_numbers.push_back(p);
        }
    }
    return prime_numbers;
}

// 区間エラトステネスの篩（素因数分解版）
// [L, R]の各数を素因数分解する
vector<vector<long long>> range_factorize(long long L, long long R) {
    if (L > R) return {};
    int sqrtR = sqrt(R);
    vector<int> primes = eratosthenes(sqrtR);
    
    long long range_size = R - L + 1;
    vector<vector<long long>> divisors(range_size);
    vector<long long> num(range_size);
    iota(num.begin(), num.end(), L); // numを L, L+1, ..., R で初期化

    for (int p : primes) {
        long long start = (L + p - 1) / p * p; // L以上の最小のpの倍数
        for (long long q = start; q <= R; q += p) {
            long long idx = q - L;
            while (num[idx] % p == 0) {
                divisors[idx].push_back(p);
                num[idx] /= p;
            }
        }
    }

    // sqrt(R)より大きい素因数を処理
    for (long long i = 0; i < range_size; ++i) {
        if (num[i] > 1) {
            divisors[i].push_back(num[i]);
        }
    }
    
    return divisors;
}

