import urllib.request
import json
majortom= "http://api.open-notify.org/astros.json"
groundctrl = urllib.request.urlopen(majortom)
helmet = groundctrl.read()
helmetson = json.loads(helmet.decode("utf-8"))
print("\n\nConverted python data")
print(helmetson)

print("\n\nPeople in Space: ", helmetson["number"])
people= helmetson["people"]
for i in people :
    print(i["name"] + " on the " + i["craft"])
