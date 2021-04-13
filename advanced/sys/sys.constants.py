#!/usr/bin/env python3
"""

"""

import logging, sys
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				#"%(module)-15.15s | " + 
				#"%(name)-10s:" +
				#"%(funcName)-15.15s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	) #
log=logging.getLogger(__name__)

format     = "sys.%-{0}.{0}s = %s".format(30)
subformat  = "	sys.%-{0}.{0}s = %s".format(30)

if __name__ == "__main__":
	#
	#	loop over all sys.* members except those __*__
	#	but include backup streams
	#
	for item in [ x for x in dir(sys) if not x.startswith("__") or x.startswith("__std") ]:
		#
		#	get current attribute
		#
		attr = getattr(sys, item)
		#
		#	for basic collections
		#
		if type(attr) in [ list, tuple, set ]:
			log.info("[")
			#
			#	for non-empty collections
			#
			if len(attr) > 0:
				for subitem in attr:
					log.info(subformat, item, subitem )
			else:
				#
				#	print empty type
				#
				log.info(subformat, item, type(attr)() )
				
			log.info("]")
		#
		#	for dictionaries
		#
		elif type(attr) == dict:
			log.info("{")
			for k, v in attr.items():
				log.info(subformat, item + "." + k, v )
			log.info("}")
		#
		#	single values
		#
		else:
			log.info(format, item, getattr(sys, item))
		