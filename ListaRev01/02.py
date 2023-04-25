print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
md = (a + b + c + d) // 4
print(f'Média = {md}')

print("Números menores que a média")
l = [a, b, c, d]

for i in l:
  if md > i:
    print(i)

print("Números maiores ou iguais à média")

for x in l:
  if md <= x:
    print(x)