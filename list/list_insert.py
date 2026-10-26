# coding: utf-8

# insert 在指定位置插入元素

name_list = ['lisi', 'wangwu', 'zhaoliu']

name_list.insert(1, 'zhangsan')

print(name_list)

list1 = [1.1]
tuple_t = (2, 3, )
dicts = {'name': 'lisi', 'age': 18}
name_list.insert(2, list1)
name_list.insert(3, tuple_t)
name_list.insert(5, dicts)
name_list.insert(7, None)
name_list.insert(8, None)
name_list.insert(9, dicts)
print(name_list)