#closer is access the value of outer function
def outer(msg):
    def inner():
        return f"message is:{msg}"
    return inner

say_hi=outer("vanakkam")
print(say_hi())

#output
#message is:vanakkam