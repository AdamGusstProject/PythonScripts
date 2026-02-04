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

color1 = GREEN
color2 = RED
color3 = YELLOW
color4 = BLUE

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

# This fuction pulls out high value fields.

def high_value(line, direction):
    enabled_value = line[3].strip().lower()
    action_value = line[4].strip().lower()
    print(f"Name:        {line[0]}")  # This section prints only the highlights
    print(f"Profile:     {line[2]}")
    if enabled_value in ("yes", "true", "enabled", "1"):
        print(color1 + f"Enabled:     {line[3]}" + RESET)
    else:
        print(color2 + f"Enabled:     {line[3]}" + RESET)
    if action_value in ("allow", "log only", "bypass", "force allow"):
        print(color1 + f"Action:      {line[4]}" + RESET)
    else:
        print(color2 + f"Action:      {line[4]}" + RESET)
    print(f"Program:     {line[6]}")
    print(f"Local Port:  {line[10]}")
    print(f"Remote Port: {line[11]}")
    print(f"Direction:   {direction}")


def normalized_rule(csv_row):
    return{
        "Name": csv_row[0],
        "Profile": csv_row[2],
        "Enabled": csv_row[3],
        "Action": csv_row[4],
        "Program": csv_row[6],
        "Local Address": csv_row[7],
        "Remote Address": csv_row[8],
        "Protocol": csv_row[9],
        "Local Port": csv_row[10],
        "Remote Port": csv_row[11],
    }

def strict_signature(rule_dict):
    return(
        rule_dict["Name"],
        rule_dict["Profile"],
        rule_dict["Enabled"],
        rule_dict["Action"],
        rule_dict["Program"],
        rule_dict["Local Address"],
        rule_dict["Remote Address"],
        rule_dict["Protocol"],
        rule_dict["Local Port"],
        rule_dict["Remote Port"]
    )

# This function runs the tests

def run_test():
    fw_rules = import_firewall_rules(file_location())
    rule_count = len(fw_rules)
    direction = rule_direction() # This is getting the firewall rule direction
    print()
    print(color3 + """
          ==============================================
                    Firewall Rule Audit Report          
          ==============================================
          """ + RESET)
    print()

    print(color3 + "This is a list of all the rules." + RESET)
    print()
    print(color3 + "NOTE: Rule Numbering Starts at 2 to keep aligned with the CSV index." + RESET)
    print()
    signatures = {}
    for index, line in enumerate(fw_rules, start=2):
        rule = normalized_rule(line)
        sig = strict_signature(rule)
        if sig not in signatures:
            signatures[sig] = [index]
        else:
            signatures[sig].append(index)

        
        print(color3 + "*" * 100 + RESET)  
        print()
        print(f"Rule {index}: {line}")  # This prints all records
        print()
        print(color3 + "_" * 100 + RESET) 
        print()
        print(color3 + "High-value Fields: " + RESET)
        print()
        high_value(line, direction) # This prints high value fields
        print()

    print()
    print(color3 + "========== Strict Duplicate Rules ==========" + RESET)
    print()

    found_any = False
    for sig, rule_numbers in signatures.items():
        if len(rule_numbers) >1:
            print("Duplicate found: ", rule_numbers)
            found_any = True
        else:
            continue
    if not found_any:
        print("No duplicates found.")

    print()
    print(color3 + "*" * 100 + RESET)
    print()
    print(color3 + f"There are {rule_count} total firewall rules (CSV lines 2 through {rule_count + 1})" + RESET)
    print()
    print(color3 + "##########  Analysis Complete  ##########" + RESET)
    print()
    print()
run_test()