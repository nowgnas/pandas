import pandas as pd

from importFile import *

weather = pd.read_csv('../doit_pandas/data/weather.csv')

# print(weather.iloc[:5, :])
weather_melt = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'],
                       var_name='day', value_name='temp')
# print(weather_melt.head())

weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day'],
    columns='element',
    values='temp'
)
# print(weather_tidy)
weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat.head())
