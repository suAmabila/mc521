t = int(input())

for _ in range(t):
  n = int(input())
  a = n - 1
  b = 1
  if a < b or a == b:
    print(0)
  else:
    soma = 0
    while a > b:
      soma += 1 
      a -= 1
      b += 1
    print(soma)


# 6
# 7
# 1
# 2
# 3
# 2000000000
# 763243547
