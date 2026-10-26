# coding: utf-8

"""
装饰器：

def out(func_args):                      外围函数
  def inter(*args,**kwargs):             内嵌函数
    return func_args(*args,**kwargs)
  return inter                           外围函数返回内嵌函数

用法：
  1、 交被调用的函数直接作为参数传入装饰器的外围函数
  将装饰器与被调用函数绑定在一起
  @符号+装饰器函数放在被调用函数的上一行



 """

def decorator_check(func_args):
  print(func_args)
  def inner(*args, **kwargs):
    print(args, kwargs)
    result = func_args(*args, **kwargs)
    if result == 'ok':
      return 'result is %s' % result
    else:
      return 'result is failed: %s' % result
  return inner


@decorator_check
def test(data):
  return data

result = test('no')
print(result)

result = test(data = 'ok')
print(result)


# classmethod 装饰器 将类函数可以不经过实例化而直接被调用
# staticthod 装饰器 将类函数可以不经过实例化而直接被调用,staticmethod 装饰器修饰的函数不允许传递 self 或者  cls ，且无法再该函数内部调用其他类函数或变量
# property 将类函数的执行免去括弧，类似于调用属性（变量）
"""
@classmethod
def func(cls, ...):    cls 替代普通类函数中的 self ，代表当前操作的是类
  do

@staticmethod
def st(...):
  do

@property
def fn(self):
  do

 """

class Parent(object):
  __name  =''
  def __init__(self, name):
    self.__name = name
  @classmethod
  def fn(cls):
    # cls.run() # missing 1 required positional argument: 'self'
    print(cls)

  def run(self):
    print('run is no classmethod')
    self.fn()

  @staticmethod
  def static_fn(): # 不允许传递 self 或者  cls
    print('staticmethod 函数')

  @property
  def p_fn(self):
    print(self.__name, 'property 修饰方法')

  @p_fn.setter
  def p_fn(self, value):
    self.__name = value

p = Parent('isi')
p.fn()

print('直接调用 classmethod 装饰器装饰的方法')
Parent.fn()

Parent.static_fn()
p.p_fn # 直接以属性访问的方式进行调用

p.p_fn = 'ww'
p.p_fn


