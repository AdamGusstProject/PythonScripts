###############################################################
#  Checks the strength of a given password and returns a score.
#  Creation Date:  12/21/2025
#  Revision:  
###############################################################

pw = input("Enter your password: ")

print(pw)

print(len(pw))

if len(pw) > 8 and len(pw) < 16:
    print("Your password is of moderate length")
elif len(pw) > 16:
    print("Your password is of good length")
else:
    print("Your password is to short")

