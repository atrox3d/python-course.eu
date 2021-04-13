#!/usr/bin/env python3
import logging, random
#
logging.basicConfig(
	#level	= 	logging.DEBUG,
	level	= 	logging.INFO,
	format	= 	"%(asctime)s | " + 
				"%(module)-15s | " + 
				"%(name)-10s:%(funcName)-10s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	) #
log=logging.getLogger(__name__)  
#
#
#
def g01():

	p=0.5
	
	while True:
		x = 1 if random.random() < p   else 0
		log.debug( "p = %s, x = %s", p, x)
		message = yield  x

		log.debug( "message = %s", message)
		if message:
			p = message


if __name__ == "__main__":
	
	x01 = g01()

	head = "{:<10s} -> {:<4s} -> {:<4s} -> {}".format(
														'BIN',
														'INT',
														'HEX',
														'CHAR'
													)
	log.info(head)

	for x in range(10):
		binary=""
	
		for b in range(8):
			n = next(x01)
			#print(n, end="")
			binary += str(n)
	
		integer = int(binary, 2)
		character = chr(integer)
		
															
		frmt = "{bin:10s} -> {int:4d} -> {hex:<#4X} -> {char}".format(
																bin=binary,
																int=integer,
																hex=integer,
																char=character
															)
		
		log.info(frmt)
	
