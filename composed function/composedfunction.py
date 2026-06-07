#A composed function is when the output of one function becomes the input of another -like
#f(g(x))

def add(x):
    return x + 2

def multi(x):
    return x * 2

def composed(x):
    return add(multi(x))
#we give 2 for x in composed then it become add(multi(2))
#then the multi(2) goes to def mutli(2)
#then it become 4
#then composed become add(4)
#then its goes to def add(4)
#4+2 = 6

print(composed(2))