
import os
import time
import requests
import pystyle
import random
import sys
from pystyle import *


os.system('cls' if os.name=='nt' else 'clear')
os.system('mode con: cols=120 lines=50')



banner = '''
 ██████╗██████╗  █████╗ ███████╗██╗   ██╗███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██████╔╝███████║  ███╔╝  ╚████╔╝ ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║     ██╔══██╗██╔══██║ ███╔╝    ╚██╔╝  ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║███████╗   ██║   ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                                                     
                        ╔══════════════════════════════════════════════╗
                        ║              CrazyScraper 1.0.0              ║
                        ║           Coded by CrazyManV2#0001           ║
                        ║               PROTOCOLS: HTTP/S              ║
                        ║             Currently 27 sources             ║ 
                        ╚══════════════════════════════════════════════╝                                           
'''
print(Colorate.Horizontal(Colors.purple_to_red, Center.XCenter(banner)))

os.system(f'title CrazyScraper')
print()
Write.Print("[+] This program will autoscrape proxies into separate files", Colors.red_to_yellow, interval=0.01)
print()
Write.Print("\n[+] Scraping Proxies Please Wait . . . \n", Colors.red_to_purple, interval=0)

http = open('proxies_http_scraped.txt','wb')

# HTTP Proxies Sources
h = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt")
h1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt")
h2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
h3 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt")
h4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt")
h5 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
h6 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt")
h7 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
h8 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
h9 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
h10 = requests.get("https://www.proxyscan.io/download?type=http")
h11 = requests.get("https://www.proxyscan.io/download?type=https")
h12 = requests.get("https://api.openproxylist.xyz/http.txt")
h13 = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt")
h14 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
h15 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
h16 = requests.get("https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt")
h17 = requests.get("https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt")

h18 = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt")
h19 = requests.get("https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt")
h20 = requests.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt")
h21 = requests.get("https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt")
h22 = requests.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt")
h23 = requests.get("https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt")
h24 = requests.get("https://raw.githubusercontent.com/almroot/proxylist/master/list.txt")
h25 = requests.get("https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt")
h26 = requests.get("https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt")
h27 = requests.get("https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt")


Write.Print(f"[!] Finished Scraping Proxies!\n", Colors.white_to_red, interval=0)
time.sleep(1)
Write.Print("[+] Writing Proxies In Files . . .\n", Colors.red_to_purple, interval=0)
time.sleep(1)

# Writing Proxies In Their Respective Files
# Writing HTTP Proxies
http.write(h.content)
http.write(h1.content)
http.write(h2.content)
http.write(h3.content)
http.write(h4.content)
http.write(h5.content)
http.write(h6.content)
http.write(h7.content)
http.write(h8.content)
http.write(h9.content)
http.write(h10.content)
http.write(h11.content)
http.write(h12.content)
http.write(h13.content)
http.write(h14.content)
http.write(h15.content)
http.write(h16.content)
http.write(h17.content)
http.write(h18.content)
http.write(h19.content)
http.write(h20.content)
http.write(h21.content)
http.write(h22.content)
http.write(h23.content)
http.write(h24.content)
http.write(h25.content)
http.write(h26.content)
http.write(h27.content)






Write.Print("[!] Finished Writing Proxies In Files!\n", Colors.white_to_red, interval=0)
time.sleep(1)
Write.Print("[+] Closing Files . . .\n", Colors.red_to_purple, interval=0)
time.sleep(1)

# Closing Files
http.close()

# Done!
Write.Print("[!] Successfully Scraped And Saved Proxies!\n\n", Colors.white_to_red, interval=0)
time.sleep(3)


def question():
    i = 0
    while i < 2:
        answer = Write.Input("Do you want to check the proxies? yes or no: ", Colors.red_to_yellow, interval=0.01)
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            os.system("python3 checker.py")
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
           
            break
        else:
            i += 1
            if i < 2:
                print('Please enter yes or no: ')
            else:
                print("Nothing done")


question()



time.sleep(1)

Write.Print("Press any key to continue . . .", Colors.white_to_red, interval=0)
input()

