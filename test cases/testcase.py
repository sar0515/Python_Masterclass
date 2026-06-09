def divide(a, b):
    try:
        return a /  b
    except ZeroDivisionError:
        return "cannot divide by zero"
    
print(divide(6, 2)) # Output: 3.0
#here we done exception handling and using / for divide ,if incase we give * ,but in test case have 6/3=2.0 ,its become error as failed.
