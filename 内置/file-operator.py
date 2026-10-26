# coding: utf-8
import os
import os.path
'''
文件对象 ‘读’ 操作方法
    seek(offset, whence) 方法，移动文件指针到指定位置
    read 方法，读取文件内容，返回整个文件字符串；无参数
    readlines 方法，读取文件列表；无参数
    readline 方法，读取文件一行内容；无参数
    mode 属性，返回文件的打开模式
    name 属性，返回文件的名称
    closed 属性，返回文件是否关闭
'''

f = open(os.path.join(os.getcwd(), 'keyword.py'), 'r') # 打开一个文件，返回一个文件对象

data = f.read() # 读取文件内容，返回整个文件字符串
f.close() # 关闭文件

# print(data)
# print(len(data))

f = open(os.path.join(os.getcwd(), 'keyword.py'), 'r') # 打开一个文件，返回一个文件对象
data = f.readlines() # 读取文件内容，返回一个列表，每一行是一个元素
f.close() # 关闭文件
# print(data)

_data = []
for i in data:
  tmp = i.strip() # 去掉每一行的空格和换行符
  if tmp:
    _data.append(tmp)
# print(data)
# print(_data)
