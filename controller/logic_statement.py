# coding: utf-8

# 逻辑判断与逻辑语句
'''
语法格式：

if bool_reslt:       # 语法块
  do                 # if 块对应的逻辑代码块
elif bool_result1:   # 非第一次的多种判断
  elif1 do           # 不满足 bool_result 但是满足 bool_result1 条件时执行的代码块入口
elif bool_result2:
  elif do
else:                # bool_reslt 的值为 False 时执行
  else do            # if 条件不满足时执行的另一个代码块入口


'''

a = 1

if a > 2:
  print('a > 2')
elif a == 2:
  print('a == 2')
elif 0<a < 2 :
  print('0<a < 2')
else:
  print('a < 0')


info = 'my name is mo'
info_list = info.split()

if info_list[0] == 'mo':
  info_list[0] = 'lisi'

if info_list[1] == 'mo':
  info_list[1] = 'lisi'
elif info_list[-1] == 'mo':
  info_list[-1] = 'lisi'

print(info_list)

# 或
if info_list[0] == 'my' or info_list[3] == 'mo':
  print(info)

# 且
if info_list[0] == 'my' and info_list[3] == 'mo':
  print(info)
else:
  print('且未匹配')


# 且
if info_list[0] == 'my' and info_list[3] == 'lisi':
  print('且匹配：',info)
else:
  print('且未匹配', info_list[0], info_list[3])

for v in info_list:
  print(v)


users = {
  'lisi': {'age': 33, 'count': 90},
  'zs': {'age': 22, 'count': 99},
  'ww': {'age': 17, 'count': 100},
}

xiaoming = ['zhaoliu', 19, 98]

if xiaoming[0] in users:
  xiaoming[0] = '%s_n' % xiaoming[0]
  users[xiaoming[0]] = xiaoming
else:
  users[xiaoming[0]] = xiaoming

print(users)