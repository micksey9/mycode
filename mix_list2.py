#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print (proto)
print(proto[1])
##proto.extend("dns")
print(proto)
print(proto.extend(["dns"]))
print("Now we try append")
##print(proto.append("dns"))
print(proto.extend([22,80,443,53]))
##print(proto.append([22,80,443,53]))
