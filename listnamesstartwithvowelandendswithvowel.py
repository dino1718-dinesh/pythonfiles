n=input("enter the values ").split()
q="aeiou"
for i in n :
    for k in range(1):
        if i[k].lower() in "aeiou" and i[len(i)-1] in "aeiou" :
            print("luck number", i)
       