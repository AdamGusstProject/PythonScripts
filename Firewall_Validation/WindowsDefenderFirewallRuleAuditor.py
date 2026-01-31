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



# This function imports the Windows Defender Firewall rules from a CSV file.

def import_firewall_rules(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        fw_rows = []
        for row in csv_reader:
            fw_rows.append(row)

        return fw_rows


# This function runs the tests

def run_test():
    color = GREEN
    fw_rules = import_firewall_rules(file_location())
    rule_count = len(fw_rules)
    for index, line in enumerate(fw_rules, start=1):
        print(color + "*" * 100 + RESET)
        print(f"Rule {index}: {line}")
    print(color + "*" * 100 + RESET)
    print()
    print(f'There are {rule_count} total firewall rules')
    print()
run_test()