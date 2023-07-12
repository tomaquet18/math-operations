def calculate_factorial(number):
    if number < 0:
        return "Error: Invalid input for factorial"
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        return factorial