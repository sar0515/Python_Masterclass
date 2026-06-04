#sum the costly item in cart.
#using lambda functions.
from functools import reduce
cart=[100,2000,1500,5000]
expensive= list (filter(lambda x:x>1000,cart))
total_cost= reduce(lambda x,y:x+y,expensive)
print(total_cost)

"""
output:
8500
"""