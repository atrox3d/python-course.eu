#!/usr/bin/env python3
#import sound
from sound import *
from sound.effects import *


try:
	print("sound           : %s" % sound)
	print("sound.effects   : %s" % sound.effects)
except Exception as e:
	print("error           : %s" % e)


