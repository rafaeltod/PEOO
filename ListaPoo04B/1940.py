j, r = map(int, input().split())
rodadasl = list(map(int, input().split()))
rodadas = []
pontosvencedor = int()
vencedor = int()
for x in range(r):
  rodada = []
  for y in range(j):
    rodada.append(rodadasl[y+x*j])
  rodadas.append(rodada)
for z in range(j):
  soma = 0
  for w in range(r):
    soma += rodadas[w][z]
  if soma >= pontosvencedor:
    pontosvencedor = soma
    vencedor = z+1
print(vencedor)