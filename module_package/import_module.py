# coding: utf-8

"""
包的导入

将 python 中的某个包（或模块）导入到当前的 py 文件中

用法：
  import 包名.模块名
只会拿到对应包下 __init__ 中的功能或当前模块下的功能

from 包名 import 模块名
只会拿到对应包下 __init__ 中的功能或当前模块下的功能


 """

# 模块
import animal

from animal import main

# 包
from animal.cat import action
from animal.dog import action as dog_action

# 函数
from animal.cat.action import run as cat_run
from animal.dog.action import run as dog_run

# 导入 __init__.py 中的功能
from animal import cat_action1
from animal import dog_action1

# print(animal.cat.action.roar()) # AttributeError: module 'animal.cat' has no attribute 'action'

print(animal.animal_test()) # animal test
print(action.roar()) # cat roars

print(dog_action.roar()) # dog roars

print(cat_run()) # cat runs
print(dog_run()) # dog runs

print(main.animal()) # animal main test

print(cat_action1.roar()) # cat roars
print(dog_action1.roar()) # dog roars

tom = animal.cat.action.Cat('tom')
print(tom.roar()) # tom roars