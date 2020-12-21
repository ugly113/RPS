import random


# List for computer to choose from
rps = ['rock', 'paper', 'scissors']

# Main game play
def game():
    player = input('R_ock - P_aper - S_cissors? or Q_uit: ')
    computer = random.choice(rps)
    if player.lower() == 'r':
        if computer == 'paper':
            print(f'\nI picked {computer} you lose!')
        elif computer == 'scissors':
            print(f'\nI picked {computer} you win!')
        else:
            print(f'\nI picked {computer} as well, it\'s a tie!')
    elif player.lower() == 'p':
        if computer == 'scissors':
            print(f'\nI picked {computer} you lose!')
        elif computer == 'rock':
            print(f'\nI picked {computer} you win!')
        else:
            print(f'\nI picked {computer} as well, it\'s a tie!')
    elif player.lower() == 's':
        if computer == 'rock':
            print(f'\nI picked {computer} you lose!')
        elif computer == 'paper':
            print(f'\nI picked {computer} you win!')
        else:
            print(f'\nI picked {computer} as well, it\'s a tie!')

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
