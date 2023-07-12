import math

def calculate_square_root(number):
    if number >= 0:
        return math.sqrt(number)
    else:
        return "Error: Invalid input for square root"