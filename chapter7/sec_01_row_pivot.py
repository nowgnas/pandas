from importFile import *

# p.156
pew = pd.read_csv('../doit_pandas/data/pew.csv')
# print(pew.head())
# print(pew.iloc[:, 0:6])
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
# print(pew_long.head())

billboard = pd.read_csv('../doit_pandas/data/billboard.csv')

# print(billboard.iloc[0:5, 0:16])
billboard_long = pd.melt(billboard,
                         id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week', value_name='rating')
print(billboard_long.head())
