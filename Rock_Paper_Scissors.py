import random

#Rock-Paper-Scisor Game logic
def game_logic(user_choice,computer_choice ):


    if user_choice==computer_choice:
        print('Draw')
    elif (user_choice=='rock' and computer_choice=='scissors') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissors' and computer_choice=='paper'):
        print('You Won')
    else: 
        print('I Won')
#Input capturing fom user choice and random generation of computer generation

choices=['rock','paper','scissors']

user_choice = input("Enter your choice among (rock, paper, scissors): ").lower()
if user_choice not in choices:
    print('Enter valid choice')
else:
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    game_logic(user_choice,computer_choice )
    




    
    


