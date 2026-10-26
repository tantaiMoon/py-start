# coding: utf-8

# 列表、元组、集合 之间的转换函数

a_list= [1,2,3]
b_tuple = (1,2,3)
c_set = {1,2,3}

print('str', str(a_list), ',type: ', type(str(a_list)))


#1、 列表 -> 集合  set() 函数；列表 -> 元组 tuple() 函数


print('list -> tuple', tuple(a_list)) # 输出: (1, 2, 3)
print('list -> set', set(a_list)) # 输出: {1, 2, 3}
print(tuple(a_list) == b_tuple) # 输出: True
print(set(a_list) == c_set) # 输出: True


#2、 元组 -> 列表 list() 函数；元组 -> 集合 set() 函数

print('tuple -> list', list(b_tuple)) # 输出: [1, 2, 3]
print('tuple -> set', set(b_tuple)) # 输出: {1, 2, 3}
print(list(b_tuple) == a_list) # 输出: True
print(set(b_tuple) == c_set) # 输出: True

#3、 集合 -> 列表 list() 函数；集合 -> 元组 tuple() 函数

print('set -> list', list(c_set)) # 输出: [1, 2, 3]
print('set -> tuple', tuple(c_set)) # 输出: (1, 2, 3)
# 内存地址不同，但是内容相同
print(list(c_set) is a_list) # 输出: False
print(list(c_set) == a_list) # 输出: True
print(tuple(c_set) is b_tuple) # 输出: False