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
