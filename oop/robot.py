#!/usr/bin/env python3
import logging
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				"%(module)s | " + 
				#"%(name)-10s:" +
				"%(funcName)-10s | " + 
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
class Robot:
	#
	#	private class attribute
	#
	__counter = 0
	#
	#	class attribute declared inside class
	#	Robot.insideclassattr
	#
	@staticmethod
	def getinstances():
		return Robot.__counter
	
	insideclassattr = "this is a class attribute"
	#
	#	constructor
	#
	def __init__(self, name = 'Nameless'):
		#
		#
		#
		type(self).__counter += 1
		log.debug("%-15.15s : %s", 'type(self)', type(self) )
		#self.name = name
		self.setname(name)														#	instance.name
		
		self.public = 'public'													#	instance.public
		self._protected = 'protected'                                           #	instance._protected
		self.__private = 'private'                                              #	instance.__private
		
		log.info("ROBOT %s has been created", self.name)
	#
	#	destructor
	#
	def __del__(self):
		log.debug("ROBOT %s has been destroyed", self.name)
	#
	#	method
	#
	def hello(self):
		log.info('hello from ' + self.name)
	#
	#	setter
	#
	def setname(self, name):
		log.debug('%-15.15s : %s', 'setname', name)
		self.name = name
	#
	#	getter
	#
	def getname(self):
		log.info('%-15.15s : %s' 'getname', self.name)
		return self.name
	#
	#	representation
	#
	def __repr__(self):
		return "{}('{}')".format(self.__class__.__name__, self.name)
	#
	#	string
	#
	def __str__(self):
		return "{} : {}".format(self.__class__.__name__, self.name)

		
		
		

if __name__ == "__main__":
	#
	#	class attribute declared outside class
	#
	Robot.outsideclassattr =  "Robot class's attribute defined outside, same as insideclassattr"
	Robot.attr1            =  "Robot class's attribute with same name of instance attribute, will be overridden"
	#
	#	some class info
	#
	log.info("%-15.15s : %s", 'Robot', Robot)
	for d in filter(lambda x: not x.startswith("__"), dir(Robot)):
	#for d in dir(Robot):
		log.info("%15.15s : %s = %s", 'contents', d, getattr(Robot,d)     )
	log.info("%15.15s : %s", 'attr1', Robot.attr1     )
	log.info("..................................................................")
	
	for k, v in Robot.__dict__.items():
		log.info("%15.15s : { %-15.15s : %s }", '__dict__', k, v )
	
	log.info("..................................................................")
	log.info("%15.15s : %s", 'getattr attr1', getattr(Robot, 'attr1' ))
	log.info("%15.15s : %s", 'repr', repr(Robot))
	log.info("%15.15s : %s", 'str', str(Robot))
	log.info("------------------------------------------------------------------")
	#
	#	two instances
	#
	r2d2 = Robot('R2D2')
	c3po = Robot('C3PO')
	#
	#	instance attribute
	#
	r2d2.attr1 = "r2d2 instance's attribute attribute with same name of class attribute"
	c3po.attr1 = "c3po instance's attribute attribute with same name of class attribute"
	#
	#	loop over instances
	#
	for r in [ r2d2, c3po ]:
		r.instanceattr = "this is an instance attribute"
		
		log.info("%-15.15s : %s", 'robot', r)
		#
		#	loop over non hidden properties
		#
		for d in filter(lambda x: not x.startswith("__"), dir(r)):
			log.info("%15.15s : %s = %s", 'contents', d, getattr(r,d)     )
		
		log.info("%15.15s : %s", 'attr1', r.attr1     )
		#
		#	loop over dict items
		#
		log.info("..................................................................")
		for k, v in r.__dict__.items():
			log.info("%15.15s : { %-15.15s : %s }", '__dict__', k, v )
		log.info("..................................................................")
		
		log.info("%15.15s : %s", 'getattr attr1', getattr(r, 'attr1' ))
		log.info("%15.15s : %s", 'repr', repr(r))
		log.info("%15.15s : %s", 'str', str(r))
		r.hello()
		log.info("%15.15s : %s", 'r.public', r.public)
		log.info("%15.15s : %s", 'r._protected', r._protected)
		try:
			log.info("r.__private  : %s", r.__private)
		except Exception as e:
			log.error(e)
		
		log.info("------------------------------------------------------------------")
	log.info( "%-15.15s : %d", '# of robots', Robot.getinstances())

