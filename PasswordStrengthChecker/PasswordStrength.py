###############################################################
#  Checks the strength of a given password and returns a score.
#  Creation Date:  12/21/2025
#  Revision:  
###############################################################

# Importing necessary libraries
import string


# ANSI color codes for terminal output
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"



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

def check_numeric_chars(password):
    if any(x.isdigit() for x in password):
        return 1
    else:
        return 0

# This function scores the password based on length, special characters, and strength.
def score_password(pass_len, pass_special, pass_strength, pass_numeric):
    check_score = pass_len + pass_special + pass_strength + pass_numeric
    if check_score >= 6:
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
        return check_score, """You should use a password manager to generate a strong password. Good password practices include using a mix of uppercase and lowercase letters, numbers, and special characters"""



# This function runs all the tests and returns the final score.

def run_test():
    password = get_password()
    pass_len = check_password_length(password)
    pass_special = check_special_chars(password)
    pass_strength = check_password_strength(password)
    pass_numeric = check_numeric_chars(password)
    score, message = score_password(pass_len, pass_special, pass_strength, pass_numeric)
    if score >= 6:
        color = GREEN
    elif score == 5 or score == 4:
        color = YELLOW
    else:
        color = RED
    print(color + "Your password score is: " + str(score) + RESET)
    print(color + message + RESET)

    # Detailed descriptions for each score component
    length_descriptions = {
    2: "strong",
    1: "acceptable",
    0: "too short"
    } 
    special_descriptions = {
    2: "contains special characters",
    0: "no special characters"
    }
    strength_descriptions = {
    2: "strong (mix of letters, numbers, special characters)",
    1: "moderate (mix of letters and numbers)",
    0: "weak (only letters or numbers)"
    }
    numeric_descriptions = {
    1: "contains numeric characters",
    0: "no numeric characters"    
    }

    # Detailed breakdown of the password analysis
    print(BLUE + "---Breakdown---" + RESET)
    print(BLUE + f"Length Score: {pass_len} " + length_descriptions[pass_len] + RESET)
    print(BLUE + f"Special Characters Score: {pass_special} " + special_descriptions[pass_special] + RESET)
    print(BLUE + f"Password Strength Score: {pass_strength} " + strength_descriptions[pass_strength] + RESET)
    print(BLUE + f"Numeric Characters Score: {pass_numeric} " + numeric_descriptions[pass_numeric] + RESET)

while True:
    run_test()
    if input("Do you want to check another password? (yes/no): ").lower() != 'yes':
        color = RED
        exit_message = "Goodbye! Thank you for using my password program."
        print(color + exit_message + RESET)
        break