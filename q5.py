# n=5

# k=5
# points=0
# for i in range (1,n+1):
    
#     q=int(input("enter no"))
#     if i==1 and q==k :
#         points=points+10
#     elif i==2 and q==k :
#         points=points+8
#     elif i==3 and q==k:
#         points=points+6
#     elif i==4 and q==k:
#         points=points+4
#     elif i==5 and q==k:
#         points=points+2
#     else:
#         print("enter correct value")
#     if q==5:
#         break

# print("you points are ",points)
    

n = 5
k = 5
points = 0

for i in range(1, n + 1):

    try:
        q = int(input("enter no: "))
    except ValueError:
        print("Please enter a valid integer!")
        continue

    if i == 1 and q == k:
        points += 10
    elif i == 2 and q == k:
        points += 8
    elif i == 3 and q == k:
        points += 6
    elif i == 4 and q == k:
        points += 4
    elif i == 5 and q == k:
        points += 2
    else:
        print("enter correct value")

    if q == 5:
        break

print("your points are", points)