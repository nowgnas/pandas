from importFile import *

tips = sns.load_dataset("tips")

tips['sex'] = tips['sex'].astype('category')
print(tips.info())
