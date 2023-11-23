import pandas as pd

df = pd.read_csv('iso_holes.csv')

#print(df.head())

#rows_to_delete = [0, 3]
#
#for item in rows_to_delete:
#    df = df.drop(item)
#

#print(df.head())
print(df)

size = 8
fit = 'H6'

print(df.iloc[0])


#column_values = df.iloc[:,0].tolist()
#print(column_values) 

#df = df.apply(pd.to_numeric, errors='coerce')

#print((df.iloc[0] < size) & size <= df.iloc[1])


#df.iloc[2, df.columns[1:]] = pd.to_numeric(df.iloc[2, df.columns[1:]], errors='coerce')


#row_name = df.iloc[0][0]
#print(row_name)
#df.iloc[0] = pd.to_numeric(df.iloc[0], errors='coerce')
#df.iloc[0][0] = 'over'
#
#print(df.iloc[0][0])

#print(type(df.iloc[0][2]))

#print(df.iloc[4][2])

print(df.head())

#col = (df.loc['over'] < size) & (size <= df.loc['inc.'])
#
#results = col[col].index[0]
#
#print(results)