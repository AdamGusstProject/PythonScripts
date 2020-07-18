#!/usr/bin/python3
#  Title:  SearchTool.py
#  Date:  6/14/2020
#  Name:  Adam Gusst
#  Version: 1.0
#  This tool is used to make API calls out to VirusTotal for threat intel
#########################################################################

import requests
import json
import csv
import sys

url = 'https://www.virustotal.com/vtapi/v2/url/report'

api_key = 'put key here'

def menu():
    print('''\nThis tool is for researching IOC's through VirusTotals API.
    \nSelect and option:
    Option 1, Lookup a URL on VirusTotal
    Option 2, File upload to VirusTotal
    Option 3, Retieve file upload results
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

# Lookup a url using VT the API

def urlLookup(option1):
    searchurl = input('Enter the URL:')
    print('Looking up the domain: ' + searchurl)
    params = {'apikey': api_key, 'resource': searchurl}
    responseOutput = open(searchurl + '.txt', 'w')
    response = requests.get(url, params=params)
    print('Writing data out to file')
    responseOutput.write(str(response.json()))
    responseOutput.close()

# Uploading a file to VT using the API

def fileUpload(option2):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    myfile = input('Enter file location <path>: ')
    uploadOutput = open('uploadResults.txt', 'w')
    files = {'file': (myfile, open(myfile, 'rb'))}
    uploadResponse = requests.post(url, files=files, params=params)
    print(uploadResponse.json())
    uploadOutput.write(str(uploadResponse.json()))
    uploadOutput.close()
    print()
    print('\nYour file was uploaded and put in queue by Virustotal')
    print('\nThe upload results have been exported to a file called uploadResults.txt')

# Pulling down the results of the file upload using the VT API

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