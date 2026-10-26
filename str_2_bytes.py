# coding: utf-8

# 比特 ： 二进制的数据流 bytes ，特殊的字符串


bt = b'hello'
print(bt, type(bt))  # 输出: b'hello' <class 'bytes'>
print(bt.capitalize())
print(bt.upper())
print(bt.lower())
# replace 的参数必须是 bytes 类型，否则会抛出 TypeError 异常
print(bt.replace(b'hello', b'world'))
print(bt[3]) # 108 输出编码
print(bt[3:]) # b'lo'
print(bt.find(b'lo')) # 3

# dir 函数 接收一个对象作为参数，返回该对象的所有属性和方法的列表
print(dir(bt))

print('---- 字符串转换为比特 encode() ----')
# encode() 、 decode() 方法将字符串转换为比特，默认使用 UTF-8 编码,第一个参数为编码格式，第二个参数为错误处理方式，默认为 strict 严格模式，如果遇到无法编码的字符会抛出 UnicodeEncodeError 异常
str = "hello，李四"
bytes_data = str.encode('utf-8')
print(bytes_data, type(bytes_data))  # 输出: b'hello\xef\xbc\x8c\xe6\x9d\x8e\xe5\x9b\x9b' <class 'bytes'>
print(bytes_data.decode('utf-8'))  # 输出: hello