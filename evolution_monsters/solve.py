import bisect

class MonsterNode:
  def __init__(self, monster):
    self.monster = monster
    self.stone = 0
    self.group = -1
    self.evolutions = []
    self.log = []

def euler_tour(node, group, g, tour_logs, stone_accs):
  g[node].log.append(len(tour_logs[group]))
  g[node].group = group
  tour_logs[group].append(node)
  stone_accs[group].append(g[node].stone)
  for e in g[node].evolutions:
    euler_tour(e, group, g, tour_logs, stone_accs)
    g[node].log.append(len(tour_logs[group]))
    tour_logs[group].append(node)
    stone_accs[group].append(-g[e].stone)

n, m, q = map(int, input().split())
g = [MonsterNode(i) for i in range(n)]

for _ in range(m):
  x, a, b, = map(int, input().split())
  a -= 1; b -= 1
  g[a].evolutions.append(b)
  g[b].stone = x


tour_logs = []
stone_accs = []

# preprocess
groups = 0
for i in range(n):
  if g[i].group >= 0:
    continue
  tour_logs.append(list())
  stone_accs.append(list())
  euler_tour(i, groups, g, tour_logs, stone_accs)
  groups += 1

# imos
for stone_acc in stone_accs:
  for i in range(1, len(stone_acc)):
    stone_acc[i] += stone_acc[i-1]

ans = []
for _ in range(q):
  p1, p2 = map(int, input().split())
  p1 -= 1; p2 -= 1
  # 異なる進化treeのモンスターのとき
  if g[p1].group != g[p2].group:
    ans.append('IMPOSSIBLE')
    continue
  group = g[p1].group
  # p1を根とする進化treeの部分木にp2が存在しないとき
  if g[p1].log[0] > g[p2].log[0] or g[p2].log[-1] > g[p1].log[-1]:
    ans.append('IMPOSSIBLE')
    continue
  index = bisect.bisect_left(g[p1].log, g[p2].log[0]) - 1
  index = g[p1].log[index]
  next_monster = tour_logs[group][index + 1]
  cost = stone_accs[group][g[p2].log[0]] - stone_accs[group][index]
  ans.append(f'{next_monster + 1} {cost}')

print('\n'.join(ans))