import pandas as pd

from importFile import *

ebola = pd.read_csv('../doit_pandas/data/country_timeseries.csv')
# ebola['date_dt'] = pd.to_datetime(ebola['Date'])
#
# ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
# ebola['month'], ebola['day'] = (
#     ebola['date_dt'].dt.month, ebola['date_dt'].dt.day)

# print(ebola[['Date', 'day', 'outbreak_d']].head())

banks = pd.read_csv('../doit_pandas/data/banklist.csv', parse_dates=[5, 6])
# print(banks.head())

banks['closing_quarter'], banks['closing_year'] = (
    banks['Closing Date'].dt.quarter, banks['Closing Date'].dt.year)
# print(banks.head())
closing_year = banks.groupby(['closing_year']).size()
# print(closing_year)

closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()
# print(closing_year_q)

# fig, ax = plt.subplots()
# ax = closing_year.plot()
# plt.show()

# 안됨??
# pd.core.common.is_list_like = pd.api.types.is_list_like
#
# tesla = pdr.get_data_quandl('TSLA')
# tesla.to_csv('../data/tesla_stock_quandl.csv')

# print(ebola.iloc[:5, :5])
head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
# print(head_range)

ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
ebola_5.reindex(head_range)
# print(ebola_5.iloc[:5, :5])

ebola.index = ebola['Date']

# fig, ax = plt.subplots()
# ax = ebola.iloc[0:, 1:].plot(ax=ax)
# ax.legend(fontsize=7, loc=2, borderaxespad=0.)
# plt.show()

img_ebola = pd.read_csv('../doit_pandas/data/country_timeseries.csv',
                        parse_dates=['Date'])
img_ebola.index = img_ebola['Date']
new_idx = pd.date_range(img_ebola.index.min(), img_ebola.index.max())
# print(new_idx)
new_idx = reversed(new_idx)
# print(new_idx)
img_ebola = img_ebola.reindex(new_idx)
# print(img_ebola.head().iloc[:, :5])
last_valid = ebola.apply(pd.Series.last_valid_index)
# print(last_valid)
earliest_date = ebola.index.min()
shift_values = last_valid - earliest_date

ebola_dict = {}
for idx, col in enumerate(ebola):
    d = shift_values[idx].days
    shifted = ebola[col].shift(d)
    ebola_dict[col] = shifted

ebola_shift = pd.DataFrame(ebola_dict)
