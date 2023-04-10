v = []
c = 0
p = 0

for i in range(0,100):
    n=int(input())
    v.append(n)

    if v[i] > c:
        c = v[i]
        p = i + 1
print(c)
print(p)