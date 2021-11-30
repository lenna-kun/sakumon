## 問題

自然数$A,B,N$が与えられます．

$\sum_{k=1}^{N} \mathrm{floor} (\frac{B \times k}{A}) = \mathrm{floor} (\frac{B \times 1}{A}) + \mathrm{floor} (\frac{B \times 2}{A}) + \mathrm{floor} (\frac{B \times 3}{A}) + ... + \mathrm{floor} (\frac{B \times N}{A})$

を求めてください．ただし，$\mathrm{floor} (x)$は，$x$以下で最大の整数値を返す関数です．

## 制約

- $1 \leq A \leq 2 \times 10^5$
- $1 \leq B < 10$
- $1 \leq N \leq 10^9$
- 入力は全て整数

## 入力

```
A B N

```

## 出力

$\sum_{k=1}^{N} \mathrm{floor} (\frac{B \times k}{A})$を1行に出力してください．

## サンプル

### 入力例1

```
2 3 1

```

### 出力例1

```
1

```

$\frac{3}{2}$の整数部分は$1$です．

### 入力例2

```
3 2 1

```

### 出力例2

```
0

```

$\frac{2}{3}$の整数部分は$0$です．

### 入力例3

```
6 8 5

```

### 出力例3

```
18

```

$\sum_{k=1}^{5} \mathrm{floor} (\frac{8 \times k}{6}) = \mathrm{floor} (\frac{8}{6}) + \mathrm{floor} (\frac{16}{6}) + \mathrm{floor} (\frac{24}{6}) + \mathrm{floor} (\frac{32}{6}) + \mathrm{floor} (\frac{40}{6}) = 1 + 2 + 4 + 5 + 6 = 18$です．