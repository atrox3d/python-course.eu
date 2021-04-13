#!/usr/bin/env python3.6
import logging
import random
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s | %(module)-15s | %(name)-10s:%(funcName)-10s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
log = logging.getLogger(__name__) 

def getline(width=50, char="#"):
	return char*width

def logbanner( message, linewidth=50, logfunc=log.info,  char="#"):
	logfunc(getline(linewidth,char=char))
	logfunc(message)
	logfunc(getline(linewidth,char))

logbanner(
	"stdformat:FLOATS",
	#logfunc=log.debug
)

floats = [ x * random.random() for x in range(0, 50, 5) ]
for f in floats:
	log.info("%-6s %%6.2f	: %6.2f", "float", f )

logbanner(
	"stdformat:HEX",
	#logfunc=log.debug
	char='-'
)

width=10

log.info("%-*s %%-6x	: %-6x"  , width, "hex", 42 )
log.info("%-*s %%-#6x	: %-#6x" , width, "hex", 42 )
log.info("%-*s %%#6x	: %#6x"  , width, "hex", 42 )
log.info("%-*s %%#6x	: %#6x"  , width, "hex", 42 )
log.info("%-*s %%#6X	: %#6X"  , width, "hex", 42 )
log.info("%-*s %%#6.6x	: %#6.6x", width, "hex", 42 )


logbanner(
	"newformat:STRINGS",
	#logfunc=log.debug
	char='-'
)
log.info("{}".format("{}"))
log.info("{0}".format("{0}"))

log.info("{:s}".format("{:s}"))
log.info("{0:s}".format("{0:s}"))

log.info("{:20s}".format("{:20s}"))
log.info("{0:20s}".format("{0:20s}"))

log.info("{:<20.20s}".format("{:20.20s}"))
log.info("{0:<20.20s}".format("{0:20.20s}"))

log.info("{:.<20.20s}".format("{:.<20.20s}"))
log.info("{0:.<20.20s}".format("{0:.<20.20s}"))

log.info("{:.>20.20s}".format("{:.>20.20s}"))
log.info("{0:.>20.20s}".format("{0:.>20.20s}"))

log.info("{:.^20.20s}".format("{:.^20.20s}"))
log.info("{0:.^20.20s}".format("{0:.^20.20s}"))


logbanner(
	"newformat:DICT",
	#logfunc=log.debug
	char='-'
)
log.info("{first}, {second}".format(first="{first}", second="{second}"))

dic={'first' : "{first}", 'second' : "{second}"}
log.info("{first}, {second}".format(**dic))


logbanner(
	"string format methods",
	#logfunc=log.debug
	char='-'
)
log.info("center(30, '#')".center(30, '*'))
log.info("ljust(30, '#')".ljust(30, '*'))
log.info("rjust(30, '#')".rjust(30, '*'))
log.info("zfill(30, '#')".zfill(30))


logbanner(
	"Formatted String Literals",
	#logfunc=log.debug
	char='-'
)
price=1.23
log.info(f"Price      : {price}")
log.info(f"Price * 10 : {price * 10}")

for article in ["bread", "butter", "tea"]:
	log.info(f"{article:>10}:")
