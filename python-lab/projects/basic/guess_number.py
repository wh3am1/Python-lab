import random
import time
def start():
    """"
    Create the magic number, number or attempts and asking for user input
    """
    global magic_number, attempts
    magic_number = choose_difficulty()
    attempts = 0
    print(f"{'------------------------------': ^10}")
    print("Guess the magic number")
    print("Try to guess the number in as few attempts as possible.")
def choose_difficulty():
    """
    Allow the User to Select the dificulty level
    """
    print("Choose Difficulty")
    print("1. Easy (1-50")
    print("2.Medium (1-100")
    print("3. Hard (1-200")

    while True:
        level = input("Enter 1, 2 or 3: ")
        if level == "1":
            return random.randint(1, 50)
        elif level == "2":
            return random.randint(1, 100)
        elif level == "3":
            return random.randint(1, 200)
        else:
            print("Invalid Choice, Please Enter 1, 2 or 3.")

def check_win(player_guess):
    """
    check if player guess is correct , too high or too low
    """
    if player_guess > magic_number:
        print("Too high! Try a smaller number.")
    elif player_guess < magic_number:
        print("Too low! Try a larger number.")
    elif player_guess == magic_number:
        return True

def play_game():
    """
    Main game loop that start the game , process use rinput, and check for win condiot
    """
    global attempts
    start()

    while True:
        try:
            guess = int(input("Enter your number: "))
            if guess < 1 or guess > 200:
                print("Enter a number betwenn 1 - 200")
                continue
        except ValueError:
            print("Invalid input, please Enter a valid number")
            continue
        attempts += 1
        if check_win(guess):
            print(f"Congratulation! you guessed the number in {attempts}atempts.")
            keep_playing = input("Would you like to play agian? (y/N)")
            if keep_playing.lower() == "y":
                print("ok...")
                print("Starting The Game ...")
                time.sleep(3)
                print(".........")
                time.sleep(2)
                print(".............")
                time.sleep(3)
                print("..................")
                time.sleep(2)
                play_game()
            elif keep_playing.lower() == "n":
                print("Thanks for playing! Have a gread day!")
                break
            else:
                print("Invalid Input. Exiting the game")
                break
play_game()