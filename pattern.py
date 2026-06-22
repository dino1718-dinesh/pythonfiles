# 12345
# 1234*
# 123**
# 1****
# *****

n=int(input("enter the value"))
k=n

for i in range(0,n):
    for j in range(1,n+1):
        if (j>=k-i+1):
            print("*",end="")
        else:
            print(j,end="")
        
    
    print()
    