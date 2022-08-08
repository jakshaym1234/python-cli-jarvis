import requests
import os 
import time

def dogapi_option1(): 
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    print(response.text)
    input("Enter to continue....")
    return

def dogapi_option2(): 
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    print(response.text)
    input("Enter to continue....")
    return

def dogapi():
    while True:
        os.system("clear")
        print("Welcome to DOG API menu")
        print("""Select from below : 
        1. Option1
        2. Option2
        0. EXIT""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            dogapi_option1()
        if choice == '2' : 
            dogapi_option2()
        if choice == '0':
            exit()    
        os.system("clear")