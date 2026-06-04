#reduce in lambda is a function that is used to apply a function of two arguments cumulatively to the items of a sequence from left to right, reducing the sequence to a single value.
#syntax: reduce(function, iterable)

from functools import reduce
#we need to import reduce from functools module to use it.


num=[1,2,3,4,5]
"""
how this work 
1+2=3
3+3=6
6+4=10
"""
total = reduce(lambda x,y:x+y,num)
print(total)

"""

output:
15
"""

#next we find the max number.
max_num = reduce(lambda x,y:x if x>y else y,num)
"""
now 
x=1,y=2 => 2
x=2,y=3 => 3
x=3,y=4 => 4
x=4,y=5 => 5

"""
print(max_num)

"""

output:
5
"""