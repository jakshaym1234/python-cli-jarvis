import requests
import os 
import time

def catapi_option1(): 
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    print(response.text)
    input("Enter to continue....")
    return

def catapi_option2(): 
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    print(response.text)
    input("Enter to continue....")
    return

def catapi():
    while True:
        os.system("clear")
        print("Welcome to CAT API menu")
        print("""Select from below : 
        1. Option1
        2. Option2
        0. EXIT""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            catapi_option1()
        if choice == '2' : 
            catapi_option2()
        if choice == '0':
            exit()    
        os.system("clear")