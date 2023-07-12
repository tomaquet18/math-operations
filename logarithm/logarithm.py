import math

def calculate_logarithm(number, base):
    if number > 0 and base > 0 and base != 1:
        return math.log(number, base)
    else:
        return "Error: Invalid input for logarithm"