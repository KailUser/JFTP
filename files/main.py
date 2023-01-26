import colorama
from colorama import *
import core as core


colorama.init(autoreset=True)

print("1. Connect to SSH")
print("2. Connect to FTP")

selection = int(input("Select: "))

if selection == 1:
    print(core.connect_ssh())
elif selection == 2:
    print(core.ftp())
else:
    print("Invalid select. Please try again.")