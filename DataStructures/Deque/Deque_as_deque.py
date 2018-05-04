# -*- coding: utf-8 -*-
"""
Double-ended queue, is an ordered collection of items similar to the queue. 
It has two ends, a front and a rear, and the items remain positioned in the 
collection. 
"""
from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')
d.appendleft('f')
len(d)
d.popleft()  

