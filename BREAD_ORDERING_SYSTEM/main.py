import sys

print("WELCOME TO BOB BAKER'S BAKERY !")
print("Please we have varieties of bread , we have COCONUT , PAWPAW and NORMAL bread")
#Variety of bread and their prices :
COCONUT = 15
PAWPAW = 15
NORMAL = 10

BILL = 0
DELIVERY = 10
Choice_of_bread = input(f"Please enter your choice of bread:")
if Choice_of_bread == "COCONUT":
    BILL = COCONUT
    print(f"Please your Choice of bread {Choice_of_bread} is GHC{BILL}.00")

elif Choice_of_bread == "PAWPAW":
    BILL = PAWPAW
    print(f"Please your Choice of bread {Choice_of_bread} is GHC{BILL}.00")

elif Choice_of_bread =="NORMAL":
    BILL = NORMAL
    print(f"Please your Choice of bread {Choice_of_bread} is GHC{BILL}.00")

else:
   print(f"Please your input is invalid , check your input again")
   sys.exit()

print(f"Thanks for buying bread from us , we also have delivery service.Do you want the service ?. Enter Y for yes and N for no")
Response = input("Enter your decision , Y and N :")

if Response == "Y":
   BILL += DELIVERY
   print(f"Thanks for buying from us , your total bill is GHC{BILL}.00")
else:
  print(f"Thank your for buying from us , your total is GHC{BILL}.00")