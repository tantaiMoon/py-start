# coding: utf-8

# 对象的生命周期

"""
对象的生命周期： （实例化对象）
__ 开头的类函数都是类的内置函数
  1、__inti__: 对象生命的开始，在内存中分配一个内存快


  2、 __del__: 删除对象，从内存中释放这个内存块

"""
"""
  私有函数与私有变量  类中无法被实例化后的对象调用的函数与变量
  类的内部可以调用私有函数和变量

  定义方法： 在函数或者变量的签名添加 __ 两个下划线定义的函数或变量就是私有的

"""

class Animal (object):
  __cat_type = 'cat'
  def __init__(self, name, sex = 'm'):
    self.__sex = sex
    self.name = name
    print('init animal')

  def run(self):
    result = self.__run()
    print(result)

  def __run(self):
    return f'{self.__cat_type} ,{self.__sex} {self.name} running'

  def dump(self):
    result = self.__dump()
    print(result)

  def __dump(self):
    return f'{self.__cat_type} ,{self.__sex} dump'

cat = Animal(name = 'Tom')
cat.run()
# print(dir(cat))
# cat.__dump() #object has no attribute '__dump'. Did you mean: 'dump'?

class Test(object):
  pass


"""
封装：
  将不对外的私有属性或者方法通过可对外使用的函数而使用。
  保护隐私、明确区分内外
 """

class Parent(object):
  def __init__(self):
    pass

  def __hello(self, data):
    print('hello %s in' % data)

  def helloword(self):
    self.__hello(data = 'word')

p = Parent()
p.helloword()