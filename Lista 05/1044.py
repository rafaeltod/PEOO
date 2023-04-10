A, B = input().split()
a = int(A)
b = int(B)

if max(a,b) % min(a,b) == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')