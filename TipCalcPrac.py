print("Welcome to the Tip Calculator!")
Bill = float(input("What was the total bill? $"))

Tip = int(input("How much tip would you like to give? 10, 12, or 15 percent?"))

People = int(input("How many people to split the bill?"))

Bill_With_Tip = Tip / 100 * Bill + Bill

Total = Bill_With_Tip / People

print("Each person should pay: " ,end="")
print(round(Total, 2))
