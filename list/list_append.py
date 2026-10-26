# coding: utf-8
# append 在列表末尾添加元素

name_list = ['lisi', 'wangwu', 'zhaoliu']

print(id(name_list))
name_list.append('zhangsan')


print(name_list)

print(id(name_list))

nums = [1.1]
tuple_nums = (1,)
dicts = {'name': 'lisi' }

name_list.append(nums)
name_list.append(tuple_nums)
name_list.append(dicts)
print(name_list)

name_list.append('zhangsan')
name_list.append(True)
print(name_list)