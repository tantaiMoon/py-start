# coding: utf-8

"""
class 声明类，使用驼峰命名的方式定义类  class Name(object):
object 是Python中的一个内置对象

self 参数是类函数中必传的参数，且必须在第一个参数的位置。是一个对象，代表实例化的变量自身。
class Name(object):
  attr = something

  def dn(self):
    print(f'{self.name} is dumping')


lisi = Name()
"""

class Person(object):
  type = 'person'
  name = None
  age= None

  def dump(self):
    print(f'Class type is {self.type}')

  def run(self):
    print(f'{self.name} is running')

  def sleep(): # takes 0 positional arguments but 1 was given
    print(f'sleep')

  def work(self):
    self.run()
    # self.sleep()
    self.dump()


lisi = Person()

print(lisi.name)
lisi.name = 'lisi'
lisi.dump()
lisi.run()

zhangsan = Person()

print(zhangsan.name)
zhangsan.sex = 'm'
print(zhangsan.sex)
zhangsan.work()