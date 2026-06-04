# map function is a built-in function ,that apply for each value in the list.
# syntax: map(function,iterable)

fruits=['apple','banana','cherry']
#using map function to convert the fruits name in uppercase
result=map(lambda fruit:fruit.upper(),fruits)
#after lambda we give agument as fruit .
print(list(result))
#we can give print(result) but it will give us the map object and we need to convert it to list to see the output.

"""
output:
['APPLE', 'BANANA', 'CHERRY']
"""