# coding: utf-8

work = {}
one = (1,)
one_key = 1
work[str(one_key)] = one
print(work)
two = [1,2]
two_key = 2
work[str(two_key)] = two

three = []
three.append(1)
three.append(2)
three.append(3)
three_key = 3
work[str(three_key)] = three

four = []
four.append(1)
four.append(2)
four.append(3)
four.append(4)
four_key = 4
work[str(four_key)] = four

five = [1,2,3,4,5]
five_key = 5
work[str(five_key)] = five

six = [1,2,3,4,5,6]
six_key = 6
work[str(six_key)] = six

s = (1,2,3,4,5,6,7)
seven = []
seven.extend(s)
seven_key = 7
work[str(seven_key)] = seven

s = {1,2,3,4,5,6,7,8}
eight = []
eight.extend(s)
eight_key = 8
work[str(eight_key)] = eight

s = {1,2,3,4,5,6,7,8,9}
nine = []
nine.extend(s)
nine_key = 9
work.update({nine_key: nine})

# print(work)

keys = list(work.keys())


one_key = keys[0]
one_value = work.pop(one_key)
print('{} * {} = {}'.format(int(one_key), one_value[0], int(one_key) * one_value[0]))

tw_key = keys[1]
tw_value = work.pop(tw_key)
print('{} * {} = {}'.format(int(tw_key), tw_value[0], int(tw_key) * tw_value[0]), end = '  ')
print('{} * {} = {}'.format(int(tw_key), tw_value[1], int(tw_key) * tw_value[1]))

tw_key = keys[2]
tw_value = work.pop(tw_key)
print('{} * {} = {}'.format(int(tw_key), tw_value[0], int(tw_key) * tw_value[0]), end = '  ')
print('{} * {} = {}'.format(int(tw_key), tw_value[1], int(tw_key) * tw_value[1]), end = '  ')
print('{} * {} = {}'.format(int(tw_key), tw_value[2], int(tw_key) * tw_value[2]))



