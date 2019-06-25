#!/usr/bin/env python3
import requests

def main() :
    neourl= "https://api.nasa.gov/neo/rest/v1/feed?"
    startdate= "start_date=2018-06-01"
    end_date= "&end_date=END_DATE"
    mykey= "&api_key=JChPoVwRpEunWQ4EsuFm4uzzkcz04YDwwhmeQVSI"

    neourl= neourl + startdate + mykey
    neojson= (requests.get(neourl)).json()
    print(neojson)
main()
