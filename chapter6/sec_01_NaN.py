from importFile import *

visited = pd.read_csv('../doit_pandas/data/survey_visited.csv')
survey = pd.read_csv('../doit_pandas/data/survey_survey.csv')

# print(visited)
# print(survey)

vs = visited.merge(survey, left_on='ident', right_on='taken')
# print(vs)

num_legs = pd.Series({'goat': 4, 'ameoba': nan})
# print(num_legs)
# print(type(num_legs))

gapminder = pd.read_csv('../doit_pandas/data/gapminder.tsv', sep='\t')

life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
# print(life_exp)

# EX: 에러가 왜 뜰까 ????
print(life_exp.loc[range(2000, 2010),])

y2000 = life_exp[life_exp.index > 2000]
# print(y2000)

ebola = pd.read_csv('../doit_pandas/data/country_timeseries.csv')

# print(ebola.count())

num_row = ebola.shape[0]
num_missing = num_row - ebola.count()
# print(num_missing)

# print(np.count_nonzero(ebola.isnull()))
# print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

# print(ebola.Cases_Guinea.value_counts(dropna=False).head())

# 누락값 처리하기
# print(ebola.fillna(0).iloc[0:10, 0:5])
# print(ebola.fillna(method='ffill').iloc[0:10, 0:5])
# print(ebola.fillna(method='bfill').iloc[0:10, 0:5])
# print(ebola.interpolate().iloc[0:10, 0:5])

# 누락값이 포함된 데이터 계산하기
ebola['Cases_multiple'] = ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola[
    'Cases_SierraLeone']
ebola_subset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone',
                             'Cases_multiple']]
print(ebola_subset.head(n=10))
