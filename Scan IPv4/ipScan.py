import scapy.all as scapy
import re

print(r"""
██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║██║         ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ """)
print("\n****************************************************************************")

#Regex to recognise IPv4 addresses
ip_regex = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

#Get the address range to ARP
while True:
    ip_regex_entered = input("\Enter the ip address and range that you want to send the ARP request to (ex : 192.168.1.0/24): ")
    if ip_regex.search(ip_regex_entered):
        print(f"{ip_regex_entered} is valid ip address range")
        break

arp_result = scapy.arping(ip_regex_entered)