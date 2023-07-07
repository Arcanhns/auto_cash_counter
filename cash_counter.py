import string
import os
import random
from colorama import init, Fore, Style
from pyfiglet import Figlet
from termcolor import colored


while True:

    def generate_code():
        section1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
        section2 = "".join(random.choices(string.digits, k=4))
        section3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
        code = "-".join([section1, section2, section3])
        return code

    f = Figlet(font='slant')
    ascii_text = f.renderText('AUTO COUNTER')

    # Generate rainbow-colored ASCII art
    rainbow_ascii_text = ""
    colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
    for char in ascii_text[:-1]:
        color = random.choice(colors)
        rainbow_ascii_text += colored(char, color)
    rainbow_ascii_text += colored(ascii_text[-1], 'white')  # Set the last character color to white

    print(rainbow_ascii_text)
    
    one_cent = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (1 Cent) coins? "))
    two_cent = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (2 Cent) coins? "))
    five_cent = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (5 Cent) coins? "))
    ten_cent = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (10 Cent) coins? "))
    twenty_cent = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (20 Cent) coins? "))
    fifthy_cent = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (50 Cent) coins? "))
    one_euro = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (1 Eur) coins? "))
    two_euro = float(input(f"{Fore.YELLOW}[+]{Fore.RESET} how many (2 Eur) coins? "))

    result = 0
    default_value = 100
    result = one_cent * 0.01 + two_cent * 0.02 + five_cent * 0.05 + ten_cent * 0.10 + twenty_cent * 0.20 + fifthy_cent * 0.50 + one_cent * 1 + two_euro * 2

    print(f"{result} Euro.")

    if result > default_value:
        result = float(result) - default_value
        print(f"There are {result} extra Euro that you have to withdraw.")
    else:
        print("There's not enough money to elaborate an estimate on the left over.")
        print(result)

    if input("Count again? y/n \n") == str("y"):
        os.system('cls')
    else:
        break

