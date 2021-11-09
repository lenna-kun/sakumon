#include <bits/stdc++.h>
using namespace std;
typedef int64_t i64;

struct F { // 写像(モノイド)
  i64 mod = 1e9+7, x, y;

  F() { // 恒等写像(単位元)
    x = 1;
    y = 0;
  }

  i64 mapping(i64 a) { // f(a)
    return (x * a + y)%mod;
  }

  void composition(F &g) { // 合成写像
    x = (x * g.x)%mod;
    y = (y * g.x + g.y)%mod;
  }
};

int main() {
  i64 n, q;
  cin >> n >> q;
  vector<i64> a(n);
  for (i64 &e: a) cin >> e;
  vector<F> imos(n, F());

  while (q--) {
    i64 l, x, y;
    cin >> l >> x >> y;
    F g = F(); g.x = x; g.y = y;
    imos.at(l-1).composition(g);
  }
  F acc = F();
  for (int i = 0; i < n; i++) {
    acc.composition(imos.at(i));
    a.at(i) = acc.mapping(a.at(i));
  }

  for (int i = 0; i < n-1; i++) {
    cout << a.at(i) << ' ';
  }
  cout << a.at(n-1) << endl;
}