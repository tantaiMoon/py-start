# coding: utf-8

# python 中子类继承父类的方法而是用的关键字
# super(CName, self) 函数的参数在 3.x 中可以省略，默认是当前类和当前对象

class P(object):
  def __init__(self, name):
    print('P init')
    self.name = name

class C(P):
  def __init__(self, name, age):
    print('C init')
    super().__init__(name) # 调用父类的构造方法
    self.age = age

c = C(name="Alice", age=10)
print(c.name)  # 输出: Alice
print(c.age)   # 输出: 10


# 多重继承，继承多个基（父）类

class A(object):
  def talk(self):
    print('A is talking')
    return 'A is talking'

class B(object):
  def talk(self):
    print('B is talking')
    return 'B is talking'


class C(A, B):
  pass
  # def talk(self):
  #   print('C is talking')
  #   return 'C is talking'

c = C()
# 继承顺序按照 C(A, B) 的顺序，先查找 A 类的方法，如果 A 类中没有找到，再去查找 B 类的方法
c.talk()  # 输出: A is talking

