names=list(input("enter the name").split())

for  word in names:
    for i in range(len(word)):
        
        if i%2==0:
            print(word[i],end=" ")
        else:
            print(chr(ord(word[i]) + 1),end=" ")

# names = input("Enter names: ").split()

# for word in names:
#     for i in range(len(word)):
#         if i % 2 == 0: why i am overthinking for smaller problems wtf
#             print(word[i])
#         else:
#             print(chr(ord(word[i]) + 1)) chr(ord(word[i])+1)