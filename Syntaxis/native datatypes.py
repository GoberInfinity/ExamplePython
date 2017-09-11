# -*- coding: utf-8 -*-

import fractions

#Common Numerical Operations
print(11 / 2)
print(11 // 2)

#Fractions
x = fractions.Fraction(1, 3)

#List
#Can expand dynamically as new items are added
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
a_list[-1] 
a_list[-3]
#Slicing A List
#Can get any part of it as a new list. This is called slicing the list
# a[start:end:step] # start through not past end, by step
# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array
 """ +---+---+---+---+---+
     | H | e | l | p | A |
     +---+---+---+---+---+
     0   1   2   3   4   5
    -5  -4  -3  -2  -1 """
a_list[1:3]  
a_list[1:-1]
a_list[3:] 
a_list[:]
#Adding Items To A List See: http://www.diveintopython3.net/native-datatypes.html#extendinglists
# the append() method takes a single argument, which can be any datatype. 
# Here, you’re calling the append() method with a list of three items.
a_list.append(True) 
a_list.append(['g', 'h', 'i'])
# The extend() method takes a single argument, which is always a list, and adds each of the items of that list to a_list.
a_list.extend(['d', 'e', 'f']) 
a_list.insert(0, 'Ω')
#Searching For Values In A List
a_list.count('g')
'new' in a_list
#Removing Items From A List
del a_list[1]
a_list.remove('new')
# removes the last item in the list
a_list.pop()

#Tuples
#A tuple is an immutable list. A tuple can not be changed in any way once it is created
#In practical terms, they have no methods that would allow you to change them.
#Tuples are faster than lists. If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.
a_tuple = ("a", "b", "mpilgrim", "z", "example")

#Sets
# A set is an unordered “bag” of unique values.