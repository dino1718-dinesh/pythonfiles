number=int(input("enter mobile number"))
count=0
countseats=0
book=[]
k=0
booked_seats=0
amount_cancel=250
amount=300
r_cancel=0

while number>0:
    count=count+1
    number=number//10

if count > 10:
    raise ValueError("Mobile number cannot have more than 10 digits")
elif count == 10:
    print("Correct number")
else:
    raise ValueError("Mobile number must have 10 digits")

seats=[1,0,1,0,1,0,0,1,1,0,0]

for i in seats:
    if i ==0:
        countseats+=1
        k=k+1
        book.append(k)
    else:
        k=k+1



if countseats>0:
    print("total avaible seats are:",countseats)
else:
    print("not enough seats")


booking=int(input("how many seats you want"))
if booking>countseats:
    print("not enough seats")
else:
    print("choose the seats in the row ",book)

for i in range(booking):
    q=int(input("enter the places where you want "))
    if q in book:
        seats[q-1]=9
        booked_seats=booked_seats+1
    else:
        print("enter valid seat number")
        

print("your seats represent as 9 in row ",seats)

if booked_seats>0:
    amount=300*booked_seats
    print("total amount:",amount)
else:
    print("no seats booked")

cancel_seats=int(input("do you want to cancel any tickets? then how many tickets you want to cancel"))
if cancel_seats>0:
    for i in range(cancel_seats):
        z=int(input("enter the places where you want cancel the seats "))
        if z in book  :
            if seats[z-1]==9:
                seats[z-1]=0
            cancel_seats-=1
            r_cancel+=1
    
    print("thank you for boooking total amount is refunded :",amount_cancel*r_cancel)
    
else:
    print("thank you for boooking total amount is :",amount)