from importFile import *

scientist = pd.read_csv('../doit_pandas/data/scientists.csv')

names = scientist['Name']
names.to_pickle('output/scientist_name.pickle')
