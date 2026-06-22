n= int(input("enter the size of the triangle "))

for i in range (n):
     
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1): 
    
        print("*",end="")
    
        
    print()
#     *
#    ***
#   *****
#  *******
# *********
# spaces = n - i - 1
# stars  = 2*i + 1
# n = int(input("Enter the size of the triangle: "))

# for i in range(n):

#     # Print spaces
#     for k in range(n - i - 1):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i + 1):
#         print("*", end="")

#     # Move to next line
#     print()
# print("*",end="")
# print("dinesh")
# n=int(input())
# if n>-1:
#     print("pos")
# else:
#     print("neg")