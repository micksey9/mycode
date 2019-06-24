#!/usr/bin/env python3

import shutil
import os

## now we can change or working directory for this scipt to run the copy command by running os.chdir
os.chdir("/home/student/mycode")
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

## The following copies the entire tree -- the directories subdirectories, everything to the specified location, useful for creating backup"
shutil.copytree("5g_research/", "5g_research_backup/")
