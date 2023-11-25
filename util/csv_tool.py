import pandas as pd 
import pyperclip

def csv_to_dict(filename):
    df = pd.read_csv(filename)
    row_names = df.iloc[:,0].tolist()
    list_dict = {}
    for n in range(len(row_names)): 
        list_dict[row_names[n]] = df.iloc[n, 1:].tolist()
    return list_dict

holes = csv_to_dict('iso_holes.csv')
shafts = csv_to_dict('iso_shafts.csv')

pyperclip.copy(str(shafts))