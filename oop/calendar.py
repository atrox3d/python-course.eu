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
				"%(module)s | " + 
				"%(name)-10s:" +
				"%(funcName)-15.15s | " + 
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

class Calendar(object):

	__validday   = Validator( lambda x: type(x) == int, lambda x: 1 <= x <= 31)
	__validmonth = Validator( lambda x: type(x) == int, lambda x: 1 <= x <= 12)
	__validyear  = Validator( lambda x: type(x) == int, lambda x: x > 999)

	months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	datestyle = "british"
	
	@staticmethod
	def leapyear(year):
		"""
		"""
		log.debug("%-10.10s = %s", 'year', year)

		if not year % 4 == 0: 
			log.debug("year %s is not leap, not divisible by 4", year)
			return False
		elif not year % 100 == 0: 
			log.debug("year %s is not leap, not divisible by 100", year)
			return False
		elif not year % 400 == 0: 
			log.debug("year %s is not leap, not divisible by 400", year)
			return False
		else: 
			log.debug("year %s is leap", year)
			return True
	
	def __init__(self, day, month, year):
		"""
		"""
		log.debug("%-10.10s = %s", 'day', day)
		log.debug("%-10.10s = %s", 'month', month)
		log.debug("%-10.10s = %s", 'year', year)
		#self.setcalendar(day, month, year)
		self.day = day
		self.month = month
		self.year = year
		
	@property
	def day(self):
		return self.__day
		
	@day.setter
	def day(self, day):
		if Calendar.__validday(day):
			self.__day = day
			log.debug("%-15.15s = %s", 'set __day', self.__day)
		else:
			raise TypeError("1 <= day <=31")
	
	@property
	def month(self):
		return self.__month
		
	@month.setter
	def month(self, month):
		if Calendar.__validmonth(month):
			self.__month = month
			log.debug("%-15.15s = %s", 'set __month', self.__month)
		else:
			raise TypeError("1 <= month <=12")
	
	@property
	def year(self):
		return self.__year
		
	@year.setter
	def year(self, year):
		if Calendar.__validyear(year):
			self.__year = year
			log.debug("%-15.15s = %s", 'set __year', self.__year)
		else:
			raise TypeError("year must be 4 digits int")
	
	
		
	#def setcalendar(self, day, month, year):
	#	"""
	#	"""
	#	log.debug("%-10.10s = %s", 'day', day)
	#	log.debug("%-10.10s = %s", 'month', month)
	#	log.debug("%-10.10s = %s", 'year', year)
	#	for check in [ day, month, year ]:
	#		if not type(check) == int:
	#			log.error("parameters must be integers")
	#			raise TypeError( "parameters must be integers")
	#	
	#	if year < 1000: 
	#		log.error("year must be a 4 digit number")
	#		raise Exception( "year must be a 4 digit number")
	#	
	#	self.__day = day
	#	self.__month = month
	#	self.__year = year
		
	def __str__(self):
		if Calendar.datestyle == "british":
			value = "{:02d}/{:02d}/{:04d}".format(
													self.day,
													self.month,
													self.year
												)
		else:
			value = "{:02d}/{:02d}/{:04d}".format(
													self.month,
													self.day,
													self.year
												)
		log.debug("%-10.10s = %s", 'value', value)
		return value
		
	def advance(self):
		"""
		"""
		maxdays = Calendar.months[self.month - 1]
		log.debug("%-10.10s = %s", 'maxdays', maxdays)
		
		if self.month == 2:
			leap = Calendar.leapyear(self.year)
			log.debug("%-10.10s = %s", 'leap', leap)
			
			if leap:
				maxdays += 1
				log.debug("%-10.10s = %s", 'maxdays', maxdays)
				
		if self.day == maxdays:
			self.day = 1
			if self.month == 12:
				self.month = 1
				self.year += 1
			else:
				self.month += 1
		else:
			self.day += 1
		log.debug("%-10.10s = %s", '__str__', self.__str__())
	
		

if __name__ == "__main__":
	try:
		c = Calendar( 1, "2", 3000 )
	except Exception as e:
		log.error(e)
	try:
		c = Calendar( 1, 2, 999)
	except Exception as e:
		log.error(e)
	try:
		c = Calendar( 1, 2, 3000 )
	except Exception as e:
		log.error(e)
	
	c = Calendar( 31, 12, 3000 )
	c.advance()
	