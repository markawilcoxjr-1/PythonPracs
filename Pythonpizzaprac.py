print("Welcome to Python Pizza Deliveries!")
type = input("What kind of pizza would you like?: Type 'C' for custom. Type 'V' for veggie. Type 'ML' for meat lovers: ")
bill = 0

if type == "V":
   size = input("What size pizza do you want? S, M, or L:")
   if size == "S":
        bill = 15

   elif size == "M":
        bill = 20
   elif size == "L":
        bill = 25
   else:
        print("You typed the wrong inputs.")
   ex_ch = input("Do you want extra cheese? Y or N:")
   ex_veg = input("Do you want extra vegetables? Y or N:")
   if ex_ch == "Y":
        bill += 1
   elif ex_veg == "Y":
       if size == "S":
           bill += 1
       else:
           bill += 2

   print(f"Your bill is: ${bill} Thank You for choosing Python Pizza!")
elif type =="ML":
     size = input("What size pizza do you want? S, M, or L: ")
     if size == "S":
         bill = 15
     elif size == "M":
         bill = 20
     elif size == "L":
         bill = 25
     else:
         print("You typed the wrong inputs.")
     ex_ch = input("Do you want extra cheese? Y or N:")
     if ex_ch == "Y":
        bill += 1

     print(f"Your bill is: ${bill} Thank You for choosing Python Pizza!")
else:
    size = input("What size custom pizza do you want? S, M, or L: ")
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25
    else:
        print("You typed the wrong inputs.")
    ex_ch = input("Do you want extra cheese? Y or N:")
    pep = input("Do you want pepperoni? Y or N:")
    sau = input("Do you want sausage? Y or N:")
    bac = input("Do you want bacon? Y or N:")
    pin = input("Do you want pineapples? Y or N:")
    ban_pep =   input("Do you want banana peppers? Y or N:")
    if ex_ch == "Y":
        bill += 1
    else:
        bill += 3
    if pep == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
    elif sau == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
    elif bac == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
    elif pin == "Y":
        if size == "S":
            bill += 1
        else:
            bill += 2
    elif ban_pep == "Y":
        if size == "S":
            bill += 1
        else:
            bill += 2

    print(f"Your bill is: ${bill} Thank You for choosing Python Pizza!")
