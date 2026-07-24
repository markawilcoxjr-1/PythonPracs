print("Welcone to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Youth admission is $5")
   elif age >= 45 and age <=55:
        bill = 0
print("Youth admission is $FREE")
 elif age <= 18:
        bill = 7
        print("Young adult admission is $7")
    else:
        bill = 12
        print("Adult admission is $12")

    Photo = input("Do you want to have your photo taken? Type Y for yes and N for no")
    if Photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you can not ride this ride.")





