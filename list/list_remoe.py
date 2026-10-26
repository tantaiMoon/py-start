# coding: utf-8

# remove 删除列表中指定元素的第一个匹配项，如果没有找到该元素，则会引发 ValueError 异常。

name_list = ['lisi', 'wangwu', 'zhaoliu']

print(name_list.remove('wangwu'))
print(name_list)


del name_list
print(name_list) # NameError: name 'name_list' is not defined