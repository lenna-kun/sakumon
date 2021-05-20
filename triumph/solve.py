class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def card2number(n, card):
  if card[0] == 'S':
    return int(card[1:])-1
  elif card[0] == 'C':
    return n + int(card[1:])-1
  elif card[0] == 'D':
    return 2*n + int(card[1:])-1
  elif card[0] == 'H':
    return 3*n + int(card[1:])-1
  else:
    raise Exception

n, q = map(int, input().split())

head = Node(0)
nodes = [head]
for i in range(1, 4*n):
  node = Node(i)
  nodes[-1].right = node
  node.left = nodes[-1]
  nodes.append(node)

for _ in range(q):
  l, r = map(lambda arg: card2number(n, arg), input().split())
  if nodes[l].left is None:
    continue
  nodes[l].left.right = nodes[r].right
  if nodes[r].right is not None:
    nodes[r].right.left = nodes[l].left
  head.left = nodes[r]
  nodes[r].right = head
  head = nodes[l]
  nodes[l].left = None
  tmp = head

cards = [[], [], [], []]
for _ in range(4*n):
  cards[head.value//n].append(head.value%n+1)
  head = head.right
for i in range(4):
  print(*[f'{"SCDH"[i]}{card}' for card in cards[i]])
