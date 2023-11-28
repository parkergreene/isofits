import pytest
from isofits import * 
from src.module import create_fit_lst
from src.data import hole_data
from src.data import shaft_data
import numpy as np

for _ in range(1000):
    body = np.random.choice(['hole', 'shaft'])
    size = np.random.uniform(3,100)
    if body == 'hole':
        fit = np.random.choice(create_fit_lst(hole_data))
    elif body == 'shaft':
        fit = np.random.choice(create_fit_lst(shaft_data))
    else:
        print('ruh roh raggy')
    ans = isofit(body,size,fit,'both')
    print(f'{body} | {size} | {fit} | both --> {ans}')

