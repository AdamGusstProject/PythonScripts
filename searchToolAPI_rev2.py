#!/usr/bin/python3
#  Title:  SearchTool.py
#  Date:  6/14/2020
#  Name:  Adam Gusst
#  Version: 2.0
#  This tool is used to make API calls out to VirusTotal for threat intel
#########################################################################

import requests
import json
import csv
import sys
import time

url = 'https://www.virustotal.com/vtapi/v2/url/report'

api_key = 'put key here'

def menu():
    print('''\nThis tool is for researching IOC's through VirusTotals API.
    \nSelect and option:
    Option 1, Lookup a URL on VirusTotal
    Option 2, File upload to VirusTotal and retrieval
    Option 3, File upload retrieval
    Option 4, 
    Option 5. Enter 5 to quit''')

    choice = input('Enter Selection: ')

    if choice == "1":
        urlLookup(1)
        menu()
    if choice == "2":
        fileUpload(2)
        menu()
    if choice == "3":
        fileResponse(3)
        menu()
    if choice == "4":
        decodedBase64(4)
        menu()
    if choice == "5":
        exitScript(5)


def urlLookup(option1):
    searchurl = input('Enter the URL: ')
    print('Looking up the domain: ' + searchurl)
    params = {'apikey': api_key, 'resource': searchurl}
    responseOutput = open(searchurl + '.txt', 'w')
    response = requests.get(url, params=params)
    print('Writing data out to file')
    responseOutput.write(str(response.json()))
    responseOutput.close()

# Used to upload a file to Virustotal and download the results to a text file.
def fileUpload(option2):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    myfile = input('Enter file location <path>: ')
    uploadOutput = open('uploadResults.txt', 'w')
    files = {'file': (myfile, open(myfile, 'rb'))}
    uploadResponse = requests.post(url, files=files, params=params)

    reponseCode = uploadResponse.json() # writing the reponse to a variable
    scanCodeID = reponseCode['scan_id'] # pulling scan ID number from the uploadResponse dictionary

    print(uploadResponse.json())
    uploadOutput.write(str(uploadResponse.json()))
    uploadOutput.close()
    print("""\nYour file was uploaded to VT and put into their queue for scanning, the upload result info is
    saved to a file called uploadResults.txt'...waiting on response from VT....

    Do not iterrupt this process.  
    
    This program is configured to wait 5 minutes for a response from VT and will print out he results to a file called Results.txt.

    Note: If the results aren't reported, you'll need to use option 3.\n""")

    time.sleep(500)  # Adding a pause to allow Virustotal to process

    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': scanCodeID} # Taking scan ID from the variable scanCodeID
    resultsOutput = open('results.txt', 'w')
    results = requests.get(url, params=params)
    print(results.json())
    resultsOutput.write(str(results.json()))
    resultsOutput.close()

#  Used to retrieve file upload report in the event that Virustotal needed more than 5 minutes to scan it.
def fileResponse(Option3):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    scanID = input('Enter your Scan_ID: ')
    params = {'apikey': api_key, 'resource': scanID}
    resultsOutput = open('results.txt', 'w')
    results = requests.get(url, params=params)
    resultsOutput.write(str(results.json()))
    resultsOutput.close()
    print('\nResults have been exported to a file called results.txt')

def exitScript(Option5):
    sys.exit()

menu()