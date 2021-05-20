import random

def number2card(n, number):
  return f'{"SCDH"[number//n]}{number%n+1}'

for sample in range(1):
  samplein = open(f'./sample/in/random-large.txt', 'w')
  sampleout = open(f'./sample/out/random-large.txt', 'w')
  samplein_write = []

  n = 10**5 # random.randrange(1, 10**5+1)
  q = 10**5 # random.randrange(1, 10**5+1)
  print(n, q)

  samplein_write.append(f'{n} {q}\r\n')

  cards = [*range(4*n)]

  for _ in range(q):
    tmp = [random.randrange(0, 4*n), random.randrange(0, 4*n)]
    l = min(tmp)
    r = max(tmp)
    samplein_write.append(f'{number2card(n, cards[l])} {number2card(n, cards[r])}\r\n')
    cards = cards[l:r+1]+cards[:l]+cards[r+1:]

  samplein.writelines(samplein_write)
  samplein.close()

  marks = [[], [], [], []]
  for card in cards:
    marks[card//n].append(card%n+1)

  for i in range(4):
    sampleout.write(' '.join([f'{"SCDH"[i]}{card}' for card in marks[i]]))
    sampleout.write('\r\n')

  sampleout.close()
