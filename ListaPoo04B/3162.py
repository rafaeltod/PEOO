def distancia(x1, y1, z1, x2, y2, z2):
  return (((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2))**0.5

n = int(input())
naves = []
for x in range(n):
  x = list(map(int, input().split()))
  naves.append(x)

for i in range(n):
  menor_distancia = float("inf")
  for j in range(n):
    if i != j:
      d = distancia(naves[i][0], naves[i][1], naves[i][2], naves[j][0], naves[j][1], naves[j][2])
      menor_distancia = min(menor_distancia, d)

  if menor_distancia <= 20:
    print("A")
    
  elif menor_distancia <= 50:
    print("M")
    
  else:
    print("B")