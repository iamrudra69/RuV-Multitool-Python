import os 
import requests
import socket 
import platform
import time
import pymongo as pym
import getpass
import hashlib

# creating logo

os.system("title RuV Tools")

logo = """\033[38;2;226;255;12m\t▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐      ███████████              █████   █████    ███████████                   ████              ▌
\t▐     ░░███░░░░░███            ░░███   ░░███    ░█░░░███░░░█                  ░░███              ▌
\t▐      ░███    ░███  █████ ████ ░███    ░███    ░   ░███  ░   ██████   ██████  ░███   █████      ▌
\t▐      ░██████████  ░░███ ░███  ░███    ░███        ░███     ███░░███ ███░░███ ░███  ███░░       ▌
\t▐      ░███░░░░░███  ░███ ░███  ░░███   ███         ░███    ░███ ░███░███ ░███ ░███ ░░█████      ▌
\t▐      ░███    ░███  ░███ ░███   ░░░█████░          ░███    ░███ ░███░███ ░███ ░███  ░░░░███     ▌
\t▐      █████   █████ ░░████████    ░░███            █████   ░░██████ ░░██████  █████ ██████      ▌
\t▐     ░░░░░   ░░░░░   ░░░░░░░░      ░░░            ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░       ▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
\033[32;221;246;255;12m                                                                                           
                                                                            credits --> @iamrudra69                                      
                                                                                           """

# Setting up functions

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printLogo():
    print(logo)

def getHost_Ip():
    print(f"Hostname : {socket.gethostname()}")
    print(f"IP Address : {socket.gethostbyname(socket.gethostname())}")

def get_CPU_Architecture():
    print(f"CPU Architecture : {platform.machine()}")

def getUsername():
    print(f"User : {os.environ.get('USERNAME')}")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def loginUser(address):

    attempts = 3

    while attempts > 0:
        cls();
        printLogo() 
        userId = input("Enter your user Id : ").lower()
        passW = getpass.getpass("Enter your password: ")
        
        password = hash_password(passW)

        try: 
            client = pym.MongoClient(address)
            database = client["RuVMultitoolv1"]
            collection = database["Auth"]
            document = collection.find_one({"userId": userId, "password": password})
            if document:
                print("\033[38;5;27mConnecting to the Server !\033[0m")       
                time.sleep(2)
                print("\033[38;5;45mConnection successful!\033[0m")             
                time.sleep(1)
                print("\033[32mLogin successful!\033[0m")
                time.sleep(2)
                break
            else:
                cls()
                print("\033[1;31mInvalid userId or password.\033[0m") 
                attempts -= 1
                print(f"\033[1;33mYou have only {attempts} attempt left!\033[0m") 
                input("")
        
        except:
            print("An error occured!")

    if (attempts == 0):
        exit(0)


# Starting main function

def main():

    cls()
    printLogo()    
    loginUser("mongodb://localhost:27017/")

    while True:
        
        # Setting up interface

        cls()
        printLogo()

        print("""[1] Get Hostname & IP Address
        \n[2] Get CPU Architecture
        \n[3] Get Current User
        \n[4] Exit""")

        # Taking input
        
        choice = input("\nOption : ")

        cls()
        printLogo()

        # Setting up conditions

        match(choice):
        
            case '1':
                getHost_Ip()
                input("\nPress Enter to return to menu...")

            case '2':
                get_CPU_Architecture()
                input("\nPress Enter to return to menu...")

            case '3':
                getUsername()
                input("\nPress Enter to return to menu...")
                
            case '4':
                for i in range(5, 0, -1):
                    cls()
                    printLogo()
                    print("Thank You for using our multitool")
                    if (i == 1):
                        print(f"This program will terminate in {i} second")
                    else:
                        print(f"This program will terminate in {i} seconds")
                    time.sleep(1)
                break

            case _:
                print("Invalid choice. Try again.")
                input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()