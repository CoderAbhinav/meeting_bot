from cryptography.fernet import Fernet
from datetime import datetime
import os

key = b'soYkJaGosGZ_JCHkP8A7By6AbGkSf_mWUL-wP3zUkS8='

f = Fernet(key)




def encrypt_data(data1,data2):





    email= f.encrypt(bytes(data1, 'utf-8'))
    password=f.encrypt(bytes(data2,'utf-8'))
    with open("data.txt","wb") as file:

        file.write(email)
        file.write(b'\n')
        file.write(password)

def decrypt_data():

    with open("data.txt","rb") as file:

        email=file.readlines(1)
        password=file.readlines(2)
    x=f.decrypt(email[0])
    y=f.decrypt(password[0])
    print(x)
    print(y)

""" encrypt_data()
decrypt_data() """
if not (os.path.isfile("data.txt")):
    x = str(input("Please enter email : "))
    y = str(input("Please enter password : "))
    encrypt_data(x,y)
else:
    decrypt_data()

   