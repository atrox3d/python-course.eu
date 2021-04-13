#!/usr/bin/env python3
import logging
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


def loopbuffer( init ):
	
	buffer		= init
	position	= 0
	element		= None
	message		= None
	
	def logstatus(display=None):
	
		if display:
			log.debug( "--------------------------------------------------------")
			log.debug( display)
			log.debug( "--------------------------------------------------------")
		
		log.debug( "	[%-20.20s] '%s'", "buffer",	buffer )
		log.debug( "	[%-20.20s] '%s'", "buffer remaining",	buffer[position:] )
		log.debug( "	[%-20.20s] %s", "position",	position )
		log.debug( "	[%-20.20s] %s", "element",	element )
		log.debug( "	[%-20.20s] %s", "message",	message )
	

	logstatus("start")
	
	if init == None or len(init) == 0 : 
		log.error( "empty init buffer, exiting" )
		return
	
	#try:
	while True:
		try:
			element =  buffer[position]
			logstatus("pre-yield")
			
			message = yield element
			
			if isinstance(message, dict):
				log.debug("message %s is dict", message)
				for key, value in message.items():
					log.debug("message key   : %s", key)
					log.debug("message value : %s", value)
				
				if key.lower() == "init":
					log.debug("set buffer to  : %s", value)
					buffer = value
					position = -1
			
			position += 1
			logstatus("post-yield")
		except GeneratorExit as ge:
			log.error("#########################################################")
			log.error("GeneratorExit	: %s", ge )
			log.error("#########################################################")
			return
		except:
			log.warn( "--------------------------------------------------------")
			log.warn( "*** end of the buffer reached, resetting position ***")
			position=0
		
	#except :
	#	return


if __name__ == "__main__":
	#del loopbuffer
	#reload(gen)
	#loopbuffer=gen.loopbuffer
	lp=loopbuffer("efg")
	
	for n in range(4):
	
		log.debug("--> call next()")
		c = next(lp)
		log.info( "[%-20.20s] '%s'", "next()",	c)
		
		log.debug("--> call next()")
		c = next(lp)
		log.info( "[%-20.20s] '%s'", "next()",	c)
		
		log.debug("--> call next()")
		c = next(lp)
		log.info( "[%-20.20s] '%s'", "next()",	c)

		log.debug("--> call send('{init:blue')")
		c = lp.send({"init":"blue"})
		log.info( "[%-20.20s] '%s'", "send({init:blue})",	c)
		