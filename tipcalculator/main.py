#we are developing a tip calculator

print("Welcome to the tip calculator"+"!")
Bill = float(input("What is the total bill that you have to pay ? $"))
Tip = int(input(" What percentage tip will you like to give ? 10 15 20 " ))
people = int(input(" How many number of people are going to share the bill ? " ))
Tip_as_percentage = Tip / 100
Total_tip_amount = Bill * Tip_as_percentage
Total_bill = Bill + Total_tip_amount
Total_bill_person = Total_bill / people
Final_amount = round(Total_bill,2)
print(f"Everyone is to pay : ${Final_amount}")