def sum_matrix(A, n, m):
  sum = 0
  for i in range(n):
    for j in range(m):
      sum += A[i][j]
  return sum

A = []
n, m = map(int, input().split())
for i in range(n):
  A.append([])
  lista = input().split()
  lista = list(map(int, lista))
  A[i].append(lista)
  
for i in range(n):
  for j in range(m):
    print(A[i][j])
  print()
