# conding: utf-8

names = ('lisi', 'wangwu', 'zhaoliu')

names_add = names + names

names_c = names * 3

print(names_add)
print(names_c)

print(len(names_add))
print(len(names_c))

print('lisi' in names_add)
print('zhangsan' in names_c)
print('zhangsan' not in names_c)


name_list = ['lisi', 'wangwu', 'zhaoliu']
name_list_add = name_list + name_list
name_list += ['zhangsan']

print(name_list_add)
print(name_list)
print(len(name_list_add))
print(name_list * 3)