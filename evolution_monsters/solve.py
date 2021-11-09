import bisect

class MonsterNode:
  def __init__(self, monster):
    self.monster = monster
    self.level = -1
    self.depth = -1
    self.group = -1
    self.evolutions = []
    self.log = []

def euler_tour(node, depth, group, g, tour_logs):
  g[node].log.append(len(tour_logs[group]))
  g[node].depth = depth
  g[node].group = group
  tour_logs[group].append(node)
  for e in g[node].evolutions:
    euler_tour(e, depth+1, group, g, tour_logs)
    g[node].log.append(len(tour_logs[group]))
    tour_logs[group].append(node)

n, m, l, q = map(int, input().split())
g = [MonsterNode(i) for i in range(n)]

for _ in range(m):
  x, a, b, = map(int, input().split())
  a -= 1; b -= 1
  g[a].evolutions.append(b)
  g[b].level = x


tour_logs = []
groups = 0
for i in range(n):
  if g[i].depth >= 0:
    continue
  tour_logs.append(list())
  euler_tour(i, 0, groups, g, tour_logs)
  groups += 1

ans = []
for _ in range(q):
  y, p1, p2 = map(int, input().split())
  p1 -= 1; p2 -= 1
  # 異なる進化treeのモンスターのとき
  if g[p1].group != g[p2].group:
    ans.append('IMPOSSIBLE')
    continue
  group = g[p1].group
  # 必要な進化回数分のレベルアップが不可能なとき
  if g[p2].depth - g[p1].depth > l - y:
    ans.append('IMPOSSIBLE')
    continue
  # p1を根とする進化treeの部分木にp2が存在しないとき
  if g[p1].log[0] > g[p2].log[0] or g[p2].log[-1] > g[p1].log[-1]:
    ans.append('IMPOSSIBLE')
    continue
  index = bisect.bisect_left(g[p1].log, g[p2].log[0]) - 1
  index = g[p1].log[index] + 1
  next_monster = tour_logs[group][index]
  ans.append(f'{max(g[next_monster].level, y + 1)} {next_monster + 1}')

print('\n'.join(ans))