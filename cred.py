from cryptography.fernet import Fernet
from datetime import datetime
import os

key = b'soYkJaGosGZ_JCHkP8A7By6AbGkSf_mWUL-wP3zUkS8='

f = Fernet(key)

email = None
psw = None


def encrypt_data(data1,data2):





    email= f.encrypt(bytes(data1, 'utf-8'))
    password=f.encrypt(bytes(data2,'utf-8'))
    with open("data.txt","wb") as file:

        file.write(email)
        file.write(b'\n')
        file.write(password)

def decrypt_data():
    global email, psw
    with open("data.txt","rb") as file:

        email=file.readlines(1)
        password=file.readlines(2)
    x=f.decrypt(email[0])
    y=f.decrypt(password[0])
    email = x.decode('utf-8')
    psw = y.decode('utf-8')

def re_cred():
    return email, psw

""" encrypt_data()
decrypt_data() """
if not (os.path.isfile("data.txt")):
    print("Before staring to use this bot please complete this process.\nIt is a one time process.")
    x = str(input("Please enter email : "))
    y = str(input("Please enter password : "))
    encrypt_data(x,y)
    decrypt_data()
else:
    decrypt_data()


  