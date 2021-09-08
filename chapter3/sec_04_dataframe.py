from importFile import *

scientist = pd.read_csv('../doit_pandas/data/scientists.csv')

# print(scientist[scientist['Age'] > scientist['Age'].mean()])
print(scientist.loc[[True, True, False, True]])  # 안됨
print(scientist.loc[[True, True, False, True, True, True, False, True]])  # 됨
