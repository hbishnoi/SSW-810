""" Implement a Rock, Paper and Scissors game where human plays against computer who randomly chooses a move. """    

from random import choice

print('---Rules for this game--- \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock')
print('R is Rock, P is Paper, S is Scissors and Q is to Quit the game.\n')

def get_computer_move() -> str:
    """ randomly choose and return one of 'rock', 'paper', 'scissors' """    
    move: str = choice(['rock', 'paper', 'scissors'])
    return move

def get_human_move() -> str:
    """ask human to choose from 'rock', 'paper', 'scissors'"""
    while True:
        user_input: str = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ").upper()
        if user_input == "R":
            user_input = "rock"
            return user_input
        elif user_input == "P":
            user_input = "paper"
            return user_input
        elif user_input == "S":
            user_input = "scissors"
            return user_input
        elif user_input == "Q":
            user_input = "quit"
            return user_input
        else:
            print ("Please respond in 'R', 'P', 'S', or 'Q' only")
            continue

def main() -> None:

    while True:
        human: str = get_human_move()
        computer: str = get_computer_move()

        if human == 'quit':  # human wants to quit
            # print("Thanks for playing! Visit again")
            break
        elif(human == computer):  # human and computer makes the same
            print ("Tie: we both chose",human)
        elif (human == "rock" and computer == "scissors"):
            print (human,'beats', computer,'- You win')
        elif (human == "rock" and computer == "paper"):
            print (computer,'beats', human,'- I win')
        elif (human == "scissors" and computer == "rock"):
            print (computer,'beats', human,'- I win')
        elif (human == "scissors" and computer == "paper"):
            print (human,'beats', computer,'- You win')
        elif (human == "paper" and computer == "rock"):
            print (human,'beats', computer,'- You win')
        elif (human == "paper" and computer == "scissors"):
            print (computer,'beats', human,'- I win')
    print("Thanks for playing! Visit again")
    

if __name__ == "__main__":
    main()