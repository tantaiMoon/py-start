# coding: utf-8
print('------------------- 字符串和数字之间的转换 -------------------')
# 字符串和数字之间的转换

# 将字符串转换为整数： 字符串中所有的字符必须是数字字符，且不能有空格，否则会抛出 ValueError 异常

int_str = "123"
int_num = int(int_str)
print('str -> int:',int_num, 'old type: {}, new type: {}'.format(type(int_str), type(int_num)))  # 输出: 123

# 将字符串转换为浮点数： 字符串中可以包含小数点，且不能有空格，否则会抛出 ValueError 异常
float_str = "3.14"
float_num = float(float_str)
print('str -> float:',float_num, 'old type: {}, new type: {}'.format(type(float_str), type(float_num)))  # 输出: 3.14


print('------------------- 数字和字符串之间的转换 -------------------')
# 将整数转换为字符串
int_num = 123
int_str = str(int_num)
print('int -> str:',int_str, 'old type: {}, new type: {}'.format(type(int_num), type(int_str)))  # 输出: "123"

# 将浮点数转换为字符串
float_num = 3.14
float_str = str(float_num)
print('float -> str:',float_str, 'old type: {}, new type: {}'.format(type(float_num), type(float_str)))  # 输出: "3.14"

print('----- 字符串和布尔值之间的转换 -------')
# 将字符串转换为布尔值
bool_str = "True"
bool_val = bool(bool_str)
print('str -> bool:',bool_val, 'old type: {}, new type: {}'.format(type(bool_str), type(bool_val)))  # 输出: True

print('----- 布尔值和字符串之间的转换 -------')
# 将布尔值转换为字符串
bool_val = False
bool_str = str(bool_val)
print('bool -> str:',bool_str, 'old type: {}, new type: {}'.format(type(bool_val), type(bool_str)))  # 输出: "False"

print('------- 字符串和列表之间的转换 split()------')
# 将字符串转换为列表
list_str = "hello"
# list_val = list(list_str)
list_val = list_str.split()  # 如果字符串中有空格，可以使用 split() 方法将其拆分为列表
print('str -> list:',list_val, 'old type: {}, new type: {}'.format(type(list_str), type(list_val)))  # 输出: ['h', 'e', 'l', 'l', 'o']

a= 'a|b|c|d'
print(a.split('|', 1))  # 输出: ['a', 'b|c|d']
print(a.split('|', 2))  # 输出: ['a', 'b', 'c|d']
# split 的参数不能是空字符串

print('----- 列表和字符串之间的转换 join() -------')
# 将列表转换为字符串，列表内的元素不能有数字、字典、元组、None、布尔值等非字符串类型，否则会抛出 TypeError 异常
list_val = ['h', 'e', 'l', 'l', 'o']
list_str = ''.join(list_val)
print('list -> str:',list_str, 'old type: {}, new type: {}'.format(type(list_val), type(list_str)))  # 输出: "hello"
a = ['a', 'b', 'c', 'd']
print('|'.join(a))  # 输出: "a|b|c|d"
print('.'.join(a))  # 输出: "a.b.c.d"

sort_str = 'a b d f i g p q c'
sort_list = sort_str.split()
print('sort_list:', sort_list)
sort_list.sort()
print('sort_list:', sort_list)
print(' '.join(sort_list))

str1 = 'abdfigpqc'
# sorted() 函数可以对可迭代对象进行排序，返回一个新的列表，原来的对象不变
print('sort_str:', sorted(str1))
print('sort_str:', ''.join(sorted(str1)))

print('----- 字符串和元组之间的转换 -------')
# 将字符串转换为元组
tuple_str = "hello"
tuple_val = tuple(tuple_str)
print('str -> tuple:',tuple_val, 'old type: {}, new type: {}'.format(type(tuple_str), type(tuple_val)))  # 输出: ('h', 'e', 'l', 'l', 'o')

print('----- 元组和字符串之间的转换 -------')
# 将元组转换为字符串
tuple_val = ('h', 'e', 'l', 'l', 'o')
tuple_str = ''.join(tuple_val)
print('tuple -> str:',tuple_str, 'old type: {}, new type: {}'.format(type(tuple_val), type(tuple_str)))  # 输出: "hello"

print('----- 字符串和集合之间的转换 -------')
# 将字符串转换为集合
set_str = "hello"
set_val = set(set_str)
print('str -> set:',set_val, 'old type: {}, new type: {}'.format(type(set_str), type(set_val)))  # 输出: {'h', 'e', 'l', 'o'}

print('----- 集合和字符串之间的转换 -------')
# 将集合转换为字符串
set_val = {'h', 'e', 'l', 'o'}
set_str = ''.join(set_val)
print('set -> str:',set_str, 'old type: {}, new type: {}'.format(type(set_val), type(set_str)))  # 输出: "helo"