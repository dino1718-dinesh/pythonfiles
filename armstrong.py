i=int(input("enter the value"))
temp=0
count=0
n=i
while n>0:
    count= count+1.    # in this first count =1 and n=15 and then count =2 and n=1 and count=3 and n=0
    n = n//10
n=i
for m in range(count) : # here k= 3 and then k=5 and then k=1
    k=n%10
    temp=k**count+temp
    n=n//10

print(temp)
# modulo gives you the reminder final reminder whether it compeletes divide or not
# floor division gives the value without float only int values
# / division gives the float or int depending upon problem


# i = int(input("Enter the value: "))

# temp = 0
# count = 0
# n = i

# while n > 0:
#     count += 1
#     n = n // 10

# n = i

# for m in range(count):
#     k = n % 10
#     temp = k ** count + temp
#     n = n // 10

# print(temp)

# if temp == i:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")