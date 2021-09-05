from sec_01_load_data import *

grouped_year_df = df.groupby('year')
lifeExp = grouped_year_df['lifeExp']

unique = df.groupby('continent')['country'].nunique()
if __name__ == '__main__':
    print(unique)
