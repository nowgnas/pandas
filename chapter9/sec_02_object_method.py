from importFile import *

d1 = '40'
m1 = '46'
s1 = '52.876'
u1 = 'N'

d2 = '73'
m2 = '58'
s2 = '26.866'
u2 = 'w'

coords = ''.join([d1, m1, s1, u1, d2, m2, s2, u2])
# print(coords)

multi_str = '''Guard: what? 
king authur: yes
Guard: hihihi
king
Guard: bye
'''
# print(multi_str)
multi_split_line = multi_str.splitlines()
# print(multi_split_line)

gurad = multi_str.replace('Guard:', '').splitlines()[::2]
print(gurad)
