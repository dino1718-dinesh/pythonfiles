n=[1,2,343,344,42,32,2]
n.append(2000)
print(n)
n.sort()
print(n)
n.sort(reverse=True)
print(n)
n.reverse()
print(n)
print(n.index(2))

n.insert(2,50000)
print(n)
print(n.count(2))
print(n)

#don't use this because that changes in th main list instead use the copy operation
# m=n
# m[0]=40000
# print(n)
o=n.copy()
o[0]=5677888
print(o)
j=["dinesh","vivek"]
n.extend(j)
print(n)
