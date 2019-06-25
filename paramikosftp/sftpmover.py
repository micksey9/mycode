#!/usr/bin/env python3
import paramiko
import os

#where are we going to connect to

t = paramiko.Transport("10.10.2.3", 22) # IP and port
t.connect(username= "bender", password= "alta3") ## this sets up ssh session

sftp = paramiko.SFTPClient.from_transport(t) ##this sets up sftp client on the bender client using the ssh session we set up throuh t
for x in os.listdir("/home/student/filestocopy/"): ##list dir basically gives a list of all files present in the path
    if not os.path.isdir("/home/student/filestocopy/"+x) : ##if this path has subdirectories then they dont get copied over only the files that are there ubder filestocopy directory get copied over to tmp
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

sftp.close()
