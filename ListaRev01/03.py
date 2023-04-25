print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

p = 0
i = 0
lista = [a, b, c, d]

for x in lista:
  if x % 2 == 0:
    p += x
  else:
    i += x

print(f'Soma dos pares = {p}')
print(f'Soma dos ímpares = {i}')