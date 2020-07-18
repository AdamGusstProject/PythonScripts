#!/usr/bin/python3
import nmap
import os
import sys

nmScan = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool.')
print("-----------------------------------------------------")

ip_address = input("Please enter the IP address to scan: ")
print("The IP you entered is: ", ip_address)
print()
type(ip_address)

#Testing connectivity to system

def testConnection(step1):
    print('Testing connectivity to: ' + ip_address)
    print()
    testingIP = os.system('ping -c 2 ' + ip_address)
    if testingIP == 0:
        print('System is alive')
    else:
        print('System is not alive or is blocked, exiting program')
        sys.exit()


testConnection(1)
nmScan.scan(ip_address, '1-1024', '-sV')

#def outputInfo():
#print('Nmap Version: ', nmScan.nmap_version)
print('System state: ', nmScan[ip_address].state())
print('All protocols: ', nmScan[ip_address].all_protocols())
print('TCP ports: ', nmScan[ip_address].all_tcp())
print('UDP ports: ', nmScan[ip_address].all_udp())
print(nmScan.csv())
print('Nmap has completed')

#outputInfo()

# Writing info to a text file
#outfile = open('nmapResults.txt', 'w')
#outfile.write(str(outputInfo()))
#outfile.close()


