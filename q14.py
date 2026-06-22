# n=int(input())


# for i in range(n):
#     k=input()
#     l=list(map(int,input().split()))
#     print(k,l)

# print(k,l)

n=int(input())


for i in range(n):
    if i==0:
        k=input()
        l=list(map(int,input().split()))
    if i==1:
        q=input()
        w=list(map(int,input().split()))
    if i==2:
        e=input()
        r=list(map(int,input().split()))
    
o=input()

if o==k:
    avg = sum(l) / len(l)
    print(avg)
if o==q:
    avg = sum(w) / len(w)
    print(avg)
if o==e:
    avg = sum(r) / len(r)
    print(avg)
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


