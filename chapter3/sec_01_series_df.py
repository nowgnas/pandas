from importFile import *

s = pd.Series(['Wes MC', 'Createor'], index=['person', 'who'])
print(s)

# data frame
scientist = pd.DataFrame({
    'Name': ['frankllin', 'willam'],
    'Occupation': ['chemist', 'statistician'],
    'Born': ['1920', '1876']
})
print(scientist)

scientist_col = pd.DataFrame(
    data={'Occupation': ['chemist', 'statistician'],
          'Born': ['1920', '1876']
          },
    index=['Rosaline', 'willam'],
    columns=['Occupation', 'Born'])
print(scientist_col)

scientist_dict = pd.DataFrame(OrderedDict([
    ('Name', ['Rosaline', 'Willam']),
    ('Occupation', ['chemist', 'statistician']),
    ('Born', ['1920', '1876'])
]))
print(scientist_dict)
