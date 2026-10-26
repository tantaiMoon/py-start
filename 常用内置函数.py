"""
函数名        参数            简介                          返回值
abs          Number         绝对值函数                    返回参数的绝对值
all          List         判断列表中所有元素是否为True      返回True或False
help         Object       查看对象的帮助信息               无
enumerate    Iterable     迭代时记录索引                  返回一个enumerate对象
input        Str          命令行输入                          用户输入的字符串
isinstance  Object, Class  判断对象是否是某个类的实例        返回True或False
type        object         查看对象的类型                   返回对象的类型
vars        object         查看对象的属性                   返回对象的属性字典
dir         Object         查看对象的属性和方法             返回对象的属性和方法列表
hasattr    Iterable, Str   判断对象是否有某个属性           返回True或False
setattr    Obj, Str, Value  设置对象的属性值                无
getattr    Obj, Str, Default  获取对象的属性值                返回对象的属性值
any        Iterable         判断列表中是否有元素为True          返回True或False

"""

import random
"""
random 函数
  random.random()                        # 返回0.0到1.0之间的随机小数
  random.randint(a, b)                   # 返回a到b之间的随机整数，包括a和b
  random.choice(seq)                     # 从序列seq中随机选择一个元素
  random.sample(seq, k)                  # 从序列seq中随机选择k个元素
  random.uniform(a, b)                   # 返回a到b之间的随机小数，包括a和b
  random.randrange(start, stop[, step])  # 返回指定范围内的随机整数，步长为step
  random.shuffle(seq)                     # 将序列seq中的元素随机打乱顺序
  random.seed(a=None)                    # 设置随机数生成器的种子，保证每次生成的随机数序列相同
  random.getrandbits(k)                  # 返回一个k位的随机整数
  random.getstate()                      # 返回当前随机数生成器的状态
  random.setstate(state)                 # 设置随机数生成器的状态
"""

abs(-5)  # 返回5
all([1, 2, 3])  # 返回True
all([1, 0, 3])  # 返回False
all(['2', 1, 3])  # 返回 True

# help(abs)  # 查看abs函数的帮助信息
# help([])  # 查看列表的帮助信息

enum_res = enumerate(['a', 'b', 'c'])  # 返回一个enumerate对象
print(list(enum_res)) # [(0, 'a'), (1, 'b'), (2, 'c')]

# str1 = input('请输入：')  # 命令行输入
# print(str1)  # 输出用户输入的字符串


print(random.sample([1, 2, 3, 4, 5], 3))  # 从列表中随机选择3个元素
print(random.sample('abcde', 3))  # 从字符串中随机选择3个元素
print(random.uniform(1, 10))  # 返回1到10之间的随机小数
print(random.randrange(1, 10, 2))  # 返回1到10之间的随机整数，步长为2
print(random.shuffle([1, 2, 3, 4, 5]))  # 将列表中的元素随机打乱顺序
