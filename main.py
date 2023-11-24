import pandas as pd
import math

df = pd.read_csv('iso_holes.csv')

#size = 130
#fit = 'E6'

row_names = df.iloc[:,0].tolist()

list_dict = {}
for n in range(len(row_names)): 
    list_dict[row_names[n]] = df.iloc[n, 1:].tolist()

def find_size_index(list_dict, size):
    indices = []
    for index, (over, inc) in enumerate(zip(list_dict['over'], list_dict['inc.'])):
        if size > int(over) and size <= int(inc):
            #print('True')
            indices.append(True)
            return index
        else:
            #print('False')
            indices.append(False)

#print(find_size_index(list_dict, size))

def find_tol(list_dict, size_index, fit, side):
    ans = list_dict[fit][size_index]
    print(ans)

    if ans == 'nan':
        raise ValueError('there is nothing there')

    upper = int(ans.split('\n')[0])
    lower = int(ans.split('\n')[1])
    if side == 'upper':
        return upper
    elif side == 'lower':
        return lower
    elif side == 'both':
        return upper, lower
    else:
        raise 'side must be upper, lower, or both'

def hole_tol(size, fit, side):
    """Returns ISO tolerance of hole
    
    Parameters:
    size (float): Size of hole in mm
    fit (str): ISO fit class of hole
    side (str): Select from tolerance band upper, lower, or both
    """
    return find_tol(list_dict, find_size_index(list_dict,size), fit, side)

print(hole_tol(150, 'J7', 'both'))
