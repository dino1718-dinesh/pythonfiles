n=int(input("enter the value"))

for i in range (1,n+1):
    for l in range(n,0,-1): # this is the way to print the reverse of the numbers
        if (l==i):
            print("*",end="")
        else:
             print(l,end="")
       
        
    print( )
    
 

# i=int(input("enter the value"))

# for i in range(1,i+1):
#     print(i,end="")
