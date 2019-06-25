#!/usr/bin/env python3

import urllib.request
import json
import turtle 
import time

##Trace the ISS - earth-orbital space station
eoss= "http://api.open-notify.org/iss-now.json"

#Call the webserv
trackiss= urllib.request.urlopen(eoss)

##put file into object
ztrack= trackiss.read()

##json 2 python data structure
result = json.loads(ztrack.decode("utf-8"))

##display our pythonic data
print("\n\nConverted Python data")
print(result)

input("\nISS data retrieved and converted. Press any key to continue. ")

location = result["iss_position"]
lat = location["latitude"]
lon= location ["longitude"]
print("\nLatitude: ", lat)
print("Longitude: ", lon)

screen= turtle.Screen() # Create screen object
screen.setup(720, 360) # set the resolution
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("iss_map.gif") ##this sets the background of screen object to iss_map
screen.register_shape("spriteiss.gif") ##make the shape of the turtle into spriteiss
iss= turtle.Turtle()
iss.shape("spriteiss.gif")
iss.setheading(90)

lon = round(float(lon)) ##lon is right now a string we first convert it to float and then round it up as we dont need crazy resolution
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)

##My location

black_lat= -77.4
black_lon= 37.2
mylocation= turtle.Turtle()
mylocation.penup()
mylocation.color("red")
mylocation.goto(black_lat, black_lon)
mylocation.dot(5)
mylocation.hideturtle()

passis= "http://api.open-notify.org/iss-pass.json"
passis= passis + "?lat" + str(black_lat) + "&lon" + str(black_lon)
response= urllib.request.urlopen(passis)
result= json.loads(response.read().decode("utf-8"))

print(result)

over= result["response"][0]["risetime"]
style= ("Arial", 6, "bold")

turtle.mainloop()
