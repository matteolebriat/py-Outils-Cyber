#import modules
import pyfiglet
import sys
import socket
from datetime import datetime
import subprocess
import re

#clear cmd line
subprocess.call('clear', shell=True)

#banner of the script
def banner():
    ascii_banner = pyfiglet.figlet_format("Port Scanner")
    print (ascii_banner)

#port scanning 
def portscan():
    #regex to recognise IPv4 addresses
    ip_regex = re.compile("^([0-9]{1,3}.){3}.[0-9]{1,3}$")
    
    #management of error cases if the user enters something other than ipv4 address
    while True:
        host = input('Enter the IPv4 address of the host to be scanned (ex : 192.168.0.105) : ')
        if ip_regex.search(host):
            print(f"{host} is valid ip address range")
            break 

    print("-" * 50)
    print("Scanning Target: " + host)

    #start time of the script    
    time1 = datetime.now()

    print("Scanning started at:" + str(time1))

    print("-" * 50)
    print("-" * 50)
    
    port1 =int(input("First port : "))
    port2 = int(input("End port : "))
    
    print("-" * 50)
    print("-" * 50)

    #ports are open on the machine
    for port in range (port1,port2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))
        socket.setdefaulttimeout(0.25)
        if result == 0:
            print("--> Port ",port," : ", socket.getservbyport(int(port)), " OPEN")
            s.close()

    #End time of script
    time2 = datetime.now()
    
    print("-" * 50)
    print("-" * 50)
    
    #Total time of script
    totalTime = time2 - time1
    
    print("Total of Time : ",totalTime)

#execute the script
def execute():
    banner()
    portscan()
    
execute()
