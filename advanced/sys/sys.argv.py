#!/usr/bin/env python3
"""

"""

import logging, sys
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				"%(module)-15.15s | " + 
				"%(name)-10s:" +
				"%(funcName)-15.15s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	) #
log=logging.getLogger(__name__)

if __name__ == "__main__":
	#
	#	iterate over argv list
	#
	for arg in sys.argv:
		log.info(arg)
	#
	#	loop over argv list by index
	#
	for i in range(len(sys.argv)):
		if i == 0:
			log.info("script name : %s", sys.argv[i])
		else:
			log.info("argument %d : %s", i, sys.argv[i])
		
		
