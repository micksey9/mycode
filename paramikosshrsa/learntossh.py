#!/usr/bin/env python3

import paramiko
import os

#issue commands to the remote
def commandissue(command_to_issue) :
    ##this sshsession.exec_command returns a three tuple, but we are just interested in the stdout taht's why we read just that
    ssh_stdin, ssh_stdout, ssh_stderr= sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

our_commands= ["touch sshworked.txt", "touch create.txt", "touch files3.txt", "ls"]

for x in our_commands :
    #if you ssh to windows sometimes it returns weird byte size objects that's why we need utf-8, it takes care of that
    print(commandissue(x).decode("utf-8"))

print(dir(sshsession))
