x=int(input())
y=int(input())
z=int(input())
n=int(input())

# all permutations of i j k 
results=[]
for i in range(x+1):
    for j in range(y+1):
        for u in range (z+1):
            if i+j+u!=n:
                results.append([i,j,u])

print(results)