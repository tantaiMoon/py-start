# coding: utf-8

# 类的构造函数: 类中一种默认的函数，用来在实例化的同时传入参数

class Person(object):
  type = 'person'
  def __init__(self, name, age = None):
    self.name = name
    self.age = age
    print('init')

  def dump(self):
    print(f'Class type is {self.type}')

  def run(self):
    print(f'{self.name} ,age {self.age} is running')


  def work(self):
    self.run()
    self.dump()


l = Person('lisi',22)
l.work()
