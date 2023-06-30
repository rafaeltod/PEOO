n, m = map(int, input().split())
matriz = []

for _ in range(n):
    linha = list(map(int, input().split())) 
    matriz.append(linha)

for i in range(n):
    for j in range(m):
        if matriz[i][j] == 1:
            print(9, end='')
        else:
            soma = 0
            for x in range(max(0, i-1), min(n, i+2)):
                for y in range(max(0, j-1), min(m, j+2)):
                    if matriz[x][y] == 1 and (x != i or y != j):
                        soma += 1
            print(soma, end='')
    print()