# n=list(map(int,input("enter the value").split()))

n=[]
vowels=0
cons=0

i =int(input("enter the value"))
for j in range (i):
    m=input("enter the value")
    n.append(m)
# for r in n:
#     for j in  r :
        # if j in "aeiou":
        #     print("vowels are:",j)
        #     vowels=vowels+1
        # else:
        #     print("consonants are :",j)
        #     cons=cons+1

for r in range(len(n)):
    for j in range(len(n[r])):
        if n[r][j].lower() in "aeiou" :
            print("vowels are:",n[r][j])
            vowels=vowels+1
        else:
            print("consonants are :",n[r][j])
            cons=cons+1

print( "total vowels are :",vowels)
print("total constants are :",cons)


