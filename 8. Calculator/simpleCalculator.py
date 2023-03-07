##########################################################
#  Simple Calculator
#  Creation Date:  3/6/2023
#  Revision:  
##########################################################

print('''
====================================
========== Calculator App ==========
====================================
''')

while 1:
    print('What would you like to do: ')
    print('1. Addition')
    print('2. Subraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        num1 = int(input('Choose first number: '))
        num2 = int(input('Choose second number: '))
        print('********************************')
        print('Your answer is: ', num1 + num2)
        print('********************************\n')

    if choice == 2:
        num1 = int(input('Choose first number: '))
        num2 = int(input('Choose second number: '))
        print('********************************')
        print('Your answer is: ', num1 - num2)
        print('********************************\n')

    if choice == 3:
            num1 = int(input('Choose first number: '))
            num2 = int(input('Choose second number: '))
            print('********************************')
            print('Your answer is: ', num1 * num2)
            print('********************************\n')

    elif choice == 4:
            num1 = int(input('Choose first number: '))
            num2 = int(input('Choose second number: '))
            print('********************************')
            print('** Your answer is: ', num1 / num2)
            print('********************************\n')

    elif choice == 5:
         print('Exiting....')
         break
    else:
        print('Invalid input...try again')

