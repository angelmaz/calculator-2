"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("write your equation: ")
    token = user_input.split(' ')
    if token[0] == "q":
        break
    elif len(token) < 2:
        print("to little tokens")
        continue

    
    sign = token[0]
    if not token[1].isdigit():
        print("it's not a number")
        continue
    num1 = float(token[1])
    if len(token) >= 3:
        if not token[2].isdigit():
            print("is not a number")
            continue
        num2 = float(token[2])
    
    

    if sign == "+":
        result = add(num1, num2)
    elif sign == "-":
        result = subtract(num1, num2)
    elif sign == "*":
        result = multiply(num1, num2)
    elif sign == "/":
        result = divide(num1, num2)
    elif sign == "pow":
        result = power(num1, num2)
    elif sign == "mod":
        result = mod(num1, num2)
    elif sign == "square":
        result = square(num1)
    elif sign == "cube":
        result = cube(num1)
    print(result)
