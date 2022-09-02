#import modules
import pyfiglet
import sys
import socket
from datetime import datetime
import re

#banner of the script
def banner():
    ascii_banner = pyfiglet.figlet_format("Port Scanner")
    print (ascii_banner)

#port scanning 
def portscan():
    host = input('Enter the host to be scanned : ')
    
    print("-" * 50)

    print("Scanning Target: " + host)
    print("Scanning started at:" + str(datetime.now()))

    print("-" * 50)

    range1 = int(input('Port Start : '))
    range2 = int(input('Port End : '))

    print("-" * 50)

    for port in range (range1, range2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.25)
        result = s.connect_ex((host, port))

        if result == 0:
            print("--> Port ",port," : ", socket.getservbyport(int(port)), " OPEN")
            s.close()

#execute the script
def execute():
    banner()
    portscan()

execute()
