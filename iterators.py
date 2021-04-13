#!/usr/bin/env python3

import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s | %(module)-15s | %(name)-10s:%(funcName)s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#

log = logging.getLogger(__name__) 

class Reverse:
	"""
	Creates backwards-loop Iterators
	"""
	def __init__(self, data):
		#self.log = logging.getLogger(__name__) 
		self.log = logging.getLogger(self.__class__.__name__) 
		self.log.debug("data = %s", data)
		self.data=data
		self.index=len(data)
		self.log.debug("index = %s", self.index)
		
	def __iter__(self):
		self.log.debug("return self")
		return self
		
	def __next__(self):
		if self.index == 0:
			self.log.debug("StopIteration")
			raise StopIteration
		self.index -= 1
		self.log.debug("index = %s", self.index)
		self.log.debug("return : %s", self.data[self.index])
		return self.data[self.index]
		

log.info("START")

lst=[34,978,42]
log.info("lst = %s", lst)

backlist = Reverse(lst)
log.debug("backlist = %s", backlist)

for el in backlist:
	log.info("el = %s", el)

	