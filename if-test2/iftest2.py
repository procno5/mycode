#!/usr/bin/env python3
ipchk = '192.168.0.1'

if ipchk:
   print('Looks like the IP address was set: ' + ipchk)

#!/usr/bin/env python3
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk: # if any data is provided, this will test true
   print('Looks like the IP address was set: ' + ipchk) # indented under if


