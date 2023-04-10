splitmaluco = input().split()
a = float(splitmaluco[0])
b = float(splitmaluco[1])
c = float(splitmaluco[2])
delta = b**2 - 4*a*c
raiz = delta**(1/2)
if (delta < 0) or (a == 0):
    print('Impossivel calcular')
else:
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')