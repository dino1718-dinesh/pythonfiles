x=int(input("enter the value "))

match x:
    case 1:
        print("hii")
    case 2:
        print("hello")
    case 3:
        print("hey there")
    case _ if x==10 :
        print("namaste")
    case _:
        print("not interested")
    