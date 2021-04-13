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
from validator import Validator


class Clock(object):

	
	__validhour   = Validator( lambda x: type(x) == int, lambda x:0<=x<24)
	__validminsec = Validator( lambda x: type(x) == int, lambda x:0<=x<60)
	
	def __init__(self, hours, minutes, seconds):
		"""
		0 < hours   < 24
		0 < minutes < 60
		0 < seconds < 60
		"""
		log.debug("%-15.15s = %s", 'hours', hours)
		log.debug("%-15.15s = %s", 'minutes', minutes)
		log.debug("%-15.15s = %s", 'seconds', seconds)
		#self.setclock(hours, minutes, seconds)
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		
	@property
	def hours(self):
		log.debug("%-15.15s = %s", 'get __hours', self.__hours)
		return self.__hours

	@hours.setter
	def hours(self, hours):
		if Clock.__validhour(hours):
			self.__hours = hours
			log.debug("%-15.15s = %s", 'set __hours', self.__hours)
		else:
			raise TypeError("0 <= hours < 24")

	@property
	def minutes(self):
		log.debug("%-15.15s = %s", 'get __minutes', self.__minutes)
		return self.__minutes

	@minutes.setter
	def minutes(self, minutes):
		if Clock.__validminsec(minutes):
			self.__minutes = minutes
			log.debug("%-15.15s = %s", 'set __minutes', self.__minutes)
		else:
			raise TypeError("0 <= minutes < 60")

	@property
	def seconds(self):
		log.debug("%-15.15s = %s", 'get __seconds', self.__seconds)
		return self.__seconds

	@seconds.setter
	def seconds(self, seconds):
		if Clock.__validminsec(seconds):
			self.__seconds = seconds
			log.debug("%-15.15s = %s", 'set __seconds', self.__seconds)
		else:
			raise TypeError("0 <= seconds < 60")

	def __str__(self):
		"""
		returns a string representing the clock value with the format "hh:mm:ss"
		"""
		value = "{:02d}:{:02d}:{:02d}".format(
												self.hours,
												self.minutes,
												self.seconds
											)
		log.debug("%-15.15s = %s", 'value', value)
		return value
		
	def tick(self):
		"""
		increments the clock value
		"""
		log.debug("%-15.15s = %s", 'before tick', self.__str__())
		if self.seconds == 59:
			self.seconds = 0
			if self.minutes == 59:
				self.minutes = 0
				if self.hours == 23:
					self.hours = 0
				else:
					self.hours += 1
			else:
				self.minutes += 1
		else:
			self.seconds += 1
		
		log.debug("%-15.15s = %s", 'after tick', self.__str__())
		#return self.__str__()

if __name__ == "__main__":
	c = Clock(23, 59, 59)
	log.info(c)
	c.tick()
	c.tick()
	c.tick()
	print('hours', c.hours)
	print('minutes', c.minutes)
	print('seconds', c.seconds)
	