n=input("enter the string")
k=len(n)-1
j=""
while k>=0:
    j=j+n[k]
    k=k-1
print(j)

if j==n :
    print("palindrome")
else:
    print("not a palindrome")



    # best way to write the reverse palindrome
#     n = input("enter the string")

# left = 0
# right = len(n) - 1

# while left < right:
#     if n[left] != n[right]:
#         print("not palindrome")
#         break
#     left += 1
#     right -= 1
# else:
#     print("palindrome")