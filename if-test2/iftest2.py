#!/usr/bin/env python3

import ipaddress
##ipchk = "192.168.0.1"
ipchk = input("Apply an IP address: ")

try :
    ipaddress.ip_address(ipchk)

    if ipchk == "192.168.70.1" :
        print("looks like the IP address was set : " + ipchk + "this is not recommended.")
    
    else :
        print("Looks like the IP address was set: " + ipchk)

except :
    print("That does not appear to be a valid ip address")
