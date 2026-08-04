import random

print(r'''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                  ''')

stages = [r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
____|____''', r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
____|____''', r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |       
    |
____|____''', r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |       
    |       
    |
____|____''', r'''
     _______
    |/      |
    |      (_)
    |      \|
    |       
    |       
    |
____|____''', '''
     _______
    |/      |
    |      (_)
    |      
    |       
    |       
    |
____|____''', '''
     _______
    |/      |
    |      
    |      
    |       
    |       
    |
____|____''']

lives = 6

word_list = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward",
             "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon"
             "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle"]
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f">>>>>>YOU HAVE {lives} LIVES LEFT<<<<<<")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"******The word was {chosen_word}, YOU Lose!******")

    if "_" not in display:
        game_over = True
        print("$$$$$$You win!$$$$$$")

    print(stages[lives])