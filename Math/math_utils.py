import math

def get_error_percentage(num, target):
    return (1 - abs(target - num) / target) * 100

def get_e_error_percentage(num):
    return get_error_percentage(num, math.e)

def get_pi_error_percentage(num):
    return get_error_percentage(num, math.pi)

