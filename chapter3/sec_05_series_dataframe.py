from importFile import *

scientist = pd.read_csv('../doit_pandas/data/scientists.csv')

born_datetime = pd.to_datetime(scientist['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientist['Died'], format='%Y-%m-%d')

print(born_datetime)

scientist['born_dt'], scientist['died_dt'] = (born_datetime, died_datetime)
print(scientist.head())
scientist_dropped = scientist.drop(['Age'], axis=1)

