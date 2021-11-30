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

# ans = (limit*b//a) * limit * ((n//limit-1)*(n//limit)//2)

# tmp = 0
# for i in range(1, limit+1):
#   tmp += (b*i)//a

# ans += tmp * (n//limit)

# for i in range(1, (n%limit)+1):
#   ans += (b*i)//a+(limit*b//a) * (n//limit)

# print(ans)

# ans = 0
# for i in range(1, n+1):
#   ans += (b*i)//a

# print(ans)