# # n=int(input())
# # l=[i for i in range(n) if i%2==0]
# # print(l)
# o=input()
# f=[k for k in o  if k.lower() in "aeiou"  ]
# print("vowles are:",f) 
# count=len(f)
# print(count)

# g=input()
# print(len(g))



amount=0
dict={"sugar":50,"salt":70,"icecream":80,"dirnks":100}
while True:
    l=input("enter the items what you what after buying press 10 : ")
    if l =="10":
        break
    elif l in dict:
        y=int(input("enter how many want"))
        a=y*dict[l]
        amount=amount+a
    else :
        print("invalid item")
print(amount)

# items = {
#     "apple": 20,
#     "banana": 10,
#     "mango": 30
# }

# amount = 0

# while True:
#     l = input("Enter item name (press 10 to stop): ")

#     if l == "10":
#         break

#     elif l in items:
#         y = int(input("Enter quantity: "))
#         amount += y * items[l]

#     else:
#         print("Item not found")

# print("Total amount:", amount)
