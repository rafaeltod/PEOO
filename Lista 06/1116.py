n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if y == 0:
      print("divisao impossivel")
    else:
      d = x / y
      print(f'{d:.1f}')