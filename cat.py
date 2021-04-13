#!/usr/bin/env python3
import sys
import logging
#
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s %(module)-15s %(levelname)-10s %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
	)
#
log=logging.getLogger(__name__) 

options={}						# options dict
options['linenumbers']=False	# init
options['filename']=False		# init

files=[]						# files list
files.append('/dev/stdin')		# init with default stdin

i=1
for arg in sys.argv[1:]:						#	loop over arguments excluding script name
	if arg.startswith('-'):						#	is it an -option?
		for opt in arg[1:]:						#	loop over every char excuding -
			if 'n' == opt:						#	n : linenumbers
				options['linenumbers']=True
			if 'N' == opt:						#	N : filename
				options['filename']=True
		sys.argv.pop(i)							#	remove argument
	else:
		files.append(arg)						#	not an option, then a filename

#
#	some debugging
#		
log.debug("%-10.10s: %s", "options", options)
log.debug("%-10.10s: %s", "files",   files)
#
#	prints file with optional leading filename, line number
#
def catfile(fp, linenumbers=False, filename=False):
	log.debug("%-10.10s( %s, %s, %s )",
		sys._getframe().f_code.co_name,	#	current function name
		fp.name, 						#	file name
		linenumbers,					#	linenumbers flag
		filename						#	filename flag
		)
	
	linenumber=0						#	let's start
	format=""							#	ready to create the format
	if filename:	format+="%s :"		#	+ filename format char
	if linenumbers: format+="%4d :"		#	+ linenumber format char
	
	format+="%s"						#	+ line format char
	
	log.debug("%-10.10s: %s", "format", format)
	
	for line in fp:						#	loop over each line
		linenumber+=1					# 	increment linenumber
		args=[]
		if filename:					#	if filename enabled
			args.append(fp.name)		#	append filename to arg list
			
		if linenumbers:					#	if linenumbers enabled
			args.append(linenumber)		#	append line number to arg list

		args=tuple(args)				#	create tuple for the % format operator
		args+=tuple([line.rstrip()])	#	add the line to args
		
		log.debug("%-10.10s: %s", "args", args)
		
		print(format % args)			# print with right format and arguments
	

for file in files:						# loop over files list

	log.debug("%-10.10s: %s", "file", file)
	
	try:								#	let's try to 
		with open(file) as fp:			#		open file
			catfile(fp, **options)		#	call catfile with keyword arguments **expansion
	except (KeyboardInterrupt) as err:			#	intercept ANY error
		sys.exit(1)
	except (Exception) as err:			#	intercept ANY error
		print( "error with file %s : %s" % (file, err) )
		sys.exit(1)
		
#linenumber=0
#try:
#	for line in sys.stdin:
#		linenumber+=1
#		if options['linenumbers']:
#			print("%d %s" % (linenumber, line.rstrip()))
#		else:
#			print(line.rstrip())
#except KeyboardInterrupt:
#	sys.exit()
	
