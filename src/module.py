#find the column number based on size input
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

#match the fit class to input
def find_tol(list_dict, size_index, fit, side):  
    
    ans = list_dict[fit][size_index]
    upper = float(ans.split('\n')[0])
    lower = float(ans.split('\n')[1])
    if side == 'upper':
        return upper
    elif side == 'lower':
        return lower
    elif side == 'both':
        return upper, lower
    else:
        raise 'side must be upper, lower, or both'

def create_fit_lst(body_data):
    fit_lst = list(body_data.keys())
    fit_lst.pop(0)
    fit_lst.pop(0)
    return fit_lst

#check if users fit input is valid 
def check_fit_input(body_data, fit_input):
    fit_lst = create_fit_lst(body_data)
    if fit_input in fit_lst:
        return
    else:
        raise ValueError(f'Invalid fit input ({fit_input}). Enter valid ISO fit class')
    
from data import hole_data

#check_fit_input(hole_data, 'p7')