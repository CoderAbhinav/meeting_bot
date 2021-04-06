from cryptography.fernet import Fernet
from datetime import datetime
import os

key= Fernet.generate_key()

with open('mykey.key','wb') as mykey:
    mykey.write(key)
with open('mykey.key','rb') as mykey:
    key= mykey.read()
print(key)

f=Fernet(key)
with open('email and password.csv','rb') as orignal_file:
    original=orignal_file.read()

encrypted = f.encrypt(original)

with open ('enc_email and password.csv','wb') as encrypted_file:
    encrypted_file.write(encrypted)
