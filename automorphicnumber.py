n=int(input("enter the value "))
t=n**2
count=0
k=n
while n>0:
    n=n//10
    count=count+1
val=t%(10**count)
print(val)
if val==k :
    print("given number is the auto morphic number")
else :
    print("not auto morphic number")