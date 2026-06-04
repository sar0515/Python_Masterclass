#filter is used to filter the elements.
#syntax: filter(function, iterable)

numbers=[1,2,3,4,5,6,7,8,9,10]
#using filter function to filter the even numbers from the list.
even = list(filter(lambda x:x%2==0,numbers))
print(even)

"""
output:
[2, 4, 6, 8, 10]
"""