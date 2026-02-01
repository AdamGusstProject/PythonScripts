###############################################################
#  Windows Defender Firewall Rule Auditor
#  Creation Date:  1/29/2026
#  Revision:  
###############################################################

# Importing necessary libraries

import csv

# ANSI color codes for terminal output

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# This fucntion defiles file path.

def file_location():
    file_path = input("Enter the log file path: ")
    return file_path

# This function looks for rule direction Inbound or Outbound

def rule_direction():
    direction = input("Are these inbound or outbound rules? Enter 1 for inbound or 2 for outbound: ")
    if direction == "1":
        return "inbound"
    else:
        return "outbound"


# This function imports the Windows Defender Firewall rules from a CSV file.

def import_firewall_rules(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        fw_rows = []
        for row in csv_reader:
            fw_rows.append(row)
        return fw_rows

def high_value(line, direction):
    print(f"Name:        {line[0]}")  # This section prints only the highlights
    print(f"Profile:     {line[2]}")
    print(f"Enabled:     {line[3]}")
    print(f"Action:      {line[4]}")
    print(f"Program:     {line[6]}")
    print(f"Local Port:  {line[10]}")
    print(f"Remote Port: {line[11]}")
    print(f"Direction:   {direction}")

# This function runs the tests

def run_test():
    color1 = GREEN
    color2 = RED
    color3 = YELLOW
    fw_rules = import_firewall_rules(file_location())
    rule_count = len(fw_rules)
    direction = rule_direction() # This is getting the firewall rule direction

    print("This is a list of all the rules.")
    for index, line in enumerate(fw_rules, start=1):
        print(color3 + "*" * 100 + RESET)  
        print()
        print(f"Rule {index}: {line}")  # This prints all records
        print()
        print(color3 + "_" * 100 + RESET) 
        print()
        print("High-Value Fields: ")
        print()
        high_value(line, direction) # This prints high value fields
        print()
    
    print()
    print(color3 + "*" * 100 + RESET)
    print()
    print(color3 + f"There are {rule_count} total firewall rules" + RESET)
    print()
    print(color3 + "##########  Analysys Complete  ##########" + RESET)
    print()
    print()
run_test()