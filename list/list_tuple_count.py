# coding: utf-8

# count 返回列表中指定元素的个数.只检查完整的元素是否存在需要计算，即 lisi 可检索 但是 li 不能检索

name_list = ['lisi', 'lisi', 'wangwu', 'zhaoliu']

tuple_t = (1, 2, 3)

print(name_list.count('lisi'))
print(tuple_t.count(2))

print(f'lisi 在列表中出现的次数为: {name_list.count("lisi")}')
print('wangwu 在列表中出现的次数为: %d' % (name_list.count('wangwu')))

dicts = [
  {'name': 'dong', 'age': 18},
  {'name': 'f', 'age': 18},
  {'name': 'g', 'age': 18}
]

print('dong 在 dicts 中出现的次数为: %d' % (dicts.count({'name': 'dong', 'age': 18})))

tuple_t = (1, 2, 3, 4, 5, 6, 7, 8, 9,3)

print('3 在 tuple_t 中出现的次数为: %d' % (tuple_t.count(3)))
print('2 在 tuple_t 中出现的次数为: %s' % (tuple_t.count(2)))
print('10 在 tuple_t 中出现的次数为: {}'.format(tuple_t.count(10)))
print(f'1 在 tuple_t 中出现的次数为: {tuple_t.count(1)}')
print('6出现 %s 次，\n7出现 %s 次,\n 3出现 %s 次' % (tuple_t.count(6), tuple_t.count(7), tuple_t.count(3)))