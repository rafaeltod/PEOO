c, n = input().split()
c = int(c)
n = int(n)

if c > n:
    print(c % n)
else:
    print(n % c)