# n=list(map(int,input("enter the name").split()))
# for num in n:
#         if num==0:
#              n.remove(num)
#              n.append(0)
# print(n)

# n = list(map(int, input("enter the numbers ").split()))
# m = 0

# for num in n[:]:    
#     if num == 0:
#         n.remove(0)
#         m = m + 1

# for i in range(m):
#     n.append(0)

# print(n)


n = list(map(int, input().split()))

nums = []
zeros = []

for x in n:
    if x == 0:
        zeros.append(x)
    else:
        nums.append(x)

result = nums + zeros

print(result)