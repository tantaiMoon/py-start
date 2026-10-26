# coding: utf-8

"""
类方法的链式调用
p.a.b.c()

 """

class A(object):
  def __init__(self, attr):
    self.__attr = attr

  # def a(self):
  #   print('A is talking')
  #   return self
  def __call__(self, *args, **kwargs):
    print('chain key is {}'.format(self.__attr))
    return self

  def __getattr__(self, key):
    print(f'Attribute [{key}] not found in A')
    if self.__attr:
      key = '{}.{}'.format(self.__attr, key)
    else:
      key = key
    print(f'key is {key}')
    # 递归调用实现链式
    return A(key)


a = A('')
a.a.b.c()  # 输出: A is talking