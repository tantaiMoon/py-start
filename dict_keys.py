# coding: utf-8

# 字典方法 keys ： 返回字典中所有键的伪列表（无法操作）
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.keys())  # 输出: dict_keys(['a', 'b', 'c'])

list_keys = list(my_dict.keys())  # 将 dict_keys 转换为列表
print(list_keys)  # 输出: ['a', 'b', 'c']


# 字典方法 get ： 获取指定键的值，如果键不存在则返回 None 或指定的默认值
print(my_dict.get('a'))  # 输出: 1
print(my_dict.get('d'))  # 输出: None
print(my_dict.get('f', '默认值'))  # 输出: 默认值

# print(my_dict['d']) # 输出: KeyError: 'd'，因为键 'd' 不存在

# clear 方法：清空字典中的所有键值对
my_dict.clear()
print(my_dict)  # 输出: {}

# pop 方法：删除指定键并返回其对应的值，如果键不存在则返回默认值或抛出 KeyError
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')  # 删除键 'b' 并返回其对应的值
print(value)  # 输出: 2
print(my_dict)  # 输出: {'a': 1, 'c': 3}7

del my_dict['a']  # 删除键 'a'
print(my_dict)  # 输出: {'c': 3}

del my_dict
# print(my_dict)  # 输出: NameError: name 'my_dict' is not defined，因为 my_dict 已被删除



# copy 方法返回一个一模一样的内存地址不同的字典，没有参数
old_dict = {'name': 'lisi', 'age': 20}

new_dict = old_dict.copy()

print(old_dict)
print(new_dict)
print('old: ', id(old_dict), ' new :', id(new_dict))


new_dict['drangle'] = 1
new_dict.update({'name': 'zhangsan'})

print(old_dict)
print(new_dict)

# popitem 方法删除当前字典中末尾一组元素，返回别删除的元素的键值对，使用元素来包裹， 0 为 可以，1为 value。如果字典为空会抛出异常

res = old_dict.popitem()
print('被删除的是{}, 对应的值是 {}'.format(res[0], res[1]))

print(bool(len(new_dict)))
print(bool('name' in new_dict))
print(bool('age' not in new_dict))