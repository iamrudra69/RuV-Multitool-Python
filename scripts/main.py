import os 
import requests
import socket 
import platform
import time

# creating logo

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

def setTerminalSize(cols=100, lines=30):
    if platform.system() == "Windows":
        os.system(f'mode con: cols={cols} lines={lines}')
    else:
        os.system(f'printf "\\e[8;{lines};{cols}t"')


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

# Starting main function

def main():

    while True:
        
        # Setting up interface
        
        setTerminalSize()
        os.system("title RuV Tools")
        cls()
        printLogo()

        print("""[1] Get Hostname & IP Address
        \n[2] Get CPU Architecture
        \n[3] Get Current User
        \n[4] Exit""")

        # Taking input
        
        choice = input("\n\nOption : ")

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
                print("Thank You for using our multitool")
                print("This program will terminate in 5 seconds")
                time.sleep(5)
                break

            case _:
                print("Invalid choice. Try again.")
                input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()