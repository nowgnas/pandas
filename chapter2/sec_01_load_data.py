import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../doit_pandas/data/gapminder.tsv', sep='\t')

if __name__ == '__main__':
    # head(): 위 5개의 데이터를 보여준다
    print(df.head())

    # df.shape: 데이터의 모양을 보여준다
    print(df.shape)

    # df.columns: 데이터 프레임의 열 이름을 확인할 수 있다
    print(df.columns)

    # df.dtypes, df.info(): 데이터 타입의 속성을 알 수 있음
    print(df.dtypes)
    print(df.info())
