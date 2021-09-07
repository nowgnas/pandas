# p.64
import pandas as pd

from importFile import *

scientist = pd.read_csv('../doit_pandas/data/scientists.csv')

ages = scientist['Age']
# print(ages.max())
# print(ages[ages > ages.mean()])
# print(ages)
# print(ages + ages)
# print(ages * ages)

# print(ages + pd.Series([1, 100]))
# print(pd.Series([1, 100]).shape)
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)
