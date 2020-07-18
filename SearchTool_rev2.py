#!/usr/bin/python3
#  Title:  SearchTooliTotal.py
#  Date:  6/14/2020
#  Name:  Adam Gusst
#  Version: 1.0
#################################################################

# Libraries to import
import os
import webbrowser
import sys
import base64
import whois

# Define menu options
def menu():
    print('''\nThis tool is for researching IOC's found within the environment.
    \nSelect and option:
    Option 1, Lookup a SHA256 hash in VirusTotal
    Option 2, Lookup an IP on threat intel sites
    Option 3, Lookup Whois on AbuseIPDB site
    Option 4, Decode base64
    Option 5. Download whoIS data to a text file
    Option 6. Enter 6 to quit''')

    choice = input('Enter Selection: ')

    if choice == "1":
        hashVTLookup(1)
        menu()
    if choice == "2":
        ipVTLookup(2)
        menu()
    if choice == "3":
        AbuseWhoisLookup(3)
        menu()
    if choice == "4":
        decodedBase64(4)
        menu()
    if choice == "5":
        whoIsLookup(5)
        menu()
    if choice == "6":
        exitScript(6)

# Defines the "whoIs" lookup and dumps it to a text file
def hashVTLookup(Option1):
    hashvalue = input('Enter a hash value to lookup on VirusTotal:')
    webbrowser.open('https://virustotal.com/gui/file/' + hashvalue + '/detection')

# Looks up an IP in Virustotal and the abuseIP database
def ipVTLookup(Option2):
    ipvalue = input('Enter IP address to lookup: ')
    webbrowser.open('https://www.virustotal.com/gui/ip-address/' + ipvalue + '/detection')
    webbrowser.open('https://www.abuseipdb.com/check/' + ipvalue)
    webbrowser.open('https://talosintelligence.com/reputation_center/lookup?search=' + ipvalue)

# Looks up the whoIs data on an IP in the AbuseIP database
def AbuseWhoisLookup(Option3):
    AbuseWhois = input('Enter IP to whoIS lookup on the IPAbuseDB site: ')
    webbrowser.open('https://www.abuseipdb.com/whois/' + AbuseWhois)

# Decodes a Base64 string
def decodedBase64(Option4):
    decodedFile = open('decodedFile.txt', 'w')
    data = input('Enter string to decode using base64: ')
    response = base64.b64decode(data)
    decodedFile.write(str(response))
    decodedFile.close()
    print('Your string breaks down to:\n')
    print(response)

def whoIsLookup(Option5):
    data = input('Enter domain name:')
    whoisOutput = open(data + '.txt', 'w')
    print('\nLooking up the domain:' + data)
    print('\nWriting data out to file called ' + data + '.txt')
    response = whois.whois(data)
    whoisOutput.write(str(response))
    whoisOutput.close()
    
# Exits program
def exitScript(Option6):
    sys.exit()

menu()