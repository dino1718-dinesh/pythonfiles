list = [2,3,4,5,6,556,7788,9999,-2,-55,777,5,6,8,90,100]

n = int(input("enter a number"))
k=0

# for i in range(n+1, max(list)+1):
#     if i in list:
#         print(i)
#         break
#     else:
#         print(f"{n} itself greater")

min=list[0]
max=list[0]
for i in range(1,len(list)):
    if max<list[i]:
        max=list[i]
print(max)
for i in range(1,len(list)):
    if max>list[i]:
        max=list[i]
print(min)
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
for i in range(len(list)):
    if n<list[i]:
        k=list[i]
        break

print(k)


