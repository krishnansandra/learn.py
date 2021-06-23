def calculate():
    operation = input('''
Please select the operation you want:
+ for addition
- for subtraction
* for multiplication
/ for division
%  percentage
sqrt for squareroot
power for power of number
''')

    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))

    if operation == '+':
        print(num1, "+", num2, "=", (num1 +num2))
    elif operation == '-':
        print(num1, "-", num2, "=", (num1 -num2))
    elif operation == '*':
        print(num1, "*", num2, "=", (num1 *num2))
    elif operation == '/':
       print(num1, "/", num2, "=", (num1 /num2))
    elif operation == '%':
        print(num1, "%" ,"=", (num1/100))  
    elif operation == 'sqrt':
        print(num1, "sqrt" ,"=", num1**0.5)  
    elif operation == 'power':
        print(num1, "power", num2, "=", num1**num2)
    else:
        print('invalid operation')

calculate()

calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
if calc_again == 'Y':
        calculate()
elif calc_again == 'N':
        print('See you later.')
