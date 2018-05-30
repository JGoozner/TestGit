#!/bin/python

#Code to check to see if variable exists


import subprocess
import re
#DO import global variables as string
string_env = subprocess.check_output('env')

#DO extract only variable names using regular expression
globalNameRegex = re.compile(r'(\w+)=')
nameEx = globalNameRegex.findall(string_env)

newGlobal= "IMMATEAPOTS"
isTaken = False

#DO check to see if var is already taken
for globalEnv in nameEx:
	if newGlobal == globalEnv:
		isTaken = True
		

#- Need to allow input of new global variable name ( ignore value wanted)
#- set value if true; print cant set if false
if isTaken == False:
	subprocess.call(["ls", "-l"])
