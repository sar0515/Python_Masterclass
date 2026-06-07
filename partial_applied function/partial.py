#the partial applied function is partially implement the argument for a function
#we need import the function (from functools import partial)

 
from functools import partial
 #step 1: define the original function

def calculate_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)

#step 2: create a partially applied function with gst fixed
price_with_gst = partial(calculate_price, tax_rate=0.18)
#we fixed the tax rate
print(price_with_gst(1000)) # 1180.0
print(price_with_gst(500)) # 590.0


#another example
def create_email(username, domain):
    return f"{username}@{domain}"

gmail=partial(create_email, domain="gmail.com")
ymail = partial(create_email, domain="ymail.com")

print(gmail("sar"))
print(ymail("www"))


"""
op

1180.0
590.0
sar@gmail.com
www@ymail.com
"""