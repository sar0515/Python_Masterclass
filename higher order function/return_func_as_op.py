#now we see how to return a function as an output .
def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email
#here see that email_builder return a fucntion called build_email,and build_email is take domain from email_builder and username from email_builder.

gmail=email_builder("gmail.com")
ymail=email_builder("ymail.com")
hotmail=email_builder("hotmail.com")

#here we assign the email_builder function to three different variables and pass different domain as an argument to the email_builder function and it will return the build_email function with the domain that we passed as an argument.
print(gmail("sar"))
print(ymail("alice"))
print(hotmail("bob"))

"""
output:
sar@gmail.com
alice@ymail.com
bob@hotmail.com
"""
