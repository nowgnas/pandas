# p.90
from importFile import *

tips = sns.load_dataset('tips')
print(tips.head())

fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)


# histogram
# axes1.hist(tips['total_bill'], bins=10)
# axes1.set_title("Histogram")
# axes1.set_xlabel('Freq')
# axes1.set_ylabel('Bill')

# scatter
# axes1.scatter(tips['total_bill'], tips['tip'])
# axes1.set_title('scatter plot')
# axes1.set_xlabel('total bill')
# axes1.set_ylabel('tip')

# boxplot
# axes1.boxplot([tips[tips['sex'] == "Female"]['tip'],
#                tips[tips['sex'] == "Male"]['tip']],
#               labels=['Female', 'Male'])
def recode_sex(sex):
    if sex == "Female":
        return 0
    else:
        return 1


tips['sex_color'] = tips['sex'].apply(recode_sex)

axes1.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size'] * 10,
    c=tips['sex_color'],
    alpha=0.5)
axes1.set_title('bill VS tip color')
axes1.set_xlabel('total bill')
axes1.set_ylabel('tip')

plt.show()
