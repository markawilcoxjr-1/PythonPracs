import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors:\n "))
computer_choice = random.randint(0,2)


if user_choice >= 3 or computer_choice > 0:
    print('You\'ve typed an invalid number. You lose!')
elif user_choice == 0 and computer_choice == 2:
    print('You Win!')
elif computer_choice == 0 and user_choice == 2:
    print('You Lose!')
elif computer_choice > user_choice:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif computer_choice == user_choice:
    print('It\'s a Draw!')

print(f'Computer chose {computer_choice}') 