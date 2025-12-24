###############################################################
#  Checks the strength of a given password and returns a score.
#  Creation Date:  12/21/2025
#  Revision:  
###############################################################

# Importing necessary libraries
import string

# Taking password input from the user.
password = input("Enter your password: ")

# This functions checks the length of the password.
def check_password_length(password):
    if len(password) > 8 and len(password) < 16:
        return 1
    elif len(password) == 16 or len(password) > 16:
        return 2
    else:
        return 0
    
# This function checks the strength of the password.

def check_password_strength(password):
    if password.isdigit():
        return 0
    elif password.isalpha():
        if password.islower():
            return 0
        elif password.isupper():
            return 0
        else:
            return 1 # Mixed alphabetic (contains both upper and lower)
    else:
        return 2


# This function checks if the password contains any special characters.
def check_special_chars(password):
    if len([x for x in password if x in string.punctuation]) > 0:
        return 2
    else:
        return 0


# This function runs all the tests and returns the final score.

def run_test():
    pass_len = check_password_length(password)
    pass_special = check_special_chars(password)
    pass_strength = check_password_strength(password)

    check_score = pass_len + pass_special + pass_strength
    print("Your password score is", check_score)
    if check_score == 6:
        print("Your password is very strong")
    elif check_score == 5:
        print("Your password is strong")
    elif check_score == 4:
        print("Your password is moderate")
    elif check_score == 3:
        print("Your password is weak")
    elif check_score == 2:
        print("Your password is very weak")
    else:
        print("You should use a password manager to generate a strong password")
        print("Good password practices include using a mix of uppercase and lowercase letters, numbers, and special characters")


run_test()
