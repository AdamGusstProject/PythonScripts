#!/usr/bin/python3

##########################################################
#  Nmap Scanner (Doesn't check for live system)
#  Creation Date:  8/16/2021
#  Revision:  v4 1/17/2023
##########################################################


import nmap

nmScan = nmap.PortScanner()

print('''
============================
===== Nmap Scan Script =====
============================
''')

print('Welcome, this is a simple nmap automation tool.')
print("-----------------------------------------------------")

ip_address = input("Please enter the IP address to scan: ")
print("The IP you entered is", ip_address)
type(ip_address)

nmScan.scan(ip_address, '1-1024', '-sV')

print('System state: ', nmScan[ip_address].state())
print('All protocols: ', nmScan[ip_address].all_protocols())
print('TCP ports: ', nmScan[ip_address].all_tcp())
print('UDP ports: ', nmScan[ip_address].all_udp())
print(nmScan.csv())
print('Nmap has completed')