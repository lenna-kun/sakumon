#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
#define i64 int64_t
#define rep(n) for(int i = 0; i < (n); i++)

int main() {
  i64 a, b, n;
  cin >> a >> b >> n;
  i64 limit = a / gcd(a, b);
  vector<i64> acc(limit+1);
  rep (limit) {
    acc[i+1] = acc[i] + (b*(i+1))%a;
  }

  i64 sum_all = ((n*(n+1))/2) * b;
  i64 sum_decimal = (n/limit) * acc[limit] + acc[n%limit];

  i64 sum_integer = (sum_all-sum_decimal) / a;
  cout << sum_integer << endl;
  // i64 ans = 0;
  // rep (n) {
  //   ans += (b*(i+1)) / a;
  // }
  // cout << ans << endl;
}