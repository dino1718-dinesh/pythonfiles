s1=int(input("enter the s1"))
s2=int(input("enter the s2"))
s3=int(input("enter the s3"))
s4=int(input("enter the s4"))
s5=int(input("enter the s5"))
s6=int(input("enter the s6"))
if s1<=100 and s1>=0 and s2<=100 and s2>=0 and s3<=100 and s3>=0 and s4<=100 and s4>=0 and s5<=100 and s5>=0 and s6<=100 and s6>=0:
    print("correctmarks")
else :
    raise ValueError("Invalid marks! Marks must be between 0 and 100.")


sum=s1+s2+s3+s4+s5+s6
print("the total sum is :",sum)

per=sum/600*100
print("the percentage is :",per)

if 100<=s1>=90 :
    print("a+")
else :
    print("b")


marks = [s1, s2, s3, s4, s5, s6]

for i in range(len(marks)):
    if marks[i] >= 90:
        grade = "A+"
    elif marks[i] >= 80:
        grade = "A"
    elif marks[i] >= 70:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    elif marks[i] >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Subject {i+1} Grade: {grade}")
