###############################################################
#  Checks the strength of a given password and returns a score.
#  Creation Date:  12/21/2025
#  Revision:  
###############################################################

# Importing necessary libraries
import string

# This function takes the password input from the user.
def get_password():
    password = input("Enter your password: ")
    return password

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


def score_password(pass_len, pass_special, pass_strength):
    check_score = pass_len + pass_special + pass_strength
    if check_score == 6:
        return check_score, "Your password is very strong"
    elif check_score == 5:
        return check_score,"Your password is strong"
    elif check_score == 4:
        return check_score, "Your password is moderate"
    elif check_score == 3:
        return check_score, "Your password is weak"
    elif check_score == 2:
        return check_score, "Your password is very weak"
    else:
        return check_score, """You should use a password manager to generate a strong password. 
        Good password practices include using a mix of uppercase and lowercase letters, numbers, and special characters"""



# This function runs all the tests and returns the final score.

def run_test():
    password = get_password()
    pass_len = check_password_length(password)
    pass_special = check_special_chars(password)
    pass_strength = check_password_strength(password)
    score, message = score_password(pass_len, pass_special, pass_strength)
    print("Your password score is:", score)
    print(message)

run_test()
