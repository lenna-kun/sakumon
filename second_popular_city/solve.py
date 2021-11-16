import random
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**4)

INF = 10**18

def euler_tour(node, parent, g, a, euler_acc):
  euler_acc.append(a[node][parent])
  if node != parent:
    euler_acc[-1] += euler_acc[-2]
  for e in g[node]:
    if e == parent:
      continue
    euler_tour(e, node, g, a, euler_acc)
    euler_acc.append(euler_acc[-1]-a[e][node])

def dijkstra_correct(first_city, second_city, n, g, new_g):
  d = [(INF, 0)] * n
  d[first_city] = (0, 0)
  hq = [(0, 0, -1, first_city)]
  count = 0
  while hq:
    p = heappop(hq)
    v = p[3]
    if d[v] < (p[0], p[1]):
      continue
    if p[2] >= 0:
      new_g[p[2]].append(p[3])
      new_g[p[3]].append(p[2])
      count += 1
    for to, cost in g[v]:
      is_tree_of_second_city = -((-p[1]) | (to == second_city))
      if d[to] > (d[v][0] + cost, is_tree_of_second_city):
        d[to] = (d[v][0] + cost, is_tree_of_second_city)
        heappush(hq, (d[to][0], d[to][1], v, to))
  assert count == n-1
  return [e[0] for e in d]

n, x, y = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]
g = [[] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if i != j:
      g[i].append((j, a[i][j]))

new_g = [[] for _ in range(n)]
dx = dijkstra_correct(x-1, y-1, n, g, new_g)

euler_acc = []
euler_tour(y-1, y-1, new_g, a, euler_acc)

print(max(dx), max(euler_acc))