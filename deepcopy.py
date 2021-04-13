#!/usr/bin/env python3
#
#	https://www.python-course.eu/python3_deep_copy.php
#
import logging
#
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s | %(module)-15s | %(levelname)-10s | %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
log=logging.getLogger(__name__) 

def logcolors():
	log.info("colours1     : %s" % colours1)
	log.info("colours2     : %s" % colours2)
	log.info("id(colours1) : %s" % id(colours1))
	log.info("id(colours2) : %s" % id(colours2))
	log.info("same id      : %s" % (id(colours1) == id(colours2)))
	log.info("------------------------------------------------------------------------")

def loglists():
	log.info("list1     : %s" % list1)
	log.info("list2     : %s" % list2)
	log.info("id(list1) : %s" % id(list1))
	log.info("id(list2) : %s" % id(list2))
	log.info("same id : %s" % (id(list1) == id(list2)))
	log.info("------------------------------------------------------------------------")

def logvars():
	log.info("%s      : %s" % ("x", x))
	log.info("%s      : %s" % ("y", y))
	log.info("id(%s)  : %s" % ("x", id(x)))
	log.info("id(%s)  : %s" % ("x", id(y)))
	log.info("same id : %s" % (id(x) == id(y)))
	log.info("------------------------------------------------------------------------")
	

log.info( "START" )
log.info( "x=3" )
x=3
log.info( "y=x" )
y=x
logvars()

log.info( "y=4" )
y=4
logvars()

log.info( "init colours1" )
colours1 = ['red', "blue"]
colours2 = colours1
log.info( "colours2 = colours1" )
logcolors()

log.info( "change colours2" )
colours2 = ["rouge", "vert"]
logcolors()

#
log.info( "colours2 = colours1" )
colours2 = colours1
logcolors()

log.info( "change colours2[1]" )
colours2[1] = "green"
logcolors()


log.info( "init list1" )
list1 = ['a','b','c','d']
log.info( "list2 = list1[:]" )
list2 = list1[:]
log.info( "change list2[1]" )
list2[1] = 'x'
loglists()


log.info( "init list1 (sublist)" )
list1 = ['a','b',['ab','ba']]
log.info( "list2 = list1[:]" )
list2 = list1[:]
loglists()

log.info( "init list1 (sublist)" )
list1 = ['a','b',['ab','ba']]
log.info( "list2 = list1[:]" )
list2 = list1[:]
log.info( "change list2[0]" )
list2[0] = 'c'
loglists()

log.info( "change sub list2[2][1]" )
list2[2][1] = 'd'
loglists()
log.warn("sub list has changed in list1")
log.info("------------------------------------------------------------------------")
log.info("NOW, USING DEEPCOPY:")
log.info("------------------------------------------------------------------------")

from copy import deepcopy

log.info( "init list1 (sublist)" )
list1 = ['a','b',['ab','ba']]
log.info( "list2 = deepcopy(list1)" )
list2 = deepcopy(list1)
log.info( "change sub list2[*]" )
list2[2][1] = "d"
list2[0] = "c"
loglists()


