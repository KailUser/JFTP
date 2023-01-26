import colorama
from colorama import *
import core as core
import os


colorama.init(autoreset=True)
print(Fore.LIGHTGREEN_EX + """
░░░░░██╗███████╗████████╗██████╗░
░░░░░██║██╔════╝╚══██╔══╝██╔══██╗
░░░░░██║█████╗░░░░░██║░░░██████╔╝
██╗░░██║██╔══╝░░░░░██║░░░██╔═══╝░
╚█████╔╝██║░░░░░░░░██║░░░██║░░░░░
░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░

1. Connect to FTP Server
2. Local Ftp Server
3. Exit""")

selection = int(input("Select: "))

if selection == 1:
    os.system('cls')
    print(core.ftp())
elif selection == 2:
    os.system('cls')
    os.system(f'python -b %cd%//files//ftp_server_local.py')
elif selection == 3:
    print("Exiting the program.")
else:
    print("Invalid select. Please try again.")