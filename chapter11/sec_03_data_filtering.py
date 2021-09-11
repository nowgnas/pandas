from importFile import *

tips = sns.load_dataset('tips')
# print(tips.shape)
# print(tips['size'].value_counts())

tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
print(tips_filtered.shape)
print(tips_filtered['size'].value_counts())
