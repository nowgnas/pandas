from sec_01_load_data import *

global_year_lifeExp = df.groupby('year')['lifeExp'].mean()

if __name__ == '__main__':
    print(global_year_lifeExp.plot())
    plt.show()
