import pandas as pd

from importFile import *

df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})


# print(df)

# print(df['a'] ** 2)
def my_sq(x, n):
    return x ** n


sq = df['a'].apply(my_sq, n=2)


# print(sq)
def print_me(x):
    print(x)


# print(df.apply(print_me, axis=1))
# print('-----------')
# print(df.apply(print_me, axis=0))

def avg_3(col):
    x = col[0]
    y = col[1]
    z = col[2]

    return (x + y + z) / 3


def avg_2_apply(col):
    sum = 0
    for item in col:
        sum += item
    return sum / df.shape[0]

#p210
print(df.apply(avg_3))
