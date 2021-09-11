from importFile import *

df = pd.read_csv('../doit_pandas/data/gapminder.tsv', sep='\t')


# 표준 점수 계산
def my_zscore(x):
    return (x - x.mean()) / x.std()


transform_z = df.groupby('year').lifeExp.transform(my_zscore)
# print(transform_z.head())

np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.NaN
print(tips_10)
count_sex = tips_10.groupby('sex').count()


# print(count_sex)


def fill_na_mean(x):
    avg = x.mean()
    return x.fillna(avg)


total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
tips_10['fill_totla_bill'] = total_bill_group_mean
print(tips_10)
