
# concepts cover dictionary while loop function with return and main concept recursion

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


# add
def addition(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


# dictionary to keep the keys and values of these function

operation_dict = {
    "+": addition,
    "-": subtract,
    "*": multiply,
    "/": divide
}

'''
    to add new expression like exponent, modulus (%)
 '''
# print(operation_dict)


def calculator():
    num1 = float(input("Enter first number : "))

    # loop over dictionary

    for operator in operation_dict:
        print(operator)

    calculation_continue = True  # flag set to true

    while calculation_continue:
        choose_operator = input("Choose the operation you want to perform. ")
        num2 = float(input("Enter next number: "))
        # to get key from operation_dict{+,-,*,/}
        calculation_function = operation_dict[choose_operator]
        result = calculation_function(num1, num2)
        print(f'{num1} {choose_operator} {num2} = {result}')
        new_Calculation = input(
            f"Type 'Y' to continue with {result} or N for new calculation to over type O :")
        if new_Calculation == 'Y':
            num1 = result
        elif new_Calculation == 'N':
            calculation_continue = False
            calculator()
        else:
            break


calculator()
