from importFile import *

ebola = pd.read_csv('../doit_pandas/data/country_timeseries.csv')
# print(ebola.columns)

ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
# print(ebola_long.head())

variable_split = ebola_long.variable.str.split('_')
# print(variable_split)

# print(type(variable_split))
status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)
# print(f'status {status_values.head()} country {country_values.head()}')

ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long.head())
# p.163
