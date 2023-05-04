conta = input('Digite dois valores inteiros separados por um operador +, -, * ou / \n')

if '+' in conta:
  a, b = map(int, conta.split('+'))
  resultado = a + b

if '-' in conta:
  a, b = map(int, conta.split('-'))
  resultado = a - b

if '*' in conta:
  a, b = map(int, conta.split('*'))
  resultado = a * b

if '/' in conta:
  a, b = map(int, conta.split('/'))
  resultado = a / b

print(f'O resultado da operação é {resultado}')