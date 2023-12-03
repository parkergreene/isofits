import pytest
from isofits import * 
from src.module import create_fit_lst
from src.data import hole_data
from src.data import shaft_data
import numpy as np

def test_isotol(n):
    for _ in range(n):
        body = np.random.choice(['hole', 'shaft'])
        size = np.random.uniform(3,100)
        if body == 'hole':
            fit = np.random.choice(create_fit_lst(hole_data))
        elif body == 'shaft':
            fit = np.random.choice(create_fit_lst(shaft_data))
        else:
            print('ruh roh raggy')
        ans = isotol(body,size,fit,'both')
        print(f'{body} | {size:0.2f} | {fit} | both --> {ans}')

#test_isotol(1000)

isofit(10, 'H7', 'h6')

isoreport(10, 'H7', 'h6')