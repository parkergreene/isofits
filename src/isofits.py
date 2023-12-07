from module import *
from data import hole_data
from data import shaft_data
import sys

#Find iso tolerance
def isotol(body, size, fit, side):
    """Returns ISO tolerance of hole/shaft
    Parameters:
    body (str): 'hole' or 'shaft'
    size (float): Size of body [mm]
    fit (str): ISO fit class of body
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
    
def isofit(size, hole_fit, shaft_fit):
    """Returns MMC and LMC for ISO fit of hole/shaft
    Parameters:
    size (float): Size of body [mm]
    hole_fit (str): ISO fit class of hole (ex: 'H7')
    shaft_fit (str): ISO fit class of shaft (ex: 'h6')
    """
    hole_max, hole_min = isotol('hole', size, hole_fit, 'both')
    shaft_max, shaft_min = isotol('shaft', size, shaft_fit, 'both')
    mmc = hole_min - shaft_max
    lmc = hole_max - shaft_min
    return mmc, lmc

def isoreport(size, hole_fit, shaft_fit): 
    """Returns MMC and LMC for ISO fit of hole/shaft
    Parameters:
    size (float): Size of body [mm]
    hole_fit (str): ISO fit class of hole (ex: 'H7')
    shaft_fit (str): ISO fit class of shaft (ex: 'h6')
    """
    mmc, lmc = isofit(size, hole_fit, shaft_fit)
    if mmc >=0 and lmc >=0:
        fit_type = 'Clearance Fit'
    elif mmc <0 and lmc <0:
        fit_type = 'Interference Fit'
    else:
        fit_type = 'Transition Fit'
    print(f'{size} {hole_fit}/{shaft_fit} | {fit_type} | {lmc}, {mmc}')