#!/usr/bin/env python3
##using csv data
import csv

def main():
    # open the csv data set
    with open("vendor.csv", "r") as vendorfile:
        ven_data = csv.reader(vendorfile, delimiter=",")
        for row in ven_data:
            print("The IP address " + row[2] + " requires the driver " + row[3])

main ()
