# coding: utf-8

# 索引： 索引是 列表、字符串、元组 中元素的位置，索引从 0 开始，负数索引表示从列表末尾开始计数，-1 表示最后一个元素，-2 表示倒数第二个元素，以此类推。

# 切片： 切片是从列表中提取一部分元素，切片的语法为 list[start:end:step]，其中 start 表示起始索引，end 表示结束索引，step 表示步长。切片返回一个新的列表，不会修改原列表。
# 切片规则为 左含右不含，即切片的结果包含起始索引对应的元素，但不包含结束索引对应的元素。
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 步长获取切片
print(nums[0:5:2]) # [1, 3, 5]
print(nums[0:5]) # [1, 2, 3, 4, 5]
print(nums[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2]) # [1, 3, 5, 7, 9]
print(nums[0:-1]) # [1, 2, 3, 4, 5, 6, 7, 8]
print(nums[-3:-1]) # [7, 8]
print(nums[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

nums[0:5] = [10, 11, 12, 13, 14]
print(nums) # [10, 11, 12, 13, 14, 6, 7, 8, 9]
print(nums.index(8)) # 7

# reverse 反转列表中的元素
nums.reverse()
print(nums) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# pop 删除列表中指定索引位置的元素，并返回该元素的值，如果没有指定索引，则删除最后一个元素。
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums.pop(0)) # 1
print(nums) # [2, 3, 4, 5, 6, 7, 8, 9]
print(nums.pop()) # 9
print(nums) # [2, 3, 4, 5, 6, 7, 8]
# sort 排序列表中的元素 sort(cmp =None, key=None, reverse=False) 其中 cmp 是一个比较函数，key 是一个函数，reverse 是一个布尔值。 reverse 的值为 True 时，列表元素将被倒序排列（降序）。
# sort 排序时，列表中元素类型必须相同

# clear 清空列表中的所有元素； 无参数，无返回值

# copy 返回列表的浅拷贝； 无参数，返回值为列表的浅拷贝，copy后得到的列表与原列表是两个不同的对象，修改其中一个不会影响另一个。

# extend 将一个可迭代对象中的元素添加到列表的末尾； 参数为一个可迭代对象，无返回值。

manhua = []
history = []
code = []

new_manhua = ('a', 'b', 'c')
new_history = ('d', 'e', 'f')
new_code = ('g', 'h', 'i')

manhua.extend(new_manhua)
history.extend(new_history)
code.extend(new_code)

print(manhua)
print(history)
print(code)

history.extend(manhua)
del manhua
print(history)
history.extend('g')
# 字符串会被切割为单个字符添加到列表中
history.extend('lmn34')
# 字典添加时会将 key 添加到列表中，而不会将 value 添加到列表中
history.extend({"name": '1', "age": 2})
history.extend(['o', 'p', 'q'])
print(history)