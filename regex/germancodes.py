#!/usr/bin/env python3
""" https://www.python-course.eu/python3_re.php """
import re
from urllib.request import urlopen
import logging
import sys
#
logging.basicConfig(
	level	= 	logging.INFO,
	format	= 	"%(asctime)s | " + 
				#"%(module)-15s | " + 
				#"%(name)-10s:%(funcName)-10s | " + 
				"%(levelname)-" + 
				str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
log = logging.getLogger(__name__) 
#
url			= 'https://www.python-course.eu/post_codes_germany.txt'
urlfile		= url.split('/')[-1]
#
with urlopen(url) as gc:							# 	open online resource
	charset		= gc.info().get_content_charset()	#	get charset
	citycodes	= {}								#	codes dict

	for line in gc:                             	#	loop over content
	
		line = line.decode(charset).rstrip()		# decode and remove \n
	
		log.debug(
					"%s : %s",
					urlfile,
					line							#	decode every line
				)
				
		mo = re.search(
						r'''
						[\d ]+
						# ([^\d]+[a-z])"			# fails with german chars
						([^\d\s]+)					# city
						\s+
						(\d+)						# postcode
						'''
					,
					line,
					re.VERBOSE
				)
				
		if mo: 
			log.debug("'%s', %s", mo.group(), mo.groups())
			
			city, postcode = mo.groups()
			log.debug("city = [%-20.20s], postcode=[%s]", city, postcode)

			if city in citycodes:
				log.debug("[%-20.20s] found in city codes", city)
				citycodes[city].add(postcode)
			else:
				log.debug("[%-20.20s] NOT found in citycodes, adding ", city)
				citycodes[city] = {postcode}
				
		else:
			log.warning("regexp FAIL")
			log.warning(line)


localfile	= 'german.population.txt'

with open(localfile, encoding="utf-8") as gp:		# 	open data file
	for line in gp:                             	#	loop over content
		log.debug(
					"%s : %s",
					localfile,
					line.rstrip()					
				)

		mo = re.search(
						r'''
						^[0-9]{1,2}\.
						\s+
						([\w\s-]+\w)				#	city name
						\s+
						[0-9]
						
						'''
					,
					line.rstrip(),
					re.VERBOSE
				)

		if mo: 
			log.debug("'%s', %s", mo.group(), mo.groups())
			city=mo.group(1)
			log.debug("city = [%s]", city)

			if city in citycodes:
				log.debug("[%-20.20s] found", city)
				print("[%s]" % city)
				print(citycodes[city])
			else:
				log.warning("[%-20.20s] NOT found", city)

