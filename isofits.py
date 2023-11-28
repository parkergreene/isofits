from src.module import *
from src.data import hole_data
from src.data import shaft_data
import sys

#Find iso tolerance
def isofit(body, size, fit, side):
    """Returns ISO tolerance of hole
    Parameters:
    size (float): Size of hole in mm
    fit (str): ISO fit class of hole
    side (str): Select from tolerance band upper, lower, or both
    """
    if body == 'hole':
        body = hole_data
        check_fit_input(body, fit)
    elif body == 'shaft':
        body = shaft_data
        check_fit_input(body, fit)
    else:
        raise ValueError('body must be hole or shaft')
    
    if 3 <= size <= 400:
        return find_tol(body, find_size_index(body,size), fit, side)
    else:
        raise ValueError('Invalid size, enter in range [3, 400]')