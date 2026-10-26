# coding: utf-8

# for , while 语句
"""
for item in iterable: # for循环语法块；iterable 表示一切可遍历内容
  print(item)

"""
# 列表、元组、字符串循环
list1 = [1,2,3,4,5,6]
for item in list1:
  if item % 2 == 0:
    print(item)

print('--------for tuple------')
tuples = (1,2,3,4,5)
for item in tuples:
  if item % 2 == 1:
    print(item)


print('--------for str---------')
str1 = 'abcdefg'

for item in str1:
  print(item)

# 字典循环: 使用内置函数 items()  先转为伪列表
m_dict = {'age': 20, 'name': 'lisi', 'sex': 'nv'}
for item in m_dict:
  print(item, ' value is %s' % m_dict[item])

for key, val in m_dict.items():
  print('{} key, value is {}'.format(key, val))


for item in m_dict.items():
  print(item)

d_list = [
  {'name': 'lisi'},
  {'name': 'zhsan'},
]

for item in d_list:
  print(item)
  print(item.get('age'))


# 内置函数 range()
# for item in range(start, stop, step = 1)
for item in range(1, 10):
  print(item)
else: # else 在 for 循环中使用，只有for正常结束才会执行
  print('for 成功结束')


# for 循环实现九九乘法表
for item in range(1, 10):
  for j in range(1, item + 1):
    print('{} * {} = {}'.format(j, item , j * (item)), end = ' ')
  print('')


print('')
"""
while 循环是无限循环模式，但是也是以一定条件为基础，条件不满足时会退出

while 循环语法：

while bool_result:
  do # while 的循环体
"""

count = 10
total = 0
while count < 20:
  print(count, end = '')
  total += count
  count+=1

print('')
print(total)

users = ['1', 2, 3, 4,5]
index = 0
length = len(users)
while index <= length - 1:
  print(users[index])
  index += 1

# 死循环
# while True:



# continue 和 break

total = 0
count = 10
while count < 100:
  if count % 3 == 0:
    break
  count += 1
  total += count
  print(count)

print(total)


users = [
  {'name': 'lisi', 'age': 18, 'sex': 'm'},
  {'name': 'lisi1', 'age': 17, 'sex': 'w'},
  {'name': 'lisi2', 'age': 18, 'sex': 'w'},
  {'name': 'lisi3', 'age': 19, 'sex': 'm'},
]

man = []
for user in users:
  if user.get('sex') == 'w':
    continue
  man.append(user)

print(man)

count = 1
while count < 5:
  print(count)
  count += 1


# while 实现九九乘法表
i = 0
j = 0
while i < 9:
  i+= 1
  while j < 9:
    j += 1
    print('{} * {} = {}'.format(j, i, i * j), end = ' ')
    if  i == j:
      j = 0
      break
  print()