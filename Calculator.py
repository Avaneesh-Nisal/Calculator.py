print('Here is the list for calculating:')
print('Press 1 for addition')
print('Press 2 for subtraction')
print('Press 3 for multiplication')
print('Press 4 for division')
print('Press 5 for finding remainder')
print('Press 6 for to the power values')
print('Press 7 for quitting')


while True:
    input_operation = int(input('Enter the number of the operation:   '))
    if input_operation == 7:
        break
    Input1 = int(input('Enter the first number:   '))
    Input2 = int(input('Enter the second number:  '))
    
    if input_operation == 1:
        print('The answer is ', Input1 + Input2)
    elif input_operation == 2:
        print('The answer is ', Input1 - Input2)
    elif input_operation == 3:
        print('The answer is ', Input1 * Input2)
    elif input_operation == 4:
        print('The answer is ', Input1 / Input2)
    elif input_operation == 5:
        print('The answer is ', Input1 % Input2)
    elif input_operation == 6:
        print('The answer is ', Input1 ** Input2)
