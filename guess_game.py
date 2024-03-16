import random
from os import system, name
import msvcrt


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

# Colors class for text colors
class Colors:
    RESET = '\033[0m'  # Reset to default color
    RED = '\033[91m'   # Red color
    GREEN = '\033[92m'  # Green color
    YELLOW = '\033[93m'  # Yellow color
    BLUE = '\033[94m'   # Blue color
    MAGENTA = '\033[95m'  # Magenta color
    CYAN = '\033[96m'   # Cyan color
    WHITE = '\033[97m'  # White color


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

        print(Colors.YELLOW + "\n!!! Your number MUST be between 0 and 100 !!!\n" + Colors.RESET)

    except ValueError:
        print(Colors.RED + "\n!!! You MUST type an INTEGER number !!!\n" + Colors.RESET)

    except KeyboardInterrupt:
        clear_screen()

        print(GOODBYE_MESSAGE)
        print("Press any key to exit...")
        msvcrt.getch()

        raise SystemExit

    input_number()


def check_number(n, target):
    print(Colors.CYAN)
    if n == target:
        clear_screen()

        print(Colors.GREEN + CONGRATULATIONS_MESSAGE + Colors.RESET)
        print("Press any key to exit...")
        msvcrt.getch()

        raise SystemExit

    elif n > target:
        print("\nYour guess was too high. Try a smaller number.")

    else:
        print("\nYour guess was too low. Try a larger number.")

    print(Colors.RESET)
    input_number()


input_number()
