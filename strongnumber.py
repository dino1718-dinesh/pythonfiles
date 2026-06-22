i=int(input("enter the value"))
count=0
n=i
sum=0
fact=1
while n>0 :
    count=count+1
    n=n//10
n=i
print(count)
for a in range (count) :
   k=n%10
   if k>1:
     for b in range (2,k+1):
       fact=fact*b 
     
   else :
     fact=1
   n=n//10
   sum=sum+fact
   fact=1

print(sum)
if sum==i:
   print("strong number")
else:
   print("not strong number")
#  another code 
# n = int(input("enter the value"))
# original = n
# sum = 0

# while n > 0:
#     k = n % 10
#     fact = 1

#     if k > 1:
#         for b in range(2, k + 1):
#             fact = fact * b

#     sum = sum + fact
#     n = n // 10

# if sum == original:
#     print("strong number")
# else:
#     print("not strong number")

