# -*- coding: utf-8 -*-
"""
Note: This is a debugg version, to see what happened with the recursion
call 
"""


def perm(lis):
    print(lis)
    if len(lis) == 0:
        return []
    elif len(lis) == 1:
        return [lis]
    else:
        l = []
        for i in range(len(lis)):
            x = lis[i]
            xs = lis[:i] + lis[i + 1 :]
            print(f"i: {i}, x: {x} , xs{xs}")
            print(lis[:i])
            print("-" * 50)
            for p in perm(xs):
                l.append([x] + p)
                print(f"***called l.append[{x}]+{p} = {l}")
        return l


print(perm(list("abc")))

"""
Uncomment if you would like to see the logic behind x and xs 
lis = [1,2,3,4,5,6,7,8]
def debug(lis):
    for i in range(len(lis)):
        x = lis[i]
        xs = lis[:i] + lis[i + 1:]
        print(x)
        print(f"lis[:i] = lis[:{i}] = " + str(lis[:i]))
        print(f"lis[i + 1:] = lis[{i} + 1:] = " + str(lis[i + 1:]))
        print("--"*19)     
print(debug(lis))
"""
