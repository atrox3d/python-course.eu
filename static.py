#!/usr/bin/env python3
#
#	simulating static vars using attributes and decorators
#
import logging
import sys
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s | %(module)-15s | %(name)-10s:%(funcName)-10s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
log = logging.getLogger(__name__) 
#
#	static decorator
#	accept a function and return a wrapper containing the "static" attribute
#
#	the function cannot see the outer scope, because it's not defined, just called
#
def static(f):
	log.debug("	-> entering static decorator")
	#
	#	local variable, visible in the wrapper's closure
	#
	static_var=0
	#
	#	wrapper function
	#
	def wrapper():
		log.debug("		--> entering static::wrapper")
		nonlocal static_var
		#
		#	init wrapper attribute
		#
		if not getattr(wrapper, 'staticval', None) :
			wrapper.static_attr=0
		#
		log.debug("		dir  %s : %s", wrapper.__name__, [ attr for attr in dir(wrapper) if not attr.startswith("_") ] )
		log.debug("		before %s: static_attr = %d", wrapper.__name__, wrapper.static_attr)
		#
		#	call f() from wrapper
		#
		f()
		log.debug("		after %s: static_attr = %d", wrapper.__name__, wrapper.static_attr)
		log.debug("		wrapper %s : static_var : %s", wrapper.__name__, static_var)
		#
		#	increment wrapper's local (closure)
		#
		static_var += 1
		#
		log.debug("		after %s: static_attr = %d", wrapper.__name__, wrapper.static_attr)
		log.debug("		<-- returning from static wrapper")
	#
	log.debug("	<- returning from static decorator")
	return wrapper

@static
def f():
	#log.debug("type %s : %s", f.__name__, type(f))
	log.debug("			dir  %s : %s", f.__name__, [ attr for attr in dir(f) if not attr.startswith("_") ] )
	#log.debug(type(f.static_attr))
	f.static_attr += 1

#
#	f IS static::wrapper now
#
#log.debug("type %s : %s", f.__name__, type(f))
log.debug("dir  %s : %s", f.__name__, [ attr for attr in dir(f) if not attr.startswith("_") ] )
f()
f()
f()
f()
