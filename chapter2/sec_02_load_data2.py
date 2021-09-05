from sec_01_load_data import *

# 원하는 열을 출력
country_df = df['country']

# 2개 이상의 열을 출력 할 경우
subset = df[['country', 'continent', 'year']]
sub_loc = df.loc[0]
sub_tail = df.tail(n=1)
sub_sli = df.loc[:, ['year', 'pop']]

small_range = list(range(5))
sub_range = df.iloc[:, list(range(5))]

if __name__ == '__main__':
    print(sub_range.head())
    print(sub_sli.head())
    # print(type(country_df))
    # print(country_df.head())
    # print(country_df.tail())
    # print('--------------------------')
    # print(subset.head())
    # print(df.loc[0])
    # print(df.tail(n=1))
    # print(df.loc[[0, 99, 999]])
    # print(type(sub_loc))
    # print(type(sub_tail))
    print('--------------------------')
    print(df.iloc[1])
    print()
