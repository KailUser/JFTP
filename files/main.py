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
2. Exit""")

selection = int(input("Select: "))

if selection == 1:
    os.system('clear')
    print(core.ftp())
elif selection == 2:
    print("Exiting the program.")
else:
    print("Invalid select. Please try again.")