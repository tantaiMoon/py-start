# coding: utf-8

# 类的继承
# 子类拥有父类的所有属性和方法
# 父类不一定拥有子类所有的属性与方法
"""
继承语法 :
  class Chhild(Parent):     表示 Child 类继承了 Parent 类
  class Parent(object):     表示 Parent 类继承了 基类 object
 """

class Parent(object):
  def __init__(self, name, sex):
    self.name = name
    self.sex = sex

  def talk(self):
    return f'{self.name} are walking'

  def is_sex(self):
    if self.sex == 'm':
      return f'{self.name} is a boy'
    else:
      return f'{self.name} is a gril'


class ChildOne(Parent):
  def play_football(self):
    return f'{self.name} are playing football'

class ChildTwo(Parent):
  def play_pingpong(self):
    return f'{self.name} are playing pingpong'

c1 = ChildOne(name = 'Tom', sex =' m')

result = c1.play_football()
print(result)

c2 = ChildTwo(name = 'Jeery', sex = 'm')
result2 = c2.play_pingpong()
print(result2)
print(c2.talk())

p = Parent(name = 'J', sex = 'm')
result3 = p.talk()
print(result3)
# print(p.play_football()) # 'Parent' object has no attribute 'play_football'


# 类的多态： 多态是指同一个方法调用作用于不同的对象上，可以产生不同的解释和不同的执行结果


# 子类中重写父类的方法，子类对象调用方法时，优先调用子类中重写的方法

class P1(object):
  def talk(self):
    print('P1 is talking')
    return 'P1 is talking'

# 子类继承父类 P1
class C1(P1):
  def talk(self):
    print('C1 is talking')
    return 'C1 is talking'

class C2(P1):
  # 子类中重写父类的方法
  def talk(self):
    print('C2 is talking')
    return 'C2 is talking'
  def play(self):
    print('C2 is playing')
    return 'C2 is playing'

c2 = C2()
c2.play()  # 调用子类 C2 中新增的方法
c2.talk()  # 调用子类 C2 中重写的方法


f = P1()
f.talk()  # 调用父类 P1 中的方法

