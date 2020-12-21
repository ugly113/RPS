import random


# List for computer to choose from
rps = ['rock', 'paper', 'scissors']

# Displaying the results
def lose(computer):
    print(f'\nI picked {computer}, you lose!')

def win(computer):
    print(f'\nI picked {computer}, you win!')

def tie(computer):
    print(f'\nI pick {computer} as well, it\'s a tie!')

# Main game play
def game():
    player = input('R_ock - P_aper - S_cissors? or Q_uit: ')
    computer = random.choice(rps)
    if player.lower() == 'r':
        if computer == 'paper':
            lose(computer)
        elif computer == 'scissors':
            win(computer)
        else:
            tie(computer)
    elif player.lower() == 'p':
        if computer == 'scissors':
            lose(computer)
        elif computer == 'rock':
            win(computer)
        else:
            tie(computer)
    elif player.lower() == 's':
        if computer == 'rock':
            lose(computer)
        elif computer == 'paper':
            win(computer)
        else:
            tie(computer)

    elif player.lower() == 'q':
        print(f'\n')
        x_check = input('Are you sure? y/n ')
        if x_check.lower() == 'y':
            exit()
        else:
            print(f'\n')
            game()
    else:
        print(f'\nThat\'s not a choice')
        print(f'\n')
        game()

    print(f'\n')
    game()

if __name__=='__main__':
    game()
