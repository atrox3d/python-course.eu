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
	save_stdout = sys.stdout
	#
	#	loop over standard streams
	#
	for stream in [ sys.stdin, sys.stdout, sys.stderr, save_stdout ]:
		log.info("stream name: %s", stream.name)
		log.info("stream     : %s", stream)
		#
		#	will fail on stdin
		#
		try:
			stream.write("hello from %s \n" % stream.name)
		except Exception as e:
			log.error(e)
	
	log.info("save_stdout is sys.stdout : %s", save_stdout is sys.stdout)
	log.info("save_stdout == sys.stdout : %s", save_stdout == sys.stdout)
	#
	#	use first argument if provided or default if not
	#
	outputfile = sys.argv[1] if len(sys.argv) > 1 else "default.txt"
	
	try:
		sys.stdout = open(outputfile, 'w')
		print("theese should go to file %s"    % outputfile)
		print("save_stdout is sys.stdout : %s" % (save_stdout is sys.stdout))
		print("save_stdout == sys.stdout : %s" % (save_stdout == sys.stdout))
		sys.stdout.close()
	except Exception as e:
		log.error(e)
	
	sys.stdout = save_stdout
	print("theese should go to file stdout")
	print("save_stdout is sys.stdout : %s" % (save_stdout is sys.stdout))
	print("save_stdout == sys.stdout : %s" % (save_stdout == sys.stdout))
	
	
	