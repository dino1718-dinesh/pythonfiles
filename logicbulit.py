n=input("enter the string")
count=0
g=len(n)
longest=0

for i in range(g):
    k=n[i]
    for j in range(i+1,g):
        if n[i]==n[j]:
            count=count+1
            print("length is between",n[i],"is",count)
            if longest<count :
                longest=count
        else :
           count=count+1
           j=j+1
    i=i+1
    count=0
print("longest:",longest)