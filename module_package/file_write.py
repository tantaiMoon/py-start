#coding:utf-8

l = ['']

# 创建 python 包的工具方法

import os

def create_package(path):
  if os.path.exists(path):
    raise Exception('路径已存在')
  os.makedirs(path) # 创建一个新目录 可以递归创建
  init_path  = os.path.join(path, '__init__.py') # 拼接路径
  f = open(init_path, 'w') # 创建一个新文件
  f.write('# coding: utf-8\n') # 写入文件内容
  f.close() # 关闭文件


class Open(object):
  def __init__(self, path, mode = 'w', is_return = True):
    self.path = path
    self.mode = mode
    self.is_return = is_return

  def write(self, message):
    f = open(self.path, mode = self.mode)
    if self.is_return:
      message = message + '\n'
    f.write(message)
    f.close() # 关闭文件

  def read(self, is_strip = True):
    with open(self.path, mode = self.mode) as f:
      data = f.read()
    print(data)
    if is_strip:
      data = data.strip()
    return data

  def readlines(self, is_strip = True):
    result = []
    with open(self.path, mode = 'r') as f:
      data = f.readlines()
    for line in data:
      if is_strip:
        tmp = line.strip()
        if tmp:
          result.append(tmp)
      else:
        if line != '':
          result.append(line)
    return result


if __name__ == '__main__':
  current_path = os.getcwd() # 获取当前工作目录
  # path = os.path.join(current_path, 'test_package') # 拼接路径
  # create_package(path) # 创建一个新包

  open_path = os.path.join(current_path, 'test_package', 'test_file.txt') # 拼接路径
  o = Open(open_path, mode = 'r')
  # o.write('test message') # 写入文件内容
  # o.read() # 读取文件内容
  data = o.readlines(is_strip = False) # 读取文件内容
  print(data)