print('Digite três valores:')
a = int(input())
b = int(input())
c = int(input())

if a + b <= c:
  print('Esses valores não formam um triângulo')

elif a == b and b == c:
  print('Equilatero')

elif a == b or b == c:
  print('Isoceles')
  
elif a != b != c:
  print('Escaleno')
