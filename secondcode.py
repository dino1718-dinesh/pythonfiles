i=1
temp=0
temp1=0
for i in range(101):
    print(i)
    if i%2==0 and i%5==0:
        temp=temp+i
    #else:
     #   temp1=temp1+i
    i+=1
print(temp)
print(temp1)