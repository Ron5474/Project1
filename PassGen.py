import string
import random

print("Hello!")
print("You are here to generate or store a password!")
option1 = input("What would you like to do today?(Save or Generate) ")


#Password Generation
if option1.lower() == 'generate':
    pass_number = int(input("How many passwords would you like to generate: "))
    for x in range(0, pass_number):
        pass_length = int(input("How many characters would You like for the password: "))
        lower_case = input("Would You like Your password to contain lower case characters? (Y/N)")
        if lower_case.lower() == 'y' or lower_case.lower() == 'yes':
            lower = string.ascii_lowercase
            upper_case = input("Would You like Your password to contain upper case characters? (Y/N)")
        elif lower_case.lower() == 'n' or lower_case.lower() == 'no':
            lower = ''
            upper_case = input("Would You like Your password to contain upper case characters? (Y/N)")
        else:
            print("Invalid Choice")

        if upper_case.lower() == 'y' or upper_case.lower() == 'yes':
            upper = string.ascii_uppercase
            digits_case = input("Would You like Your password to contain digits characters? (Y/N)")
        elif upper_case.lower() == 'n' or upper_case.lower() == 'no':
            upper = ''
            digits_case = input("Would You like Your password to contain digits characters? (Y/N)")
        else:
            print("Invalid Choice")

        if digits_case.lower() == 'y' or digits_case.lower() == 'yes':
            digits = string.digits
            symbols_case = input("Would You like Your password to contain symbols characters? (Y/N)")
        elif digits_case.lower() == 'n' or digits_case.lower() == 'no':
            digits = ''
            symbols_case = input("Would You like Your password to contain symbols characters? (Y/N)")
        else:
            print("Invalid Choice")

        if symbols_case.lower() == 'y' or symbols_case.lower() == 'yes':
            symbols = string.punctuation
        elif symbols_case.lower() == 'n' or symbols_case.lower() == 'no':
            symbols = ''
        else:
            print("Invalid Choice")

        combination = lower + upper + digits + symbols

        pass_example = random.sample(combination, pass_length)

        password = ''.join(pass_example)
        print(password)

        k = input("Would You like to store this password?(y/n) ")
        if k.lower() == 'y' or k.lower() == 'yes':
            list1 = [password]
            print(list1)

#Password Storage        
elif option1.lower() == 'save':
    list2 = []
    saved_passwords = int(input("How many Passwords would You like to store: "))
    for passwords in range(0, saved_passwords):
        z = input(f"Enter Password {passwords + 1} to be saved: ")
        list2.append(z)
        print(', '.join(list2))
else:
    print("Error! Wrong Choice")