n = int(input())
t = 0
c = 0
r = 0
s = 0

for x in range(n):
    q, a = input().split()
    q = int(q)
    a = str(a)
    t += q
    if a == "C":
        c += q
    if a == "R":
        r += q
    if a == "S":
        s += q
    pc = c / t * 100
    pr = r / t * 100
    ps = s / t * 100
print(f'Total: {t} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')