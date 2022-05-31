import random


def game():
    game_on = True

    cpu_choice = random.choice(['rock', 'paper', 'scissors'])
    user = input('Enter your name:\n').lower()
    user_input = input('Enter your choice: "R" for rock, "P" for paper, "S" for scissors:\n').upper()

    while game_on:

        if cpu_choice == 'rock':
            if user_input == 'R':
                print('It is a tie')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            elif user_input == 'P':
                print(f'{user} wins computer lose')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            elif user_input == 'S':
                print(f'{user} lose computer wins')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            else:
                print('Input the correct choice')
                game()

        elif cpu_choice == 'paper':
            if user_input == 'R':
                print(f'{user} lose computer wins')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            elif user_input == 'P':
                print('It is a tie')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            elif user_input == 'S':
                print(f'{user} wins computer lose')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            else:
                print('Input the correct choice')
                game()

        else:
            if user_input == 'R':
                print(f'{user} wins computer lose')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            elif user_input == 'P':
                print(f'{user} lose computer wins')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            elif user_input == 'S':
                print('It is a tie')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    game_on = False
            else:
                print('Input the correct choice')
                game()


game()
