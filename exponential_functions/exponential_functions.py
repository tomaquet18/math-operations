import math

def calculate_exponential(base):
    return math.exp(base)

def calculate_natural_logarithm(number):
    if number > 0:
        return math.log(number)
    else:
        return "Error: Invalid input for natural logarithm"