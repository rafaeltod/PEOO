print("Digite os coeficientes a, b, e c de uma equação do II grau")
a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c
raiz = delta**(1/2)
if (delta < 0) or (a == 0):
    print('impossível calcular')
else:
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print(f'As raízes são {x1:.0f} e {x2:.0f}')