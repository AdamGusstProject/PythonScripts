###############################################################
#  Parses log files to extract and analyze information.
#  Creation Date:  12/30/2025
#  Revision:  
###############################################################

# Importing necessary libraries


# ANSI color codes for terminal output

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


# This function prompts the user for the log file location.

def file_location():
    file_path = input("Enter the log file path: ")
    return file_path

# This function reads a log file and returns its content.

def read_log_file(file_path):
   with open(file_path, 'r') as file:
      lines = file.readlines()
      return lines

# This function parses the log data from a syslog file.

def parse_log_data(log_data):
    parsed_data = []
    unparsed_data = []
    
    for line in log_data:

        # 1. Blank line check
        if not line.split():
            unparsed_data.append(line)
            parsed_data.append({
                "timestamp": None,
                "hostname": None,
                "process": None,
                "message": line.strip(),
                "error": "unrecognized_format"
            })
            continue

        # 2. Split into parts

        parts = line.split(None, 4)
        if len(parts) < 5:
            unparsed_data.append(line)
            parsed_data.append({
                "timestamp": None,
                "hostname": None,
                "process": None,
                "message": line.strip(),
                "error": "unrecognized_format"
            })
            continue

        # 3. Process/message must contain ":"

        process_and_message = parts[4]
        if ":" not in process_and_message:
            unparsed_data.append(line)
            parsed_data.append({
                "timestamp": None,
                "hostname": None,
                "process": None,
                "message": line.strip(),
                "error": "unrecognized_format"
            })
            continue

        # 4. Valid line -> parse normally
        process, message = process_and_message.split(":", 1)
        event_type = classify_event(process, message)
        time_stamp = parts[0] + " " + parts[1] + " " + parts[2]
        hostname = parts[3]
        parsed_data.append({"timestamp": time_stamp, "hostname": hostname, "process": process, "message": message.strip(), "event_type": event_type})
    return parsed_data, unparsed_data

# This function classifies log events based on process and message content.

def classify_event(process, message):
    process = process.lower()
    message = message.lower()

    # SSH Failures and Acceptances
    if "sshd" in process and "failed password" in message:
        return "ssh_failure"
    elif "sshd" in process and "accepted" in message:
        return "ssh_success"
    
    # Firewall (UFW) Events
    elif "ufw" in message:
        return "firewall_event"
    
    # Privilege Escalation Attempts
    elif "sudo" in process:
        return "possible_privilege_escalation"
    
    # Cron Job Executions
    elif "cron" in process or "cmd" in message:
        return "cron_job"
    
    # Kernel Warnings
    elif "kernel" in process and "warning" in message:
        return "kernel_warning"
    
    # Package Management Activities
    elif "apt" in process:
        return "package_management"
    
    # Catch-all for unclassified events
    else:
        return "General Event - No specific classification"
    


# This function runs the log file parser.

def run_parser():
  log_data = read_log_file(file_location())

  color = GREEN
  beginning_message = "Log file processed. Valid and malformed lines are shown below."
  print(color + "*" * 100 + RESET)
  print()
  print(color + beginning_message + RESET)
  print()
  print(color + "*" * 100 + RESET)
  print()

  parsed_data, unparsed_data = parse_log_data(log_data)
  event_counts = {}
  for entry in parsed_data:
        if "error" in entry:
            continue
        etype = entry["event_type"]
        event_counts[etype] = event_counts.get(etype, 0) + 1
        print()
        print(
            BLUE
            + f"Timestamp: {entry['timestamp']}, "
              f"Hostname: {entry['hostname']}, "
              f"Process: {entry['process']}, "
              f"Message: {entry['message']}"
              f" (Event Type: {etype})"
              + RESET
        )
        print()
        print(BLUE + "-" * 100 + RESET)

  print()
  print(GREEN + "\nEvent Summary:" + RESET)
  for etype, count in event_counts.items():
    print(f"{etype}: {count}")
  print()

  if unparsed_data:
    print()
    mal_color = RED
    mal_message = "The following lines could not be parsed:"
    print(mal_color + mal_message + RESET)
    for bad in unparsed_data:
        print(RED + bad.strip() + RESET)


  color = GREEN
  end_message = "This is the end of the parsed data!"
  print()
  print(color + "*" * 100 + RESET)
  print()
  print(color + end_message + RESET)
  print()
  print(color + "*" * 100 + RESET)

run_parser()