# this is the coprime prime means 1 and itself can divide the number
def num(k):
    if k<2:
        return False
    else:
        for i in range (2,int(k**0.5)+1): # no need to check beyond the square root for prime numbers
            if k%i==0:
                return False
                break
        else:
            return True

try: 
    n=int(input("enter the values"))
    j=int(input("enter the values"))
except:
    ValueError("enter intergers only")


num(n)
num(j)
 
if abs(n-j)==2 and num(n) and num(j):
    print("twin prime")
else:
    print("not twin prime")


# print(int(25**0.5)+1)
