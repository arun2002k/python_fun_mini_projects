import random
import string

password_len = int(input("Write the lenght of the password : "))
new_password = ""


for i in range(password_len):
    new_password += random.choice(string.printable)

print("Your new password : ", new_password) 
