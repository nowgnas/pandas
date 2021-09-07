from importFile import *

scientist = pd.DataFrame(
    data={'Occupation': ['chemist', 'statistician'],
          'Born': ['1920', '1876'],
          'Died': ['1958', '1937']},
    index=['Rosaline', 'William'],
    columns=['Occupation', 'Born', 'Died'])

first_row = scientist.loc['William']
# print(type(first_row))
# print(first_row)
print(first_row.index)
print(first_row.values)
print(first_row.keys())
