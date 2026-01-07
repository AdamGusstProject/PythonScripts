###################################################################
#  This script is used to pull Cisco device configurations via SSH.
#  Creation Date:  1/6/2026
#  Revision:  
###################################################################

# Importing necessary libraries
from netmiko import ConnectHandler

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
            username='agusst',
            password='password1'
        )
        return net_connect


# This function retrieves the device configuration.
def get_device_configuration(net_connect):
      output = net_connect.send_command('show ip interface brief')
      return output

# This function disconnects from the network device.
def disconnect_from_device(net_connect):
        net_connect.disconnect()

def run_test():
  net_connect = connect_to_device()
  output = get_device_configuration(net_connect)

  color = GREEN
  message = "Configuration Retrieved"
  print()
  print(color + message + RESET)
  print()
  print(color + "*" * 100 + RESET)
  print()
  print(output)
  print()
  print(color + "*" * 100 + RESET)
  print()

  disconnect_from_device(net_connect)


run_test()