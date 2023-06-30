x = []
n = int(input())
for i in range(10):
  n *= 2
  x.append(n)
  print(f'X[{i}] = {x[i]}')