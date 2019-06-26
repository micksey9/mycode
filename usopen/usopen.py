#!/usr/bin/env python3
import pyexcel
import os

from netmiko import ConnectHandler

def retv_excel(par):
    d = {}
    records= pyexcel.iget_records(file_name=par)
    for record in records:
        d.update( {record["IP"]: record["driver"]})
    return d

def ping_router(hostname):
    response = os.system("ping -c 1 " + hostname)

    if response ==0 :
        return True
    else:
        return False

def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection= ConnectHandler(device_type=dev_type, ip=dev_ip, username= dev_un, password=dev_pw)
        my_command= open_connection.send_command("show ip int brief")
    except:
        my_command= "**ISSUING COMMAND FAILED**"
    finally:
        return my_command

def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection= ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        return True
    except:
        return False

def main():
    file_location= str(input("\nWhere is the file located?"))
    entry = retv_excel(file_location)
    print("\n**** BEGIN SSH CHECKING ****")
    for x in entry.keys():
        if login_router(str(entry[x]), x, "admin", "alta3"):
            print("\n\t**IP: -" + x + " - SSH connectivity up\n")
        else:
            print("\n\t**IP: - " + x + " SSH connectivity DOWN\n")

    print("\n**** BEGIN ICMP CHECKING ****")
    for x in entry.keys():
        if ping_router(x):
            print("\n\t**IP: -"+ x + " - responding to ICMP\n")
        else :
            print("\n\t**IP: -" + X + " -NOT responding to ICMP\n")
    print("\n**** BEGIN SHOW IP INT BRIEF ****")
    for x in entry.keys():
        print("\n" + interface_check(str(entry[x]), x, "admin", "alta3"))
main()
