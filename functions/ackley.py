import math


def obj_fun(x):
        first_sum = 0.0
        second_sum = 0.0
        for c in x:
            first_sum += c**2.0
            second_sum += math.cos(2.0*math.pi*c)
        n = float(len(x))
        return -20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20.0 + math.e

def get_bounds():
    return -32,32
