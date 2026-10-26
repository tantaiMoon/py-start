# coding: utf-8

"""
类的高级函数

__str__(self)  # 返回对象的描述信息,当使用 print() 函数打印对象时，会调用该方法

__getattr__(self, key)  # 获取对象的属性值,当访问的属性不存在时，会调用该方法

__setattr__(self, key, value)  # 设置对象的属性值,当给对象的属性赋值时，会调用该方法

__call__(self, *args, **kwargs)  # 当对象被当作函数调用时，会调用该方法

"""

class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f'Person(name={self.name}, age={self.age})'

  def __getattr__(self, key):
    return f'Attribute [{key}] not found'

  def __setattr__(self, key, value):
    print(f'Setting attribute [{key}] to value [{value}]')
    if key not in self.__dict__:
      self.__dict__[key] = value

  def __call__(self, *args, **kwargs):
    print(f'Calling object with args: {args} and kwargs: {kwargs}')


p = Person(name='Alice', age=30)
print(p)  # 输出: Person(name=Alice, age=30)
print(p.gender)  # 输出: Attribute [gender] not found

p.score = 100  # 输出: Setting attribute [score] to value [100]
print(p.score)  # 输出: 100
p(2, name='lisi')  # 输出: Calling object with args: (2,) and kwargs: {'name': 'lisi'}