# -*- coding: utf-8 -*-

a_list = [1, 9, 8, 4]
a_dict = {'a': 1, 'b': 2, 'c': 3}
a_set = set(range(10))

print ([elem * 2 for elem in a_list])
print ({value:key for key, value in a_dict.items()})
print ({x ** 2 for x in a_set})
print ({x for x in a_set if x % 2 == 0}) 