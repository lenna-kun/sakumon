import random
from heapq import heappush, heappop

INF = 10**18

def dijkstra(s, n, g):
  d = [INF] * n
  d[s] = 0
  hq = [(0, s)]
  while hq:
    p = heappop(hq)
    v = p[1]
    if d[v] < p[0]:
      continue
    for to, cost in g[v]:
      if d[to] > d[v] + cost:
        d[to] = d[v] + cost
        heappush(hq, (d[to], to))
  return max(d)

def dijkstra_wrong1(s, n, g, a, new_g):
  d = [INF] * n
  d[s] = 0
  hq = [(0, -1, s)]
  count = 0
  while hq:
    p = heappop(hq)
    v = p[2]
    if d[v] < p[0]:
      continue
    if p[1] >= 0:
      new_g[p[1]].append((p[2], a[p[1]][p[2]]))
      new_g[p[2]].append((p[1], a[p[2]][p[1]]))
      count += 1
    for to, cost in g[v]:
      if d[to] > d[v] + cost:
        d[to] = d[v] + cost
        heappush(hq, (d[to], v, to))
  assert count == n-1
  return d

def dijkstra_wrong2(s, second_city, n, g, a, new_g):
  d = [INF] * n
  d[s] = 0
  hq = [(0, 0, -1, s)]
  count = 0
  while hq:
    p = heappop(hq)
    v = p[3]
    if d[v] < p[0]:
      continue
    if p[2] >= 0:
      new_g[p[2]].append((p[3], a[p[2]][p[3]]))
      new_g[p[3]].append((p[2], a[p[3]][p[2]]))
      count += 1
    for to, cost in g[v]:
      is_second_city = -(to == second_city)
      if d[to] > d[v] + cost:
        d[to] = d[v] + cost
        heappush(hq, (d[to], is_second_city, v, to))
  assert count == n-1
  return d

def dijkstra_wrong3(first_city, second_city, n, g, a, new_g):
  d = [INF] * n
  d[first_city] = 0
  hq = [(0, 0, -1, first_city)]
  count = 0
  while hq:
    p = heappop(hq)
    v = p[3]
    if d[v] < p[0]:
      continue
    if p[2] >= 0:
      new_g[p[2]].append((p[3], a[p[2]][p[3]]))
      new_g[p[3]].append((p[2], a[p[3]][p[2]]))
      count += 1
    for to, cost in g[v]:
      is_tree_of_second_city = -((-p[1]) | to == second_city)
      if d[to] > d[v] + cost:
        d[to] = d[v] + cost
        heappush(hq, (d[to], is_tree_of_second_city, v, to))
  assert count == n-1
  return d

def dijkstra_correct(first_city, second_city, n, g, a, new_g):
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
      new_g[p[2]].append((p[3], a[p[2]][p[3]]))
      new_g[p[3]].append((p[2], a[p[3]][p[2]]))
      count += 1
    for to, cost in g[v]:
      is_tree_of_second_city = -((-p[1]) | (to == second_city))
      if d[to] > (d[v][0] + cost, is_tree_of_second_city):
        d[to] = (d[v][0] + cost, is_tree_of_second_city)
        heappush(hq, (d[to][0], d[to][1], v, to))
  assert count == n-1
  return [e[0] for e in d]

for sample in range(18, 21):
  while True:
    n = random.randrange(2, 2001)
    x, y = random.sample(range(1, n+1), 2)
    assert x != y
    a = [[0]*n for _ in range(n)]

    for i in range(n):
      for j in range(i+1, n):
        a[i][j] = random.randrange(1, 1000000001)
        a[j][i] = a[i][j]

    # sample 2
    # n = 4
    # x = 1
    # y = 2
    # a = [[0, 10, 20, 40], [10, 0, 10, 20], [20, 10, 0, 10], [40, 20, 10, 0]]

    # print(x, y)
    # print(a)

    g = [[] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if i != j:
          g[i].append((j, a[i][j]))

    g_wrong1 = [[] for _ in range(n)]
    dx_wrong1 = dijkstra_wrong1(x-1, n, g, a, g_wrong1)
    g_wrong2 = [[] for _ in range(n)]
    dx_wrong2 = dijkstra_wrong2(x-1, y-1, n, g, a, g_wrong2)
    g_wrong3 = [[] for _ in range(n)]
    dx_wrong3 = dijkstra_wrong3(x-1, y-1, n, g, a, g_wrong3)
    g_correct = [[] for _ in range(n)]
    dx_correct = dijkstra_correct(x-1, y-1, n, g, a, g_correct)

    assert max(dx_wrong1) == max(dx_wrong2) == max(dx_wrong3) == max(dx_correct)

    dy_wrong1 = dijkstra(y-1, n, g_wrong1)
    dy_wrong2 = dijkstra(y-1, n, g_wrong2)
    dy_wrong3 = dijkstra(y-1, n, g_wrong3)
    dy_correct = dijkstra(y-1, n, g_correct)

    if dy_correct != dy_wrong1 and dy_correct != dy_wrong2 and dy_correct != dy_wrong3:
      print(sample, 'good')
    elif dy_correct == dy_wrong1 == dy_wrong2 == dy_wrong3:
      print(sample, 'bad')
    else:
      print(sample, 'not bad')

    samplein_write = []
    for e in a:
      samplein_write.append(f'{" ".join(map(str, e))}\r\n')

    samplein = open(f'./sample/in/random{sample}.txt', 'w')
    samplein.writelines(f'{n} {x} {y}\r\n')
    samplein.writelines(samplein_write)
    samplein.close()

    sampleout = open(f'./sample/out/random{sample}.txt', 'w')
    sampleout.writelines(f'{max(dx_correct)} {dy_correct}\r\n')
    sampleout.close()
    break
