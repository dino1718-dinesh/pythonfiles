# divisors of that particular number is sum of that all divisors
i=int(input("enter the value"))
sum=0
count=0
n=1
while n<=i//2:
    if i%n==0:
        sum= sum +n
        count=count+1
    n=n+1

print(sum)
print(count)
# i = int(input("Enter the value: "))
# sum = 0
# count = 0
# n = 1

# while n <= i // 2:
#     if i % n == 0:
#         sum = sum + n
#         count = count + 1

#     n = n + 1

# print("Sum =", sum)
# print("Count =", count)

# if sum == i:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")