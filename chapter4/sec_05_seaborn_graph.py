from importFile import *

tips = sns.load_dataset("tips")

# sns.set_style('whitegrid')
# fig, ax = plt.subplots()
# ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)

fig = plt.figure()
seaborn_style = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
for idx, style in enumerate(seaborn_style):
    plot_position = idx + 1
    with sns.axes_style(style):
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(x='time', y='total_bill', data=tips, ax=ax)
        violin.set_title(style)
fig.tight_layout()

plt.show()
