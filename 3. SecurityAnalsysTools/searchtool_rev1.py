#  Title:  SearchTool.py
#  Date:  6/14/2020
#  Name:  Adam Gusst
#  Version: 1.0
#################################################################

# Libraries to import
import os
import webbrowser
import sys 
import whois
import base64


"""You will need to install the following:
   whois library - pip install python-whois
   """

# Define menu options
def menu():
    print('''\n********************************************************************************
    \nThis tool is for researching IOC's found within the environment.

    \nSelect and option:\n
    Option 1, Lookup Whois on a domain           (Exported to a text file)
    Option 2, Lookup a SHA256 hash in VirusTotal (Opens a web browser)
    Option 3, Lookup an IP in VirusTotal         (Opens a web browser)
    Option 4, Lookup an IP on AbuseIPDB site     (Opens a web browser)
    Option 5, Lookup Whois on AbuseIPDB site     (Opens a web browser)
    Option 6. Decode Base64 code                 (Writes a file and prints to screen)
    Option 7. Enter 7 to quit''')
    
    print()
    choice = input('Enter Selection: ')

    if choice == "1":
        whoIsLookup(1)
        menu()
    if choice == "2":
        hashVTLookup(2)
        menu()
    if choice == "3":
        ipVTLookup(3)
        menu()
    if choice == "4":
        AbuseIPLookup(4)
        menu()
    if choice == "5":
        AbuseWhoisLookup(5)
        menu()
    if choice == "6":
        decodedBase64(6)
        menu()
    if choice == "7":
        exitScript(7)

# Defines the "whoIs" lookup and dumps it to a text file

def whoIsLookup(Option1):
    data = input('Enter domain name:')
    whoisOutput = open(data + '.txt', 'w')
    print('Looking up the domain:' + data)
    print('Writing data out to file')
    response = whois.whois(data)
    whoisOutput.write(str(response))
    whoisOutput.close()

# Defines the hash lookup on VirusTotal
def hashVTLookup(Option2):
    hashvalue = input('Enter a hash value to lookup on VirusTotal:')
    webbrowser.open('https://virustotal.com/gui/file/' + hashvalue + '/detection')

# Defines the IP lookup on VirusTotal
def ipVTLookup(Option3):
    ipvalue = input('Enter IP address to lookup on VirusTotal:')
    webbrowser.open('https://www.virustotal.com/gui/ip-address/' + ipvalue + '/detection')

# Defines the IP lookup on the AbuseIP database
def AbuseIPLookup(Option4):
    AbuseIPDB = input('Enter IP to lookup on the IPAbuseDB site: ')
    webbrowser.open('https://www.abuseipdb.com/check/' + AbuseIPDB)

# Defines the Whois lookup on the AbuseIP database
def AbuseWhoisLookup(Option5):
    AbuseWhois = input('Enter IP to whoIS lookup on the IPAbuseDB site: ')
    webbrowser.open('https://www.abuseipdb.com/whois/' + AbuseWhois)

# Defines the Base64 decoding
def decodedBase64(Option6):
    decodedFile = open('decodedFile.txt', 'w')
    data = input('Enter string to decode using base64: ')
    response = base64.b64decode(data)
    decodedFile.write(str(response))
    decodedFile.close()
    print('Your string breaks down to:\n')
    print(response)


# Ends the program
def exitScript(Option7):
    sys.exit()

menu()