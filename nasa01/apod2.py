#!/usr/bin/env python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp

## defins some constants
NASAAPI = "https://api.nasa.gov/planetary/apod?"
MYKEY="api_key=JChPoVwRpEunWQ4EsuFm4uzzkcz04YDwwhmeQVSI"

##pretty print json
def main():
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)
    nasaread = nasaapiobj.read()
    convertedjson= json.loads(nasaread.decode("utf-8"))

    print(convertedjson)
    input('\nThis is the converted json response, press ENTER to continue.')
    pp(convertedjson)

    ##pprint.pprint(convertedjson)
    input("\nThis is the pretty printed JSON")
    print(convertedjson["explanation"])
    input("\nPress ENTER to view this photo")
    webbrowser.open(convertedjson["hdurl"])
main ()

