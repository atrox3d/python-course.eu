#!/usr/bin/env python3
"""
class simulating a calendar
"""

import logging
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

from clock import Clock
from calendar import Calendar
#
#
#
class CalendarClock(Clock, Calendar):
	
	def __init__(
		self,
		day,
		month,
		year,
		hours,
		minutes,
		seconds
	):
		#
		#	play with args : get list of arg keys in reverse order except self
		#
		args = [ arg for arg in list(locals().keys())[::-1] if  not arg == 'self' ]
		for arg in args:
			log.debug("%-10.10s = %s", arg, locals()[arg])
		
		Clock.__init__( self, hours, minutes, seconds )
		Calendar.__init__( self, day, month, year )
	
	def tick(self):
		"""
		"""
		hours = self.hours
		Clock.tick(self)
		log.debug("%-10.10s = %s", 'hours', hours)
		log.debug("%-10.10s = %s", 'self._hours', self.hours)
		if self.hours < hours:
			self.advance()
	
	def __str__(self):
		value = Calendar.__str__(self) + ", " + Clock.__str__(self)
		log.debug("%-10.10s = %s", 'value', value)
		return value

if __name__ == "__main__":
	cc = CalendarClock(1, 2, 3000, 23, 59, 59)
	print("\nstr\n")
	print(cc)
	print("\ntick\n")
	cc.tick()