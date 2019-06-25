#!/usr/bin/env python3
import urllib.request
import json
import webbrowser

##Define APOD
apodurl = "https://api.nasa.gov/planetary/apod?"
mykey = "api_key=JChPoVwRpEunWQ4EsuFm4uzzkcz04YDwwhmeQVSI"

##Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

##read the file-like object
apodread= apodurlobj.read()

##decode json to python data structure

decodepad= json.loads(apodread.decode("utf-8"))

##display pythonic data

print("\n\nConverted python Data")
print(decodepad)

## use browser to open HTTPS url

input("\nPress Enter to open NASA Picture of the day in firefox")
webbrowser.open(decodepad["url"])
