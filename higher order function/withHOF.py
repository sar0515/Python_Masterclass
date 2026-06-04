#now we see with HOF

def gamil_email(username, domain="gmail.com"):
    return f"{username}@{domain}"
#here we create a seprate function for each procider .

def ymail_email(username,domain ="ymail.com"):
    return f"{username}@{domain}"

#main opreation>
def build_email(username, email_func):
    return email_func(username)
#here we create a new function build_email ,that have email_func as a parameter and we pass the function as an argument to the build_email function.
#if i call with username and with gmail_email function as an argument then it will return the email with gmail domain and if i call with ymail_email function as an argument then it will return the email with ymail domain.
#then we call build_email function with username and gmail_email function ,then it think so email_func is equal to gmail_email function and it will return the email with gmail domain and if i call with ymail_email function as an argument then it will return the email with ymail domain.
print(build_email("john", gamil_email))
print(build_email("alice", ymail_email))