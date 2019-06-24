#!/usr/bin/env python3

def main() :
    ##create dictionary
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version":"1.2", "vendor":"cisco"}
    print(switch["hostname"])
    print(switch["ip"])
    ##print(switch["lynx"])

    #using get function
    print("First test - .get()")
    print(switch.get("lynx"))

main ()
