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
class CalendarClock:
	
	def __init__(
		self,
		calendar,
		clock
	):
		self.calendar = calendar
		self.clock = clock
		
	@property
	def calendar(self):
		return self.__calendar
		
	@calendar.setter
	def calendar(self, calendar):
		if type(calendar) == Calendar:
			self.__calendar = calendar
		else:
			raise TypeError("%s is not an instance of calendar, it is an instance of %s" % (calendar, type(calendar)))
	
	@property
	def clock(self):
		return self.__clock
		
	@clock.setter
	def clock(self, clock):
		if type(clock) == Clock:
			self.__clock = clock
		else:
			raise TypeError("%s is not an instance of Clock, it is an instance of %s" % (clock, type(clock)))
	
	def tick(self):
		"""
		"""
		hours = self.clock.hours
		self.clock.tick()
		log.debug("%-10.10s = %s", 'hours', hours)
		log.debug("%-10.10s = %s", 'self._hours', self.clock.hours)
		if self.clock.hours < hours:
			self.calendar.advance()
	
	def __str__(self):
		value = str(self.calendar) + ", " + str(self.clock)
		log.debug("%-10.10s = %s", 'value', value)
		return value

if __name__ == "__main__":
	ca = Calendar(1, 2, 3000)
	cl = Clock(23, 59, 59)
	cc = CalendarClock(ca, cl)
	print("\nstr\n")
	print(cc)
	print("\ntick\n")
	cc.tick()