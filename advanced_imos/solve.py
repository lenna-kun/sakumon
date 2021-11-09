class F:
  MOD = 10**9+7
  def __init__(self):
    self.x = 1
    self.y = 0

  def mapping(self, a):
    return (self.x * a + self.y)%F.MOD

  def composition(self, g):
    h = F()
    h.x = (g.x * self.x)%F.MOD
    h.y = (g.y * self.x + self.y)%F.MOD
    return h

n, q = map(int, input().split())
a = [*map(int, input().split())]
imos = [F() for _ in range(n)]

for _ in range(q):
  l, x, y = map(int, input().split())
  g = F(); g.x = x; g.y = y
  imos[l-1] = g.composition(imos[l-1])

acc = F()
for i in range(n):
  acc = imos[i].composition(acc)
  a[i] = acc.mapping(a[i])

print(*a)