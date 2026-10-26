# coding: utf-8

# 集合（set）是一个无序的不重复元素的序列。支持所有不可变数据类型。
# 使用 set() 函数或者 {1,2,3} 有值的{} 来创建集合。不能使用  {}  来创建，会被认为是字典类型

# 列表有序、集合无序
# 列表元素可重复、集合元素不能重复
# 列表用于数据的使用、集合用于数据的交并差集获取
# 列表数据元素有索引、集合数据元素无索引
# 列表使用 [] 、集合使用 {}

new_set = set()

print(new_set)
print(type(new_set))

b = set(['py', 'js', 'flask'])
print(b)

# c = {[1,2,3]} # TypeError: unhashable type: 'list'

# 不可变数据类型
c = {(1,2,3), '4', 5,  True}
print(c)

# 集合
# add 方法：向集合中添加元素，如果元素已存在，则不进行任何操作

# update 方法：向集合中添加多个元素，如果元素已存在，则不进行任何操作
# update() 方法可以接受一个可迭代对象（如列表、元组、字典、字符串等）作为参数，将其中的元素添加到集合中

# remove 方法：从集合中删除指定元素，如果元素不存在，则抛出 KeyError 异常

# discard 方法：从集合中删除指定元素，如果元素不存在，则不进行任何操作

# pop 方法：随机删除集合中的一个元素，并返回该元素，如果集合为空，则抛出 KeyError 异常

# clear 方法：清空集合中的所有元素

# 示例代码
s = {1, 2, 3}
s.add(4)
print(s)  # 输出: {1, 2, 3, 4}

s.update([5, 6, (7, 8), 'py'])
s.update('flask')
print(s)  # 输出: {1, 2, 3, 4, 5, 6, (7, 8), 'py', 'f', 'l', 'a', 's', 'k'}

s.remove(2)
print(s)  # 输出: {1, 3, 4, 5, 6}

s.discard(10)  # 不会抛出异常
print(s)  # 输出: {1, 3, 4, 5, 6}

popped_element = s.pop()
print(popped_element)  # 输出: 随机删除的元素
print(s)  # 输出: 剩余的集合元素

s.clear()
print(s)  # 输出: set()


# difference 方法：返回两个集合的差集，即属于第一个集合但不属于第二个集合的元素组成的集合
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
diff = s1.difference(s2)
print(diff)  # 输出: {1, 2}

# intersection 方法：返回两个及以上集合的交集，即同时属于两个集合的元素组成的集合
inter = s1.intersection(s2, {4, 5})
print(inter)  # 输出: {4}

# union 方法：返回两个及以上集合的并集，即属于任一集合的元素组成的集合
# 参数可以是一个或多个集合，也可以是一个可迭代对象（如列表、元组、字典、字符串等），将其中的元素添加到集合中
uni = s1.union(s2, {7, 8})
print(uni)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# symmetric_difference 方法：返回两个集合的对称差集，即属于任一集合但不同时属于两个集合的元素组成的集合
sym_diff = s1.symmetric_difference(s2)
print(sym_diff)  # 输出: {1, 2, 5, 6}
print(list(sym_diff))  # 输出: [1, 2, 5, 6]，将集合转换为列表

print('------------- isdisjoint 方法 -------------')
# isdisjoint 方法：判断两个集合是否包含共同的元素，如果没有交集则返回 True，否则返回 False
s3 = {1, 2}
s4 = {3, 4}
print(s3.isdisjoint(s4))  # 输出: True
s5 = {2, 3}
print(s3.isdisjoint(s5))  # 输出: False