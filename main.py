import secrets
import string
from string import ascii_lowercase, ascii_uppercase
from difflib import SequenceMatcher


def pass_gen(num, capital, symbol):
    char_type = {'lower': ascii_lowercase, 'upper': ascii_uppercase,
                 'special': string.punctuation, 'number': string.digits}

    # lower and number are included by default
    char_choice = ['lower', 'number']
    if capital:
        char_choice += ['upper']
    if symbol:
        char_choice += ['special']

    # check for input of num length 1 or 0
    if capital and symbol and num == 1:
        print("Unable to create password of length 1 with uppercase & special characters.")
        return
    elif num == 0:
        print("Unable to create password of length 0.")
        return

    print("\nPasswords: ")
    password = ''

    for i in range(5):
        # makes sure special or upper are in the generated password
        if 'special' in char_choice or 'upper' in char_choice:

            # SequenceMatcher checks the similarity between strings
            while 'special' in char_choice and SequenceMatcher(None, password, string.punctuation).ratio() == 0 or \
                    'upper' in char_choice and SequenceMatcher(None, password, ascii_uppercase).ratio() == 0:

                password = ''
                for j in range(num):
                    password += str(secrets.choice(char_type[secrets.choice(char_choice)]))
            print(">> ", end="")
            print(password)
            password = ''

        # in the case special and upper aren't needed
        if 'special' not in char_choice and 'upper' not in char_choice:
            for j in range(num):
                password += str(secrets.choice(char_type[secrets.choice(char_choice)]))
            print(">>", password)
            password = ''
    print()


def main():
    print("Welcome to Password Generator 9000!\nSimply type 'exit' at any time to quit!")
    y_n = {'yes': True, 'no': False, 'y': True, 'n': False}

    while True:
        # validates password length
        try:
            num = input("Length of password >> ").lower()
            if num == 'exit':
                return
            num = int(num)
        except ValueError:
            print("Error! Please input a number!")
            continue

        # validates if user wants uppercase letters
        while True:
            up = input("Uppercase Letters? y/n? >> ").lower()
            if up == 'exit':
                return
            if up not in y_n:
                print("Invalid Input!")
                continue
            break
        capital = y_n[up]

        # validates if user wants special characters
        while True:
            symbol = input("Special Characters? y/n? >> ").lower()
            if symbol == 'exit':
                return
            if symbol not in y_n:
                print("Invalid Input!")
                continue
            break
        special = y_n[symbol]

        pass_gen(num, capital, special)


main()
