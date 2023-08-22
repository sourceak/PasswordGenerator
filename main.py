import secrets
from string import ascii_lowercase, ascii_uppercase

def pass_gen(num, capital, spec):
    char_type = {'lower': ascii_lowercase, 'upper': ascii_uppercase,
                 'special': "!@#$%^&*()_+[]{}|;:,.<>?~-", 'number': range(0, 9)}

    char_choice = ['lower', 'number']
    if capital:
        char_choice += ['upper']
    if spec:
        char_choice += ['special']

    print("\nPasswords: ")
    password = ''
    for i in range(5):
        password += '>> '
        for j in range(num):
            password += str(secrets.choice(char_type[secrets.choice(char_choice)]))
        password += '\n'
    return password

def main():
    print("Welcome to Password Generator 9000!\nSimply type 'exit' an any time to quit!")
    y_n = {'yes': True, 'no': False, 'y': True, 'n': False}
    while True:
        try:
            num = input("Length of password >> ").lower()
            if num == 'exit':
                return
            num = int(num)
        except ValueError:
            print("Error! Please input a number!")
            continue
        while True:
            up = input("Uppercase Letters? y/n? >> ").lower()
            if up == 'exit':
                return
            if up not in y_n:
                print("Invalid Input!")
                continue
            break
        capital = y_n[up]
        while True:
            spec = input("Special Characters? y/n? >> ").lower()
            if spec == 'exit':
                return
            if spec not in y_n:
                print("Invalid Input!")
                continue
            break
        special = y_n[spec]
        print(pass_gen(num, capital, special))


main()
