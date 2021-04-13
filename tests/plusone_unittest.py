#!/usr/bin/env python3

import unittest
import logging
#
logging.basicConfig(
	level	= 	logging.DEBUG,
	#level	= 	logging.INFO,
	format	= 	"%(asctime)s | " + 
				"%(module)-15s | " + 
				"%(name)-10s:%(funcName)-20s | " + 
				"%(levelname)-" + 
					str(len("CRITICAL")) + "s | " + 
				"%(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	) #
log=logging.getLogger(__name__)
#
from plusone import plusone

class PlusoneTest(unittest.TestCase):

	def setUp(self):
		log.debug("setUp")
		self.elems = [
			(-1, 0),
			( 0, 1),
			( 1, 2),
			( 5, 6),
			(10, 11),
			(20, 21),
		]

	def testCalculation(self):
		log.debug("testCalculation")
		for input, output in self.elems:
			log.debug("%d == %d", plusone(input), output)
			self.assertEqual(plusone(input), output)
			
	def tearDown(self):
		log.debug("tearDown")
		self.elems = None

if __name__ == "__main__": 
    unittest.main()


