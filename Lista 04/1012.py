valores = input().split()
valor1 = float(valores[0])
valor2 = float(valores[1])
valor3 = float(valores[2])
pi = 3.14159
areadotriangulo = (valor1 * valor3) / 2
areadocirculo = pi * (valor3)**2
areadotrapezio = (valor1 + valor2) * (valor3) / 2
areadoquadrado = (valor2)**2
areadoretangulo = (valor1) * (valor2)
print (f'TRIANGULO: {areadotriangulo:.3f}')
print (f'CIRCULO: {areadocirculo:.3f}')
print (f'TRAPEZIO: {areadotrapezio:.3f}')
print (f'QUADRADO: {areadoquadrado:.3f}')
print (f'RETANGULO: {areadoretangulo:.3f}')