n=list(map(int,input("enter the values ").split()))
print(n)
count=0

for i in range(len(n)-1):
    for j in range(i,i+1):
        if (n[i]==n[i+1]):  # or n[i-1]
            count=count+1

print("count is :",count)
