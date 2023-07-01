while True:
  try:
    
    n, m = map(int, input().split())
    matriz = []

    for k in range(n + 2):
      matriz.append([0] * (m + 2))

    for k in range(n):
      linha = list(map(int, input().split())) 
      for j in range(m):
        matriz[k+1][j+1] = linha[j]

    for i in range(1, n + 1):
      for j in range(1, m + 1):
        if matriz[i][j] == 1:
          print(9, end='')
        else:
          soma = 0
          if matriz[i-1][j]:
            soma += 1
          if matriz[i][j-1] == 1:
            soma += 1
          if matriz[i+1][j] == 1:
            soma += 1
          if matriz[i][j+1] == 1:
            soma += 1
          print(soma, end='')
      print()
  except EOFError:
    break