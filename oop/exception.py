# coding: utf-8


"""

try / except / finally

python 2.5 之前 finally 是独立的关键字。
异常就是错误

语法： except 可以有多个，但是捕获到第一个异常后不会再继续往下执行 except 语句块了。
try:
    可能发生异常的代码块,被 try 关键字检查并保护的业务
except 异常类型 as e:
    异常处理代码块
except Exception as e:
    无法确定是哪种异常的情况下使用的捕获方法
finally:
    无论是否发生异常都会执行的代码块，如果在 finally 中返回了值，那么 finally 中的返回值会覆盖掉 try 或 except 中的返回值

⚠️
except (异常类型1, 异常类型2, ...) as e
    捕获多个异常类型的处理方式

日常开发中，异常处理更加推荐使用具体异常捕获的方式，具体实践根据实际情况而定。
"""

# 无法确定是哪种异常的情况下使用的捕获方法 ： except Exception as e
try:
    print(1 / 0)
except Exception as e:
    print("发生异常", e)
finally:
    print("无论是否发生异常都会执行的代码块")


# 具体异常捕获 ： except 异常类型 as e
try:
    print(1 / 0)
except (ZeroDivisionError, NameError) as e:
    print("除数不能为零", e)
finally:
    print("无论是否发生异常都会执行的代码块")


"""
常见异常类型：

  Exception  所有异常的基类
  ZeroDivisionError  除零异常
  TypeError  类型异常
  IndexError  索引异常
  KeyError  键异常
  AttributeError  属性异常
  NameError  名称异常
  SyntaxError  语法异常
  SystemError  系统异常
  ValueError  传入参数异常


"""

def test():
    try:
        print('try')
        return 'try'
    except Exception as e:
        print('except')
        return 'except'
    finally:
        print('finally')
        return 'finally'

test()


"""
自定义异常与抛出异常

自定义异常抛出 raise ，将信息以报错的形式抛出

raise 异常类型(异常信息)



"""

print('---------------自定义异常与抛出异常')
try:
    raise ValueError('raise 自定义异常')
except ValueError as e:
    print(e)


def test2(num):
    if num == 100:
        raise ValueError('num 不能为 100')
    return num

def test3(num):
    try:
        return test2(num)
    except ValueError as e:
        print(e)
        return 0

test3(100)


print('---------------自定义异常类')
class NumberLimitError(Exception):
    def __init__(self, message):
        self.message = message

def test4(num):
    if num == 100:
        raise NumberLimitError('custom NumberLimitError异常 num 不能为 100')
    return num

def test5(num):
    try:
        return test4(num)
    except NumberLimitError as e:
        print(e.message)
        return 0

test5(100)


print('---------------断言')

# assert 1 == 1, '断言失败'
