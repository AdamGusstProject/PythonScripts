###################################################################
#  This script is used to pull Cisco device configurations via SSH.
#  Creation Date:  1/6/2026
#  Revision:  
###################################################################

# Importing necessary libraries
from netmiko import ConnectHandler
import csv
from datetime import datetime
import os

# ANSI color codes for terminal output

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


# This function connects to a Cisco device and retrieves its configuration.
def connect_to_device():
        net_connect = ConnectHandler(
            device_type='cisco_ios',
            host='10.0.0.100',
            username='*****',
            password='*****',
            secret='*****' 
        )
        net_connect.enable()
        return net_connect

def run_command(net_connect, device, command):
  output = net_connect.send_command(command)
  timestamp = datetime.now().isoformat()
  
  evidence = {
      "device": device,
      "command": command,
      "output": output,
      "timestamp": timestamp
  }
  return evidence

# This function writes the evidence to a CSV file.
def write_evidence_to_csv(evidence):
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "evidence_log.csv")

    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass
    with open(filename, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=evidence.keys())
        if not file_exists:
          writer.writeheader()
        writer.writerow(evidence)

# This function writes the evidence to a text file.
def write_evidence_to_text(evidence):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "evidence_log.txt")

    with open(filename, "a") as f:
        f.write(f"Device: {evidence['device']}\n")
        f.write(f"Command: {evidence['command']}\n")
        f.write(f"Timestamp: {evidence['timestamp']}\n")
        f.write("Output:\n")
        f.write(evidence['output'])
        f.write("\n" + ("-" * 80) + "\n\n")


# This function disconnects from the network device.
def disconnect_from_device(net_connect):
        net_connect.disconnect()

def run_test():
  net_connect = connect_to_device()
  command = ["show ip interface brief", 
  "show version", "show running-config | include hostname"]
  for cmd in command:
    evidence = run_command(net_connect, '10.0.0.100', cmd)
    write_evidence_to_csv(evidence)
    write_evidence_to_text(evidence)

    #output = get_device_configuration(net_connect)
    color = GREEN
    message = "Configuration Retrieved"
    print()
    print(color + message + RESET)
    print()
    print(color + "*" * 100 + RESET)
    print()
    print(evidence['output'])
    print()
    print(color + "*" * 100 + RESET)
    print()

  disconnect_from_device(net_connect)


run_test()