# coding:utf-8
#! /usr/bin/env python



class_count = 51

boys = 28
grils = 23
every_body_pay = 35.5
start_time = 8.00
bus_count = 2
site_every_bus = 30

come_park_time = 10.33

lunch_time = 12.0
lunch_pay = 12.0

leave_park_time = 15.05

come_back_school_time = 5.00

back_pay = 5

def data_type():
    num = int(1) # long 类型在 Python3 中已废弃
    num_f = float(1.12)
    num_f1 = 1.12

    # 字符串是不可变的，变量重新赋值是将另一个字符串赋值给变量而不是修改原来的字符串
    var_str = 'string'
    var_str1 = str('string')

    print('int: ', num)
    print('float: ', num_f, num_f1)
    print('var_str ', var_str, var_str1)

    print('num type is ', type(num))
    print('num _f type is ', type(num_f))
    print('var_str type is ', type(var_str))
    print('var_str 1type is ', type(var_str1))
    print('var_str id is ', id(var_str1))
    print('var_str length(len) is ', len(var_str))


# 内置成员运算符 in
print('今' in '今天是1月3日')
print('今日' not in '今天是1月3日')
# max 函数返回数据中最大的成员
# 中文 > 字母 > 数字 > 英文符号
print(max('今天是1月3日'))
# min 函数返回数据中最小的成员
# 中文 < 字母 < 数字 < 英文符号
print(min('今天是1月3日'))

# 字符串的拼接使用 + 号
print('今天是' + '1月3日')

# 内置数学运算符
# + 加法
# - 减法
# * 乘法
# / 除法


def bool_type():
    bool_true = True
    bool_false = False # 0, 0.0, ''，None,[] ,{} 为 False， 其余为 True
    print('bool_true type is ', type(bool_true))
    print('bool_false type is ', type(bool_false))
    print(bool(1))
    print(bool(0))
    print(bool(0.0))
    print(bool(''))
    print(bool(None))
    print('bool_true value is ', bool_true)
    print('bool_false value is ', bool_false)
    print('bool_true id is ', id(bool_true))
    print('bool_false id is ', id(bool_false))

# 不属于任何数据类型，用于表示空值，固有值为 None
# 不确定类型时可以为变量赋值为 None
def null_type():
    null_value = None
    print(bool(null_value))
    print('null_value type is ', type(null_value))
    print('null_value value is ', null_value)
    print('null_value id is ', id(null_value))

# list 列表，有序可变序列，使用 [] 表示
def list_type():
    list_value = [1, 2, 3, 4, 5]
    print('list_value length is ', len(list_value))
    print('list_value min is ', min(list_value))
    print('list_value type is ', type(list_value))
    list_value = list((1, 2, 3, 4, 5,6))
    print('list_value max is ', max(list_value))
    print('list_value sum is ', sum(list_value))
    print('list_value value is ', list_value)
    print('list_value id is ', id(list_value))

# 元组，有序不可变序列，使用 () 表示，可以存储多种数据结构的队列列表
# 元组中，如果只存在一个元素，后面必须要有一个逗号
# 元组占用的内存空间更小
# 元组不可变，一经创建就不能修改，如果需要修改元组，需要将元组转换为列表
def tuple_type():
    tuple_value = (1, 2, 3, 4, 5)
    tuple_value = tuple((1, 2, 3, 4, 5))
    print('tuple_value type is ', type(tuple_value))
    print('1 in tuple_value is ', 1 in tuple_value)
    print('14 not in tuple_value is ', 14 not in tuple_value)
    print('tuple_value value is ', tuple_value)
    print('tuple_value id is ', id(tuple_value))

def dict_type():
    dict_value = {'name': '张三', 'age': 18}
    print('dict_value type is ', type(dict_value))
    print('dict_value value is ', dict_value)
    print('name in dict_value is ', 'name' in dict_value)
    print('{} is ', bool({}), '{1: "a", 2: "b"} is ', bool({1: 'a', 2: 'b'}))
    print('dict_value length is ', len(dict_value))
    print('dict_value id is ', id(dict_value))

def set_type():
    set_value = {1, 2, 3, 4, 5}
    print('set_value type is ', type(set_value))
    print('set_value value is ', set_value)
    print('set_value id is ', id(set_value))

def complex_type():
    complex_value = 1 + 2j
    print('complex_value type is ', type(complex_value))
    print('complex_value value is ', complex_value)
    print('complex_value id is ', id(complex_value))

if __name__ == '__main__':
    data_type()
    bool_type()
    null_type()
    list_type()
    tuple_type()
    dict_type()
    set_type()
    complex_type()