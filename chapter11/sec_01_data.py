import numpy as np

from importFile import *

df = pd.read_csv('../doit_pandas/data/gapminder.tsv', sep='\t')
years = df.year.unique()
# print(years)

y1951 = df.loc[df.year == 1957, :]
y1951_mean = y1951.lifeExp.mean()


# print(y1951)
def my_mean(values):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return sum / n


# ??
agg_my_mean = df.groupby('year').lifeExp.agg(my_mean)


# print(agg_my_mean)

def my_mean_diff(values, diff_value):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    mean = sum / n
    return mean - diff_value


globla_mean = df.lifeExp.mean()
# print(globla_mean)
agg_mean_diff = df.groupby('year').lifeExp.agg(my_mean_diff, diff_value=globla_mean)
# print(agg_mean_diff)

gdf = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
# print(gdf)

gdf_dict = df.groupby('year').agg(
    {'lifeExp': 'mean', 'pop': 'median', 'gdpPercap': 'median'})
# print(gdf_dict)

