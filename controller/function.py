# coding: utf-8

# 函数： 定义、参数、返回结果、全局与局部变量

"""
函数：默认返回值为 None
def <name>(args...):
  do something...
  return


  函数的参数：
  必传参数、默认参数、不确定参数、参数规则
  必传： 必须要传递的参数，不传递时函数调用会抛出异常
  默认： 设置了默认值，不是必传，不传递时使用默认值，传递后使用传递的值。不传不影响函数的调用
  不确定：没有固定的参数名和数量 def add(*args, **kwargs):
    add(1,2,3, name = 'lisi', age = 33)
    args 合并为元组 (1,2,3)
    kwargs 合并结果 字典 {'name': 'lisi', 'age': 33}

  规则：从左至右依次为： 必传、默认、可变元组参数? 、 可变字典参数
  函数类型: 不会对函数的参数进行校验，如果类型出现错误，只会在执行时遇到具体业务时报错，其他情况不会出现异常
    def name(arg1: int, arg2: str):
      print(arg1,arg2)

"""

def test_paramter(a:int, b:int=2, *args:int,**kwargs: str):
  print(a,b,args, kwargs)

test_paramter(1,2,3,'4',True, name = 'lisi')

def test_args(*args, **kwargs):
  print('args', args, len(args))
  print('kwargs',kwargs)

a = ('py', 'django')
b = {'name': 'lisi'}

test_args(*a, **b)

def add(a, b = 1):
  print( a + b)



add( 1, 3)
add(4)
add(a = 1, b = 2)
add(b = 2, a = 2)
add(a = 2)


def add(a:int, b:int = 1, *args):
  print( a , b, args)



""" 不推荐
def add(*args, a, b = 1):
  print( a , b, args)

"""

s = (1,2)
add(1,2)
add(1,2,*s)
# add(1,2,**s) # argument after ** must be a mapping, not tuple

def add(a, b = 1, **kwargs):
  print( a , b, kwargs)

add(1,2, name = 'lisi')
add(a =1,b=2, name = 'lisi')
add(name = 'lisi',age = 20,a =1,b=2,)

def sum( a,  b):
  c = a + b
  return c

print(sum(3, 8))

def capitalize(data: str):
  index = 0
  temp = ''
  for item in data:
    if index == 0:
      temp = item.upper()
    else:
      temp += item
    index += 1
  return temp

print(capitalize(data = 'result'))



# recursion 递归与匿名函数

"""
递归函数： 类型与while 循环，函数内部不停地调用自己
"""
count = 0
def test():
  global count
  count += 1
  if count != 5:
    print('count 条件不满足，重新执行自己，当前count是%s' % count)
    return test()
  else:
    print('count is &=%s' % count)

test()

"""
使用 lambda 定义匿名函数
  f = lambda: value
有参数的匿名函数
  f = lambda x,y: x * y
"""

f = lambda: 1
print(f())

f2 = lambda x,y: x * y
print(f2(1,2))

f3 = lambda x, y =3: print(x > y)
f3(2)

users = [
  {'name': 'lisi'},
  {'name': 'zhangsan'},
  {'name': 'wangwu'},
  {'name': 'zhaoliu'},
]

users.sort(key = lambda x: x['name'])
print(users)