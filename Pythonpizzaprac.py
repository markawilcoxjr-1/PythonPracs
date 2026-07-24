print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pep = input("Do you want pepperoni? Y or N: ")
ex_ch = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You typed the wrong inputs.")

if pep == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if ex_ch == "Y":
    bill += 1
    
print(f"Your bill is: ${bill} Thank You for choosing Python Pizza!")
