import pandas as pd

from importFile import *

now1 = datetime.now()
# print(now1)

now2 = datetime.today()
# print(now2)

t1 = datetime.now()
t2 = datetime(1970, 1, 1)
t3 = datetime(1970, 12, 12, 13, 24, 34)

# print(t3)
diff1 = t1 - t2
# print(diff1)

ebola = pd.read_csv('../doit_pandas/data/country_timeseries.csv')
ebola['data_dt'] = pd.to_datetime(ebola['Date'])
# print(ebola.info())

test_df1 = pd.DataFrame({'order_day': ['01/01/15', '02/01/15', '03/01/15']})

test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
# print(test_df1)

test_df2 = pd.DataFrame({'order_day': ['01-01-15', '02-01-15', '03-01-15']})
test_df2['date_dt'] = pd.to_datetime(test_df2['order_day'], format='%d-%m-%y')
# print(test_df2)

ebola1 = pd.read_csv('../doit_pandas/data/country_timeseries.csv',
                     parse_dates=['Date'])
# print(ebola1.info())

date_series = pd.Series(['2018-05-16', '2018-05-17', '2018-05-18'])
d1 = pd.to_datetime(date_series)
# print(d1)

ebola_ = pd.read_csv('../doit_pandas/data/country_timeseries.csv')
ebola_['date_dt'] = pd.to_datetime(ebola_['Date'])
# print(ebola_[['Date', 'date_dt']].head())

ebola_['year'] = ebola_['date_dt'].dt.year
print(ebola_[['Date', 'date_dt', 'year']].head())
ebola_['month'], ebola_['day'] = (
    ebola_['date_dt'].dt.month, ebola_['date_dt'].dt.day)

print(ebola_[['Date', 'date_dt', 'year', 'month', 'day']].head())
