import ftplib
import os 
import colorama
from colorama import *
import sys
import paramiko

def ftp():
    os.system('cls')
    server = input("Enter the FTP server: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    os.system('cls')
    print(Fore.RED + "Server: ", server)
    print(Fore.RED + "Username: ", username)
    print(Fore.RED + "Password: ", password)

    confirm = input("Is the above information correct? (y/n)")
    if confirm.lower() == 'y':
        while True:
            os.system('cls')
            ftp = ftplib.FTP()
            ftp.connect(server, 21)
            ftp.login(user=username, passwd=password)
            ftp.cwd('/')
            print(Fore.GREEN + "1. List files")
            print(Fore.GREEN + "2. Upload a file")
            print(Fore.GREEN + "3. Download a file")
            print(Fore.GREEN + "4. Read file")
            print(Fore.GREEN + "5. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                os.system('cls')
                ftp.retrlines('LIST')
            elif choice == '2':
                filename = input("Enter the file name: ")
                with open(filename, 'rb') as f:
                    ftp.storbinary('STOR '+ filename, f)
            elif choice == '3':
                filename = input("Enter the file name: ")
                with open(filename, 'wb') as f:
                    ftp.retrbinary('RETR '+ filename, f.write)
            elif choice == '4':
                os.system('cls')
                os.getcwd()
                filename = input("File name: ")
                with open(filename, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        print(line)
            elif choice == '5':
                ftp.quit()
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Exiting the program.")
def connect_ssh():
    os.system('cls')
    hostname = input("Server: ")
    username = input("Login: ")
    password = input("Password: ")
    os.system('cls')
    print(Fore.RED + "Server: ", hostname)
    print(Fore.RED + "Username: ", username)
    print(Fore.RED + "Password: ", password)

    confirm = input("Is the above information correct? (y/n)")
    if confirm.lower() == 'y':
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        return ssh
