# coding: utf-8

# 第三方包的导入

# ipythoon 是一个 python 的交互式 shell ，比默认的 python shell 更加好用，支持自动补全、语法高亮、魔法命令等功能。

# datetime 是 python 内置的一个模块，提供了处理日期和时间的类和方法。
"""
获取当前时间
获取当前日期
 """

from datetime import datetime as dt # 导入一个模块
print(dt.now()) # 2024-06-12 15:30:45.123456
from datetime import timedelta # 导入一个模块
print(timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, weeks=0, minutes=0, hours=0)) # 1 day, 0:00:00


import datetime # 导入包

print(datetime.datetime.now()) # 1 day, 0:00:00


""" 时间对象的加减法运算 """
now = dt.now() # 获取当前时间
print(now) # 2026-09-04 16:52:51.579408
three_day = timedelta(days=3) # 获取三天的时间差
print(three_day) # 3 days, 0:00:00
after_three_day = now + three_day # 获取三天后的时间
print(after_three_day) # 2026-09-07 16:52:51.579408

one_hour = timedelta(hours=1) # 获取一小时的时间差
print(one_hour) # 1:00:00
before_one_hour = now - one_hour # 获取一小时前的时间
print(before_one_hour) # 2026-09-04 15:52:51



""" 时间对象转字符串

strftime() 方法将时间对象转为字符串，格式化输出时间。
%Y-%m-%d %H:%M:%S
%Y: 年份，四位数表示，如 2026
%m: 月份，01-12
%d: 日，01-31
%H: 小时，00-23
%M: 分钟，00-59
%S: 秒，00-59

 """

now = dt.now() # 获取当前时间
print(now) # 2026-09-04 16:52:51.579

str_now = now.strftime("%Y-%m-%d %H:%M:%S") # 将时间对象转为字符串
print(str_now) # 2026-09-04 16:52:51

str_now = now.strftime("%Y-%m-%d") # 将时间对象转为字符串
print(str_now) # 2026-09-04


after_three_day_str = after_three_day.strftime("%Y/%m/%d %H:%M:%S") # 将时间对象转为字符串
print(after_three_day_str, type(after_three_day_str)) # 2026/09/07 16:58:22 <class 'str'>


""" 字符串转时间对象
strptime() 方法将字符串转为时间对象，格式化输出时间。
传入的字符串格式必须和时间对象的格式一致，否则会报错。
 """
now_obj = dt.strptime(after_three_day_str, "%Y/%m/%d %H:%M:%S") # 将字符串转为时间对象
print(now_obj, type(now_obj)) # 2026-09-07 16:58:22 <class 'datetime.datetime'>