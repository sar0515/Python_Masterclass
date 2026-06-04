from password_utils import encrypt_password
from cryptography.fernet import fernet

# generate key and save to file 
def generate_key():
    key = fernet.generate_key()
    with open("secret.key","wb" )as f:
        f.write(key)
    print("key save to secret.key")

if __name__ == "__main__":
    #uncomment this only the first time
    #generate_key()
    #replace with your real MYSQL root password 
    encrypted= encrypt_password("root")
    print("encrypted password(copy this to password_utils.py):")
    print(encrypted)