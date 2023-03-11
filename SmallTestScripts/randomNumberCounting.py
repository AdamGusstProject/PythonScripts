total = 0
count = 0

while True:
    num1 = input('Pick a number: ')
    try:
        guess = int(num1)
    except:
        print('Invalid Input')  

    if num1 == 'done':
        break
    
    elif guess > 0:
        total = total + guess
        count = count + 1

print(total, count, 'Average: ', total/count)
        