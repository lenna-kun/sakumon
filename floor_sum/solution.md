解き方は複数ありますが，実装が最も楽な解法を紹介します．

まず，$\frac{B \times k}{A}$の少数部分からなる数列$X_k$を考えます．

$
X_k = \frac{B \times k}{A} - \mathrm{floor} (\frac{B \times k}{A})
$

このままでは扱いづらいので，$X_k$を扱いやすい形に変形すると，以下のように表せます．

$
Y_k = (B \times k) \mod A
$

$
X_k = \frac{Y_k}{A}
$

$Y_k$は明らかに周期性を持ちます．よって，$X_k$も$Y_k$と同じ周期を持ちます．周期は，$B \times k$が$\mathrm{lcm} (A, B)$の倍数ときなので，$\frac{A}{\mathrm{gcd} (A, B)}$です．したがって，$X_k$は，$X_{\frac{A}{\mathrm{gcd} (A, B)}}$まで求めれば十分です．

以上から，$\sum_{k=1}^{N} X_k$が以下の式で表されることがわかります．

$
\sum_{k=1}^{N} X_k = (\mathrm{floor} (\frac{N}{\frac{A}{\mathrm{gcd} (A, B)}}) \times \sum_{k=1}^{\frac{A}{\mathrm{gcd} (A, B)}} X_k) + \sum_{k=1}^{N \mod \frac{A}{\mathrm{gcd} (A, B)}} X_k
$

$
= \frac{(\mathrm{floor} (\frac{N}{\frac{A}{\mathrm{gcd} (A, B)}}) \times \sum_{k=1}^{\frac{A}{\mathrm{gcd} (A, B)}} Y_k) + \sum_{k=1}^{N \mod \frac{A}{\mathrm{gcd} (A, B)}} Y_k}{A}
$

したがって，最終的に求めるべき答え$\sum_{k=1}^N \mathrm{floor} (\frac{B \times k}{A})$は


$
\sum_{k=1}^N \mathrm{floor} (\frac{B \times k}{A})
$

$
= \sum_{k=1}^N (\frac{B \times k}{A} - X_k) 
$

$
= \sum_{k=1}^N \frac{B \times k}{A} - \sum_{k=1}^{N} X_k
$

$
= \frac{B \times \sum_{k=1}^{N} k - ((\mathrm{floor} (\frac{N}{\frac{A}{\mathrm{gcd} (A, B)}}) \times \sum_{k=1}^{\frac{A}{\mathrm{gcd} (A, B)}} Y_k) + \sum_{k=1}^{N \mod \frac{A}{\mathrm{gcd} (A, B)}} Y_k)}{A}
$

$\sum_{k=1}^{N} k = \frac{N \times (N+1)}{2}$なので，上記式を求めるのにかかる計算量は，$O(\frac{A}{\mathrm{gcd} (A, B)})$となり，これはこの問題の実行時間制限に対して十分高速です．

式では複雑に見えますが，コードは以下のようになり，短くてわかりやすいです．

```py
import math

a, b, n = map(int, input().split())
limit = a // math.gcd(a, b)
acc = [0]
for i in range(1, limit+1):
  acc.append(acc[-1] + (b*i)%a)

sum_all = ((n*(n+1))//2) * b
sum_decimal = (n//limit) * acc[-1] + acc[n%limit]

sum_integer = (sum_all-sum_decimal) // a

print(sum_integer)
```

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll int64_t

int main() {
  ll a, b, n;
  cin >> a >> b >> n;
  ll limit = a / gcd(a, b);
  vector<ll> acc(limit+1);
  for (int i = 1; i <= limit; i++) {
    acc[i] = acc[i-1] + (b*i)%a;
  }

  ll sum_all = ((n*(n+1))/2) * b;
  ll sum_decimal = (n/limit) * acc[limit] + acc[n%limit];

  ll sum_integer = (sum_all-sum_decimal) / a;
  cout << sum_integer << endl;
}
```