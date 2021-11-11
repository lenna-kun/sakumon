import random

for sample in range(20, 21):
  print(sample)
  samplein = open(f'./sample/in/random{sample}.txt', 'w')
  samplein_write = []

  n = random.randrange(1, 200001)
  a = [random.randrange(1, 1000000001) for _ in range(n)]

  before = 1
  for _ in range(200000):
    before = before + random.randrange(1)
    if before > n:
      break
    samplein_write.append(f'{before} {random.randrange(1, 1000000001)} {random.randrange(1, 1000000001)}\r\n')

  q = len(samplein_write)
  samplein.writelines(f'{n} {q}\r\n')
  samplein.writelines(f'{" ".join(map(str, a))}\r\n')
  samplein.writelines(samplein_write)
  samplein.close()
