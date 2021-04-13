#!/usr/bin/env python3
"""
class simulating a clock
"""

import logging
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	#"%(asctime)s | " + 
				"%(module)s | " + 
				"%(name)-10s:" +
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
debug_value_format = "%-{0}.{0}s : %s".format(20)
class Validator:
	#def __init__(self, value, *validators):
	def __init__(self, *validators):

		#self.value = value

		self.__validators = []
		for validator in validators:
			self.add(validator)

		#log.debug(debug_value_format,  'value',			value)
		log.debug(debug_value_format,  'validators',		validators)
		#log.debug(debug_value_format,  'self.value',		self.value)
		log.debug(debug_value_format,  'self.__validators',	self.__validators)
	
	def add(self, validatorfunc):
		if callable(validatorfunc):
			log.debug(debug_value_format,  'adding validator',	validatorfunc)
			self.__validators.append(validatorfunc)
			log.debug(debug_value_format,  'self.__validators',	self.__validators)
		else:
			raise TypeError("%s is not a function" % validatorfunc)
			
	def list(self):
		log.debug(debug_value_format,  'return __validators',	self.__validators)
		return self.__validators
		
	def __call__(self, value):
		log.debug(debug_value_format,  'value',			value)
		log.debug(debug_value_format,  'self.__validators',	self.__validators)
		for v in self.__validators:
			log.debug(debug_value_format,  'next validator',	v)
			if not v(value):
				log.debug(debug_value_format,  'validated',	False)
				log.debug(debug_value_format,  'isvalid',	False)
				return False
			else:
				log.debug(debug_value_format,  'validated',	True)
		
		log.debug(debug_value_format,  'isvalid',	True)
		return True
				


#def validator(value, *valfuncs):
#	for v in valfuncs:
#		if not v(value):
#			return False
#	
#	return True


if __name__ == "__main__":
	v = Validator()
	v = Validator(lambda x: type(x) == int, lambda x: 0<=x<10)
	v.add(lambda x:x>6)
	v.list()
	print(v.isvalid(7))