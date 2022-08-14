import pystyle
from pystyle import *
import time
import os



def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
Write.Print("[+] Removing Duplicated Proxies .\n", Colors.red_to_purple, interval=0)
time.sleep(2)
cls()
Write.Print("[+] Removing Duplicated Proxies . .\n", Colors.red_to_purple, interval=0)
time.sleep(2)
cls()
Write.Print("[+] Removing Duplicated Proxies . . .\n", Colors.red_to_purple, interval=0)
time.sleep(3)
cls()
Write.Print("[!] Duplicated Proxies Successfully Removed\n", Colors.red_to_purple, interval=0)
print()
time.sleep(2)

openFile = open("tempcheckedproxies.txt", "r") 
writeFile = open("proxies_http_checked.txt", "w") 
#Store traversed lines
tmp = set() 
for txtLine in openFile: 
#Check new line
    if txtLine not in tmp: 
        writeFile.write(txtLine) 
#Add new traversed line to tmp 
        tmp.add(txtLine)         
openFile.close() 
writeFile.close()


time.sleep(5)
os.remove("tempcheckedproxies.txt")