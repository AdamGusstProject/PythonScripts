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
    for line in log_data:
        parts = line.split(None, 4)
        process_and_message = parts[4]
        process, message = process_and_message.split(":", 1)
        time_stamp = parts[0] + " " + parts[1] + " " + parts[2]
        hostname = parts[3]
        parsed_data.append({"timestamp": time_stamp, "hostname": hostname, "process": process, "message": message.strip()})
    return parsed_data

# This function runs the log file parser.

def run_parser():
  log_data = read_log_file(file_location())

  color = GREEN
  beginning_message = "This data has been parsed successfully."
  print(color + "*" * 100 + RESET)
  print()
  print(color + beginning_message + RESET)
  print()
  print(color + "*" * 100 + RESET)
  print()
  
  parsed_data = parse_log_data(log_data)
  for entry in parsed_data:
        print(
            BLUE
            + f"Timestamp: {entry['timestamp']}, "
              f"Hostname: {entry['hostname']}, "
              f"Process: {entry['process']}, "
              f"Message: {entry['message']}"
            + RESET)
        print()
        print(BLUE + "-" * 100 + RESET)

  color = GREEN
  end_message = "This is the end of the parsed data!"
  print()
  print(color + "*" * 100 + RESET)
  print()
  print(color + end_message + RESET)
  print()
  print(color + "*" * 100 + RESET)

run_parser()