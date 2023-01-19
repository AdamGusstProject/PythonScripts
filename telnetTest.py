##############################################
#  Project:  Tests for open ports using Telnet
#  Date:  1-17-2023
#  Version: 
##############################################

from telnetlib import Telnet

print('''
    =============================
          Telnet Access Test
    =============================\n''')

# Setting up ip and port to test
ipaddy = input('What IP would you like to Telnet into: ')
porttest = int(input('What port would you like to test: '))
print('')

try:
    print('Testing Telnet access to: ', ipaddy, 'on port:', porttest)
    print('If no error is retured the port is open.')
    with Telnet(ipaddy, porttest) as tn:
        tn.interact()

except Exception as e:
    print('There was an error: ', e)