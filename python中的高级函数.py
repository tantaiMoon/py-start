# coding: utf-8

"""
三个魔法函数：
  filter(func, list)      对循环器中的每个元素进行过滤，返回True的元素会被保留，返回False的元素会被丢弃。
  map(func, list)         对循环器中的每个元素进行映射，返回映射后的元素。
  reduce(func, list)      对循环器中的元素进行累积计算，返回最终结果。
"""

list1 = [1, 2, 3, 4, 5]
# filter函数
def is_even(n):
    return n % 2 == 0

filtered_list = list(filter(is_even, list1))

print(filtered_list)  # [2, 4]

# map函数
def square(n):
    return n ** 2

squared_list = list(map(square, list1))
print(squared_list)  # [1, 4, 9, 16, 25]

# reduce函数
from functools import reduce
def multiply(x, y):
    return x * y

reduced_result = reduce(multiply, list1)
print(reduced_result)  # 120