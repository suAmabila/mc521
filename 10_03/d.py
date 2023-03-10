t = int(input())

for _ in range(t):
  c1, c2, c3 = map(int, input().split()) # capacidade dos containers
  a1, a2, a3, a4, a5 = map(int, input().split()) # numero de itens de cada categoria

# 1 2 3
# 1 2 3 0 0
# 2 2 3
# 1 2 3 1 0
# 2 2 3
# 1 2 3 0 1
# 1 2 5
# 1 2 3 1 1
# 0 0 0
# 0 0 0 0 0
# 0 0 4
# 1 0 0 0 0
# 13 37 42
# 0 0 0 40 47
