import random
from os import system, name


GOODBYE_MESSAGE = """
╔══════════════════════════════════════════════════════════════╗
║                  Thank you for playing!                      ║
║                                                              ║
║           We hope you enjoyed the Guess Game.                ║
║         Have a great day, and see you next time!             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
HELLO_MESSAGE = """
╔══════════════════════════════════════════════════════════════╗
║                  Welcome to the Guess Game!                  ║
║                                                              ║
║      Try to guess the secret number between 0 and 100.       ║
║            Let's see if you can get it right!                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
CONGRATULATIONS_MESSAGE = """
╔══════════════════════════════════════════════════════════════╗
║             Congratulations! You got it right!               ║
║                                                              ║
║     You guessed the secret number correctly. Great job!      ║
║             Thanks for playing the Guess Game.               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
MIN_NUMBER = 0
MAX_NUMBER = 100


def clear_screen():
    return system('cls' if name == 'nt' else 'clear')


clear_screen()
print(HELLO_MESSAGE)

target: int = random.randint(0, 100)


def input_number():
    try:
        num = int(input("Type a integer number: "))

        if num <= MAX_NUMBER and num >= MIN_NUMBER:
            check_number(num, target)

        print("\n!!! Your number MUST be between 0 and 100 !!!\n")

    except ValueError:
        print("\n!!! You MUST type an INTEGER number !!!\n")

    except KeyboardInterrupt:
        clear_screen()
        print(GOODBYE_MESSAGE)
        raise SystemExit

    input_number()


def check_number(n, target):
    if n == target:
        clear_screen()
        print(CONGRATULATIONS_MESSAGE)
        raise SystemExit
    elif n > target:
        print("\nYour guess was too high. Try a smaller number.\n")
    else:
        print("\nYour guess was too low. Try a larger number.\n")

    input_number()


input_number()
