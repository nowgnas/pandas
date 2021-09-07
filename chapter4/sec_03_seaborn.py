import matplotlib.pyplot as plt

from importFile import *

# p.95

tips = sns.load_dataset("tips")

ax = plt.subplots()
# ax = sns.distplot(tips['total_bill'], rug=True)
# ax.set_title('total bill')

# count 그래프
# ax = sns.countplot('day', data=tips)
# ax.set_title('count')

# 다양한 종류의 이변량 그래프 그리기
# ax = sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=False)
# ax.set_title('scatter')

# jointplot 그래프
# joint = sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
# joint.set_axis_labels(xlabel='total bill', ylabel='tip')
# joint.fig.suptitle('joint', fontsize=10, y=1.03)

# 이차원 밀집도 그리기
# ax = sns.kdeplot(data=tips['total_bill'],
#                  data2=tips['tip'],
#                  shade=True)
# ax.set_title('kernel density plot')

# 바 그래프 그리기
# ax = sns.barplot(x='time', y='total_bill', data=tips)
# ax.set_title('bar plot')

# 박스 그래프 그리기
# p.103
# ax = sns.boxplot(x='time', y='total_bill', data=tips)

# 바이올린 그래프
# ax = sns.violinplot(x='time', y='total_bill', data=tips)

# figs = sns.pairplot(tips)

# pair_grid = sns.PairGrid(tips)
# pair_grid = pair_grid.map_upper(sns.regplot)
# pair_grid = pair_grid.map_lower(sns.kdeplot)
# pair_grid = pair_grid.map_diag(sns.distplot, rug=True)

# ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)

# 산점도 관계 그래프 색상 추가
# scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False)

# 산점도 그래프 크기 모양 조절
# 왜 안되는거야
# scatter = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex',
#                      scatter_kws={'s': tips['size'] * 10})

# lmplot 4개 데이터 그룹에 대한 그래ㅐ프 한번에 그리기


plt.show()
