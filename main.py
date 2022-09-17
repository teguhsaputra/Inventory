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
import pandas as pd
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
    mypath = pathlib.Path().resolve()
    #print(mypath/'aaa')
    with open(pathlib.Path().resolve()/'menu.json','r') as f:
        data = json.load(f)
    clear_screen()
    
    # CreateUser = createUser(100)
    # val = CreateUser.getVal()
    # print(val)
    
    print("=======================")
    print("          Menu         ")
    print("=======================")
    
    s = '{"col1":{"row2":2,"row3":3},"col2":{"row2":"y","row3":"z"}}'
    df = pd.read_json(s)
    print(df)
    # for m in data['menu']:
    #     df = pd.read_json(m)
    #     print(df)
    menu = int(input("Masukan kode menu akses : "))
    f.close()


clear_screen()
login()