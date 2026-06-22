name=input("enter the string")
v=0
c=0
for character in name :
    if  character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        v = v + 1
        
    else:
        c=c+1
print(v)
print(c)

# or we can use the if character in "aeiou"