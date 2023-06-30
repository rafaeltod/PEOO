x = []
for i in range(100):
  n = float(input())
  x.append(n)
  if x[i] <= 10:
    print(f'A[{i}] = {x[i]}')