import math
import random

def solve(a, b, n):
  limit = a // math.gcd(a, b)
  acc = [0]
  for i in range(1, limit+1):
    acc.append(acc[-1] + (b*i)%a)

  sum_all = ((n*(n+1))//2) * b
  sum_decimal = (n//limit) * acc[-1] + acc[n%limit]

  sum_integer = (sum_all-sum_decimal) // a

  ans = (limit*b//a) * limit * ((n//limit-1)*(n//limit)//2)

  tmp = 0
  for i in range(1, limit+1):
    tmp += (b*i)//a

  ans += tmp * (n//limit)

  for i in range(1, (n%limit)+1):
    ans += (b*i)//a+(limit*b//a) * (n//limit)
  
  assert ans == sum_integer
  return sum_integer

for sample in range(1, 2):
  b = random.randrange(2, 10)
  while True:
    a = random.randrange(100000, 200001)
    if a%b > 0:
      break

  n = random.randrange(999990000, 1000000001)

  samplein = open(f'./sample/in/small_b_random{sample}.txt', 'w')
  samplein.writelines(f'{a} {b} {n}\r\n')
  samplein.close()

  sampleout = open(f'./sample/out/small_b_random{sample}.txt', 'w')
  sampleout.writelines(f'{solve(a, b, n)}\r\n')
  sampleout.close()