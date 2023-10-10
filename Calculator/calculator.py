##########################################################
#  Calculator
#  Creation Date:  3/3/2023
#  Revision:  
##########################################################
import sys

print('''
====================================
========== Calculator App ==========
====================================
''')

print('''
Thank you for using the simple calculator, choose your option\n''')

print('Pick your numbers: \n')
    
def menu():
    print('''
    Pick your option to calculate:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit Calculator
    ''')
    choice = input('What funtion would you like to perform?: ')

    if choice == '1':
        addition()
        menu()
    
    if choice == '2':
        subtraction()
        menu()
    
    if choice == '3':
        multiplication()
        menu()
    
    if choice == '4':
            division()
            menu()

    if choice == '5':
        exitScript()

def addition():
    number_1 = input('Enter your first number: ')
    number_2 = input('Enter your second number: ')
    
    try:
        num1 = float(number_1)
        num2 = float(number_2)
    except:
        print('One of your entries was not a number, try again.')
    
    answer = num1 + num2
    print('''
    **************************************
    ******* Calculation Complete *********
    **************************************
    ''')
    print('Addition Answer: ', answer)
    
def subtraction():
    number_1 = input('Enter your first number: ')
    number_2 = input('Enter your second number: ')
    
    try:
        num1 = float(number_1)
        num2 = float(number_2)
    except:
        print('One of your entries was not a number, try again.')
    
    answer = num1 - num2
    print('''
    **************************************
    ******* Calculation Complete *********
    **************************************
    ''')
    print('Subtraction Answer: ', answer)

def multiplication():
    number_1 = input('Enter your first number: ')
    number_2 = input('Enter your second number: ')
    
    try:
        num1 = float(number_1)
        num2 = float(number_2)
    except:
        print('One of your entries was not a number, try again.')
    
    answer = num1 * num2
    print('''
    **************************************
    ******* Calculation Complete *********
    **************************************
    ''')
    print('Multiplication Answer: ', answer)

def division():
    number_1 = input('Enter your first number: ')
    number_2 = input('Enter your second number: ')
    
    try:
        num1 = float(number_1)
        num2 = float(number_2)
    except:
        print('One of your entries was not a number, try again.')
    
    answer = num1 / num2
    print('''
    **************************************
    ******* Calculation Complete *********
    **************************************
    ''')
    print('Division Answer: ', answer)

def exitScript():
    sys.exit()

if __name__ == "__main__":
    menu()
    