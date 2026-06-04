"""
higher order function (HOF) is a function that takes another function as an argument or returns a function as a result. HOFs are a powerful tool in functional programming and can be used to create more flexible and reusable code.
1.takes another function as an agrumenst.
def apply_function(func, value):
    return func(value)


2.returns a function as its output.

used to make code more flexible and reusable, anddynamic.



"""

#frst we will see normal function without HOF

def build_email(username, provider):
    if provider == "gmail":
        return f"{username}@gmail.com"
    elif provider == "ymail":
        return f"{username}@ymail.com"
    else:
        return f"{username}@{provider}.com"
#now call the functions with inputs
print(build_email("john", "gmail"))
print(build_email("alice", "ymail"))
print(build_email("bob", "outlook"))


#if we need to add the more provider in the code ,we need to rewrite the code ,that why we use HOF.

