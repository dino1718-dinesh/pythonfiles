
# # ruppes=50
# # time="evening"
# # n= f" pasta only {ruppes} until {time}"

# # print(n)

# # print(type(int(f"{6*10}")))
# # pi = 3.14159265
# # print(f"Pi = {pi:.2f}")



# amount = 1000

# def withdraw():
#     # global amount
#     amount = amount - 100

# withdraw()
# print(amount)
import time
amount = 10000
def withdraw():
    global amount
    am = int(input("enter the amount to withdraw "))
    if am <= amount and am > 0:
        if am % 100 == 0:
            amount -= am
            print("withdraw success",am,"total balance",amount)
            
            time.sleep(5)
            print("thanks for using fruad bank")
        else:
            pass
    else:
        print("insufficient balance")
def deposit():
    global amount
    dep = int(input("enter the amount to depsoit "))
    amount+=dep
    print("depsoit succesfull",dep,"total balance",amount)
def balance():
    global amount
    print("total balance:",amount)
def transfer():
    global amount
    tra=int(input("enter the amount to trans "))
    amount-=tra
    print("total transfer:",tra,"total bal",amount)

    
withdraw()
deposit()
balance()
transfer()

