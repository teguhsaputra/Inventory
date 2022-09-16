# def looping(i):
#     for i in range(0,i):
#         for j in range(0,10 - i):
#             print(" ", end="")
#         for k in range(0,i):
#             print("* ", end="")
#         print("\r")

# n = 10
# looping(n)

import os
import json
import pathlib
from time import sleep
from user import createUser

def clear_screen():
    _ = os.system('cls')

def login():
    mypath = pathlib.Path().resolve()
    #print(mypath/'aaa')
    with open(pathlib.Path().resolve()/'auth.json','r') as f:
        data = json.load(f)
    print("=======================")
    print("System Inventory Barang")
    print("=======================")
    username = input("Massukan Username : ")
    password = input("Password : ")
    if username == "" or password == "": 
        print("Username / Password Tidak Boleh Kosong")
        sleep(1)
        clear_screen()  
        login()
    else:
        for i in data['auth']:
            if(username == i['username'] and password == i['password']):
                clear_screen()
                print("Anda Berhasil Login")
                sleep(1)
                home()
            else:
                clear_screen()
                print("Username/Password Anda Salah")
                sleep(1)
                clear_screen()
                login()
    f.close()

def home():
    clear_screen()
    CreateUser = createUser(100)
    val = CreateUser.getVal()
    print(val)
    print("selamat datang")

clear_screen()
login()