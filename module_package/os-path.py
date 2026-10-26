#coding: utf-8

import os
import os.path

import sys

# os 模块是 Python 内置的一个模块，提供了丰富的方法来处理文件和目录。

getcwd = os.getcwd() # 获取当前工作目录
print(getcwd) # /Users/username/Desktop

listdir = os.listdir(getcwd) # 获取当前工作目录下的所有文件和目录
print(listdir) # ['file1.txt', 'file2.txt', 'dir1', 'dir2']


new_path = '%s/test1' % getcwd # 拼接路径
# os.mkdir(new_path) # 创建一个新目录

new_path = '%s/test2/abc' % getcwd # 拼接路径

# os.makedirs(new_path) # 创建一个新目录 可以递归创建

# os.mkdir('test3') # 创建一个新目录,默认会创建在当前工作目录下


remove_path = '%s/test1' % getcwd # 拼接路径
#  os.removedirs(remove_path) # 删除一个目录,默认会删除当前工作目录下的目录

# os.rename('%s/test3-1' % getcwd, '%s/test3-2' % getcwd) # 重命名一个目录/文件

# os.removedirs('%s/test3-2/abc' % getcwd) # 删除一个目录,默认会删除当前工作目录下的目录
if os.path.exists('%s/test3-2' % getcwd): # 判断文件或者路径是否存在
  os.rmdir('%s/test3-2' % getcwd) # 删除一个目录,默认会删除当前工作目录下的目录,目录必选为空



'''
path
    exists 文件或者路径是否存在
    isfile 是否是文件
    isdir 是否是目录
    join 拼接路径
    isabs 是否是绝对路径
    abspath 获取绝对路径
    basename 获取文件名
    dirname 获取目录名
    split 分割路径，返回一个元组，包含目录和文件名
    splitext 分割路径，返回一个元组，包含文件名和扩展名
'''

is_exists = os.path.exists('%s/test3-2' % getcwd) # 判断文件或者路径是否存在
print(is_exists) # False

new_path = os.path.join(getcwd, 'test3-2') # 拼接路径
print(new_path) # /Users/username/Desktop/test3-2

is_file = os.path.isfile(new_path) # 判断是否是文件
print(is_file) # False

split_path = os.path.split(new_path) # 分割路径，返回一个元组，包含目录和文件名
print(split_path) # ('/Users/username/Desktop', 'test3-2')

is_dir = os.path.isdir(new_path) # 判断是否是目录
print(is_dir) # False

abs_path = os.path.abspath(new_path) # 获取绝对路径
print(abs_path) # /Users/username/Desktop/test3-2

base_name = os.path.basename(new_path) # 获取文件名
print(base_name) # test3-2

dir_name = os.path.dirname(new_path) # 获取目录名
print(dir_name) # /Users/username/Desktop

split_ext = os.path.splitext(new_path) # 分割路径，返回一个元组，包含文件名和扩展名
print(split_ext) # ('/Users/username/Desktop/test3-2', '')



print('------------------- sys 模块 -------------------')
'''

sys 模块
    modules py 启动时加载的模块列表
    path 返回当前 py 的环境路径
    exit 退出当前 py 解释器
    ncoding 返回当前 py 的默认编码
    argv 返回当前 py 的命令行参数列表，外部传入的参数
    platform 返回当前 py 的平台信息
    version 属性，返回当前 py 的版本信息
    getdefaultencoding 返回当前 py 的默认编码
    executable 返回当前 py 的解释器路径
'''

modules = sys.modules # py 启动时加载的模块列表
print(modules) # {'sys': <module 'sys' (built-in)>, '

# sys.exit(1) # 退出当前 py 解释器,后面代码不再执行
path = sys.path
print(path)

code = sys.getdefaultencoding() # 返回当前 py 的默认编码
print(code) # utf-8

print(sys.platform) # darwin
print(sys.version) # 3.9.1 (default, Dec  8 2020, 07:51:42)

print(sys.executable) # /usr/local/bin/python3.9
print(sys.argv) # ['/Users/username/Desktop/test.py', 'arg1', 'arg2']
command = sys.argv[1] # 获取命令行参数
print(command) # arg1