###############################################################
#  Windows Defender Firewall Rule Auditor
#  Creation Date:  1/29/2026
#  Revision:  
###############################################################

# Importing necessary libraries

import csv
import os


# ANSI color codes for terminal output

RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
RESET = "\033[0m"

BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

BOLD      = "\033[1m"
DIM       = "\033[2m"
ITALIC    = "\033[3m"
UNDERLINE = "\033[4m"
REVERSE   = "\033[7m"



# This fucntion defiles file path.

def file_location():
    while True:
        file_path = input("Enter the log file path: ")
        if os.path.exists(file_path):
            return file_path
        else:
            print(RED + f"File does not exist: {file_path}" + RESET)
        


# This function looks for rule direction Inbound or Outbound

def rule_direction():
    while True:
        direction = input("Are these inbound or outbound rules? Enter 1 for inbound or 2 for outbound: ")
        if direction == "1":
            return "inbound"
        elif direction == "2":
            return "outbound"
        else:
            print(color2 + f"Your choice was not 1 or 2: {direction}" + RESET)
        
        


# This function imports the Windows Defender Firewall rules from a CSV file.

def import_firewall_rules(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        fw_rows = []
        for row in csv_reader:
            fw_rows.append(row)
        return fw_rows


# This function creates a menu for the users to choose what they want to see.

def menu():
    while True:
        print()
        print(f'''
            {YELLOW}{BOLD}======= Firewall Rule Auditor ====== {RESET}
            {YELLOW}{BOLD}____________________________________ {RESET}
            
            {CYAN}1. Show high-value fields only {RESET}
            {CYAN}2. Show duplicate rules {RESET} 
            {CYAN}3. Search rules by port {RESET}
            {CYAN}4. Show enabled disabled counts {RESET}
            {CYAN}5. Full audit {RESET}
            {CYAN}6. Exit audit {RESET}
            ''')
        
        choice = input(f"{CYAN}Enter your selection: {RESET}").strip()
        if choice in ("1", "2", "3", "4", "5", "6"):
            return choice
        else:
            print(RED + f"You need to enter a number between 1 and 5, try again." + RESET)

# This function clears the screen and lives after the menu choice in main()

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear') # MAC and Linux




# This fuction pulls out high value fields.

def high_value(line, direction):
    enabled_value = line[3].strip().lower()
    action_value = line[4].strip().lower()
    print(f"Name:        {line[0]}")  # This section prints only the highlights
    print(f"Profile:     {line[2]}")
    if enabled_value in ("yes", "true", "enabled", "1"):
        print(GREEN + f"Enabled:     {line[3]}" + RESET)
    else:
        print(RED + f"Enabled:     {line[3]}" + RESET)
    if action_value in ("allow", "log only", "bypass", "force allow"):
        print(GREEN + f"Action:      {line[4]}" + RESET)
    else:
        print(RED + f"Action:      {line[4]}" + RESET)
    print(f"Program:     {line[6]}")
    print(f"Local Port:  {line[10]}")
    print(f"Remote Port: {line[11]}")
    print(f"Direction:   {direction}")

# This functions counts the number of rules that are enabled and disabled.

def enable_disable(line):
    enabled = line[3].strip().lower()
    if enabled in ("enabled", "true", "1", "yes"):
        return 1
    else:
        return 0


def enable_disable_sumary(fw_rules):
    enabled_counter = 0
    disabled_counter = 0
    for line in fw_rules:
        if enable_disable(line) == 1:
            enabled_counter += 1
        else:
            disabled_counter += 1

    return enabled_counter, disabled_counter

# Enable / disable function

def show_enable_disable(fw_rules):
    enabled, disabled = enable_disable_sumary(fw_rules)
    print()
    print(f"Enable rules: {enabled}")
    print(f"Disabled rules: {disabled}")
    print()

# Normalizing rules and building signatures

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

def dup_detection(fw_rules):
    signatures = {}
    index = 2
    for line in fw_rules:
        rule = normalized_rule(line)
        sig = strict_signature(rule)
        if sig not in signatures:
            signatures[sig] = [index]
        else:
            signatures[sig].append(index)
        index += 1
    return signatures

def show_duplicates(fw_rules):
    signatures = dup_detection(fw_rules)
    found_any = False
    for sig, rule_numbers in signatures.items():
        if len(rule_numbers) >1:
            print("Duplicate found: ", rule_numbers)
            found_any = True
        else:
            continue
    if not found_any:
        print("No duplicates found.")


# This function searches for port numbers

def get_port():
    while True:
        port = input("Enter the port you want to search for: ").strip()
        if port.isdigit():
            return port
        else:
            print("That port number is not in the rule set. Enter a port: ")

def search_port(fw_rules, port, direction):
    found_any = False
    for line in fw_rules:
        if line[10].strip() == port:
            high_value(line, direction)  # or print(normalized_rule(line))
            found_any = True
            print()
            print()

    if not found_any:
        print("No rules found for that port.")
        print()
        print()




# Function for full audit report

def full_audit(fw_rules, rule_count, direction):
    index = 2
    for line in fw_rules:
        print()
        print(YELLOW + """
            ==============================================
                        Firewall Rule Audit Report          
            ==============================================
            """ + RESET)
        print()
        print(YELLOW + "*" * 100 + RESET)  
        print()
        print(f"Rule {index}: {line}")  # This prints all records
        print()
        print(YELLOW + "_" * 100 + RESET) 
        print()
        print(YELLOW + "All Rules in a Dictionary" + RESET)
        print()
        print(normalized_rule(line))
        print()
        print(YELLOW + "High-value Fields: " + RESET)
        print()
        high_value(line, direction) # This prints high value fields
        print()
        index += 1

    # This section counts the enabled and disabled rules.

    enabled_counter, disabled_counter = enable_disable_sumary(fw_rules)

    print()
    print(YELLOW + "========== Enable / Disable Rule Count ==========" + RESET)
    print()
    print(f"Total number of Enabled rules: {enabled_counter}")
    print(f"Total number of Disabled rules: {disabled_counter}")


    # This sectino looks for duplicate rules

    signatures = dup_detection(fw_rules)
    print()
    print(YELLOW + "========== Strict Duplicate Rules ==========" + RESET)
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
    print(YELLOW + "*" * 100 + RESET)
    print()
    print(YELLOW + f"There are {rule_count} total firewall rules (CSV lines 2 through {rule_count + 1})" + RESET)
    print()
    print(YELLOW + "##########  Analysis Complete  ##########" + RESET)
    print()


# This function runs the tests

def main():
    fw_rules = import_firewall_rules(file_location())
    rule_count = len(fw_rules)
    direction = rule_direction() # This is getting the firewall rule direction
    print()
    print()

    while True:  # This section invokes a menu
        choice = menu()
        if choice == "1":
            clear_screen()
            for line in fw_rules:
                print()
                high_value(line, direction)
                print()
            input("Press enter to return to the menu ... ")
            continue

        elif choice == "2":
            clear_screen()
            show_duplicates(fw_rules)
            input("Press enter to return to the menu ... ")
            continue
        
        elif choice == "3":
            clear_screen()
            port = get_port()
            search_port(fw_rules, port, direction)
            input("Press enter to return to the menu...")
            continue

        elif choice == "4":
            clear_screen()
            show_enable_disable(fw_rules)
            input("Press enter to return to the menu ... ")
            continue

        elif choice == "5":
            clear_screen()
            full_audit(fw_rules, rule_count, direction)
            input("Press enter to return to the menu ... ")
            continue

        elif choice == "6":
            print()
            print("Exiting program")
            print()
        break

main()