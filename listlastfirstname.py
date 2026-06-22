f=[]
l=[]
g=[]
o=[]
p=[]
i =int(input("enter the value how many to insert"))
for j in range (i):
    m=input("enter the value")
    f.append(m)

j =int(input("enter the value how many to inssert"))
for j in range (i):
    k=input("enter the value")
    l.append(k)

for t in f:
    for w in range(2):
        o.append(t[w])

for q in l:
    for w in range(len(q)-1,len(q)-3,-1):
         p.append(q[w])

print("these are first",o)
print("these are last",p)
o.extend(p)
name = ''.join(o)
print(name)