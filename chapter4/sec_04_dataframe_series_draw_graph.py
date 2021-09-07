from importFile import *

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
# ax = tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20, ax=ax)
# ax = tips['tip'].plot.kde()

# ax = tips.plot.scatter(x='total_bill', y='tip', ax=ax)

ax = tips.plot.hexbin(x='total_bill', y='tip', ax=ax, gridsize=10)
plt.show()
