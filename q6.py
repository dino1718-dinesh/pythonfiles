import numpy
n=int(input())
e=int(input())
l=int(input())
m=[]
f=[]
h=[]
for i in range (n):
    u=list(map(int,input().split()))
    m.append(u)
    
for p in range (e):
    u=list(map(int,input().split()))
    f.append(u)
    
for w in range (l):
    u=list(map(int,input().split()))
    h.append(u)

print(numpy.zeros(f))
print(numpy.zeros(h))
print(numpy.zeros(m))


print(numpy.ones(m))
print(numpy.ones(f))
print(numpy.ones(h))
    
    