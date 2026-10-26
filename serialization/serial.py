# coding: utf-8

# 可序列化的数据类型主要为 dict 字典
# 支持的基本数据类型包括 str、int、float、bool、None，以及嵌套的 list 和 dict
# 函数、类、对象等不可序列化

# json 序列化
'''
    dumps(obj) 将对象 obj 序列化为 JSON 格式的字符串
    loads(s) 将 JSON 格式的字符串 s 反序列化为 Python 对象
'''
from json import dumps, loads
print(dumps({"name": "Alice", "age": 30}))
print(loads('{"name": "Alice", "age": 30}'))
print(loads('false'))
print(loads('true'))
print(loads('null'))


# pickle python 自身的 json 的序列化模块

'''
    dumps(obj) 将对象 obj 序列化为二进制格式的字符串，返回值为 bytes 类型
    loads(bytes_object) 将二进制格式的字符串 bytes_object 反序列化为 Python 对象
'''
from pickle import dumps as pickle_dumps, loads as pickle_loads
print(pickle_dumps({"name": "Alice", "age": 30}))
print(pickle_loads(b'\x80\x05\x95\x1c\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x05Alice\x94\x8c\x03age\x94K\x1eu.'))
