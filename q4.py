# import numpy
# a=int(input())
# n=[]
# for i in range(a):
#     row=list(map(float, input().split()))
#     n.append(row)

# print(numpy.linalg.det(n))
import numpy
a=int(input())
n=[]
for i in range(a):
    row=list(map(float, input().split()))
    n.append(row)

print(float(round(numpy.linalg.det(n))))
        