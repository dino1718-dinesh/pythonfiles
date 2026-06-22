n=int(input())
a = []

for i in range(n):
    l = int(input())
    a.append(l)

maxs = max(a)
k = min(a)

for i in a:
    if i > k and i < maxs:
        k = i

print(k)