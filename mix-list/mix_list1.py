#!/usr/bin/env python3


my_list = [ "192.168.0.5", 5060, "UP" ]
# index         0           1     2

#Printing out first item
print ("The first item in the list (IP): " + my_list[0] )

# Using the F-string
print(f"the second item in the list (port): " + (my_list[1])  


# Printing the last item 
print("The last item in the list (state): " + my_list[2] )


new_list = [ 5060, "80",  55, "10.0.0.1", "10.20.30.1", "ssh" ]

#             0      1     2      3          4             5

print:when I ssh into Ip address 10.0.0.1 or 10.20.30.1 i am unable to ping

print( "when I ssh into IP address " + new_list[3] + " or " + new_list[4] + "I am unable to ping"  )

