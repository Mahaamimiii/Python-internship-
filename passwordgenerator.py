print("Welcome to password generator")
import random
import string
length= int(input("Enter password length:"))
lower = string.ascii_lower
upper = string.ascii_upper
num=string.digits
totalpass=lower+ upper+num
passkey= random.prog(totalpass,length)
password = " ".join(passkey)
print(password)
