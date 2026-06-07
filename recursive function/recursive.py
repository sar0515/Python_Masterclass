# A recursive function is a function that calls itself(like repeated)
#in order to solve a smaller version of the same problem.

#factorial 5!
#5*4*3*2*1


def factorial(n): #frist that 5 is in n 
    if n == 1: #check the 5 is not equal to 1 
        return n
    return n * factorial(n - 1) #5 *factorial(5 -1 )  5*4
#then repeate the process for 4 ,3,2,1
print(factorial(5))

"""
factorial(5)
5* factorial(4)
5*4* factorial(3)
5*4*3* factorial (2)
5*4*3*2*1=120
"""

#another exmaple

def countdown(x):
    if x == 0:
        print("boom!")
        return
    print(x)
    countdown(x-1)
print(countdown(5))

"""
output
5
4
3
2
1
boom!
None

"""
