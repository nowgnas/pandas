from importFile import *

tips_10 = sns.load_dataset('tips').sample(10, random_state=42)
# print(tips_10)

grouped = tips_10.groupby('sex')
# print(grouped.groups)

# 파이썬 짱이다
avgs = grouped.mean()
# print(avgs)

female = grouped.get_group('Female')
# print(female)

# for sex_group in grouped:
#     print(sex_group)

bill_sex_time = tips_10.groupby(['sex', 'time'])
grouped_avg = bill_sex_time.mean()
# print(grouped_avg)
# print(type(grouped_avg))

# EX: 책이랑 좀 다른데??
# print(grouped_avg.index)

group_method = tips_10.groupby(['sex', 'time']).mean().reset_index()
print(group_method)

group_params = tips_10.groupby(['sex', 'time'], as_index=False).mean()
print(group_params)
