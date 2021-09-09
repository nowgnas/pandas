from importFile import *

tips = sns.load_dataset("tips")

tips['sex_str'] = tips['sex'].astype(str)
# print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(str)
# print(tips.dtypes)

tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
# print(tips_sub_miss)
# print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'],
                                            errors='coerce', downcast='float')
print(tips_sub_miss.dtypes)
