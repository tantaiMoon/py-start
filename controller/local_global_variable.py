# coding: utf-8

"""
全局变量
  Python 脚本最上层的代码块定义的变量。可以在函数内部读取全局变量并使用，但是不能修改

局部遍历
  在函数体内定义的变量，函数外不能使用，外部访问报错
 """

global_var = 'global var'

def test():
  print(global_var)

test()

def test1():
  global_var = '函数内修改全局变量'
  print('这里是局部变量：',global_var)

test1()

print('global var: ', global_var)

def test2():
  age = 33
  print(age)

test2()

# print(age) # 未定义“age”P

def test3(a):
  a = a + '函数内修改全局变量'

test3(global_var)

print(global_var)

"""
global 关键字可以在函数体内修改全局变量。global 修饰的全局变量只支持 数字、布尔、空、字符串
  global var
  var = ''        函数体内给全局变量重新赋值
 """
def test4():
  global global_var
  global_var = 'global 关键字修改全局变量了'

test4()
print(global_var)


test_dict = {'a': 1}

def test5():
  test_dict['b'] = 2
  test_dict['c'] = 3

test5()
print(test_dict)

def test6():
  test_dict['b'] = 9
  test_dict.pop('a')

test6()
print(test_dict)