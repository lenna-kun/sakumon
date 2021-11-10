import random
import bisect
import sys
sys.setrecursionlimit(10**7)
class MonsterNode:
  def __init__(self, monster):
    self.monster = monster
    self.group = -1
    self.stone = random.randrange(0, 1000000001)
    self.stone_acc = self.stone
    self.log = []

def euler_tour(n, m, q, evolutions, node, group, nodes, tour_logs, stone_accs):
  nodes[node].group = group
  nodes[node].log.append(len(tour_logs[group]))
  tour_logs[group].append(node)
  stone_accs[group].append(nodes[node].stone)
  g = []
  for e in range(len(evolutions)+1, len(evolutions)+random.randrange(m-len(evolutions)+1)//random.randrange(100, 1000)):
    g.append(e)
  for e in g:
    evolutions.append((nodes[e].stone, node, e))
  for e in g:
    euler_tour(n, m, q, evolutions, e, group, nodes, tour_logs, stone_accs)
    nodes[node].log.append(len(tour_logs[group]))
    tour_logs[group].append(node)
    stone_accs[group].append(-nodes[e].stone)

for sample in range(1, 21):
  samplein = open(f'./sample/in/random{sample}.txt', 'w')
  sampleout = open(f'./sample/out/random{sample}.txt', 'w')
  samplein_write = []
  sampleout_write = []
  sampleout_ = []

  n = random.randrange(2, 2*100000+1)
  m = random.randrange(0, n)
  q = min(2*100000, n*(n-1)//2)

  nodes = [MonsterNode(i) for i in range(n)]
  evolutions = []
  tour_logs = []
  stone_accs = []

  groups = 0
  for i in range(n):
    if nodes[i].group >= 0:
      continue
    tour_logs.append(list())
    stone_accs.append(list())
    euler_tour(n, m, q, evolutions, i, groups, nodes, tour_logs, stone_accs)
    groups += 1

  # assert m == len(evolutions)
  m = len(evolutions)
  print(groups)

  # imos
  for stone_acc in stone_accs:
    for i in range(1, len(stone_acc)):
      stone_acc[i] += stone_acc[i-1]

  mapping = [*range(n)]
  querys_ = set()
  querys = []
  for _ in range(q):
    while True:
      s = random.sample(mapping, 2)
      if random.randrange(100) < 90:
        s.sort()
      p1, p2 = s
      if (p1, p2) not in querys_ and (p2, p1) not in querys_:
        break
    querys_.add((p1, p2))
    querys.append((p1, p2))
    # 異なる進化treeのモンスターのとき
    if nodes[p1].group != nodes[p2].group:
      sampleout_.append((-1, -1))
      continue
    group = nodes[p1].group
    # p1を根とする進化treeの部分木にp2が存在しないとき
    if nodes[p1].log[0] > nodes[p2].log[0] or nodes[p2].log[-1] > nodes[p1].log[-1]:
      sampleout_.append((-1, -1))
      continue
    index = bisect.bisect_left(nodes[p1].log, nodes[p2].log[0]) - 1
    index = nodes[p1].log[index]
    next_monster = tour_logs[group][index + 1]
    cost = stone_accs[group][nodes[p2].log[0]] - stone_accs[group][index]
    sampleout_.append((next_monster, cost))

  assert len(querys) == len(sampleout_) and q == len(querys)
  q = len(querys)
  random.shuffle(mapping)

  for e in evolutions:
    stone, a, b = e
    a = mapping[a] + 1
    b = mapping[b] + 1
    samplein_write.append(f'{stone} {a} {b}\r\n')

  for e in querys:
    p1, p2 = e
    p1 = mapping[p1] + 1
    p2 = mapping[p2] + 1
    samplein_write.append(f'{p1} {p2}\r\n')

  samplein.writelines(f'{n} {m} {q}\r\n')
  samplein.writelines(samplein_write)
  samplein.close()

  for e in sampleout_:
    monster, cost = e
    if monster == -1:
      pass
      # sampleout_write.append('IMPOSSIBLE\r\n')
    else:
      monster = mapping[monster] + 1
      sampleout_write.append(f'{monster} {cost}\r\n')

  sampleout.writelines(sampleout_write)
  sampleout.close()
