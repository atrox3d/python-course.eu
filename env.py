#!/usr/bin/env python3
#
#	usage : eval $(env.py)
#
import sys, os

os.environ['YO']="1" # won't alter parent shell

print("export YO=1") # eval $(env.py)

