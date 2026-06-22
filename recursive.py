# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))


#fibbonaci
def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
    
    
for i in range(11):
    print(f(i))
# print(f(3))