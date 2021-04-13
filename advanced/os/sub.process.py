#!/usr/bin/env python3
"""

"""

import logging, subprocess, sys
#
logging.basicConfig(
    #level  =   logging.DEBUG,
    level   =   logging.INFO,
    format  =   #"%(asctime)s | " + 
                #"%(module)-15.15s | " + 
                #"%(name)-10s:" +
                #"%(funcName)-15.15s | " + 
                "%(levelname)-" + 
                    str(len("CRITICAL")) + "s | " + 
                "%(message)s",
    datefmt = '%Y/%m/%d %H:%M:%S',
    stream = sys.stdout
    ) 
#
log=logging.getLogger(__name__)

width       = 20
format      = "[shellmode:%s] %-{0}.{0}s = %s".format(width)
subformat   = " %-{0}.{0}s = %s".format(width)

if __name__ == "__main__":
    for shellmode in [False, True]:
        #
        #   let's try some ls variant
        #                                               
                                                        #################################
                                                        #                               #
                                                        #       shellmode               #
                                                        #                               #
                                                        #################################
                                                        #   False   #   True            #
        for command in  [                               #################################
                            'ls',                       #   OK      #   OK              #
                            'ls *',                     #   FAIL    #   OK              #
                            ['ls', '*'],                #   FAIL    #   ONLY 1ST PARAM  #
                            'ls ~',                     #   FAIL    #   OK              #
                            ['ls', '~'],                #   FAIL    #   ONLY 1ST PARAM  #
                            'ls -l',                    #   FAIL    #   OK              #
                            ['ls', '-l'],               #   OK      #   ONLY 1ST PARAM  #
                            ['ls', '-l ~'],             #   FAIL    #   ONLY 1ST PARAM  #
                            ['ls', '-l', '~'],          #   FAIL    #   ONLY 1ST PARAM  #
                            'ls -l $HOME',              #   FAIL    #   OK              #
                            ['ls', '-l', '$HOME'],      #   FAIL    #   ONLY 1ST PARAM  #
                            'echo $(ls  ~)',            #   FAIL    #   OK              #
                            'env',                      #   OK      #   OK              #
                        ]:
            #
            #   log the command being executed
            #
            log.info('--------------------------------------------------------------')
            log.info(format, shellmode, 'command', command)
            log.info('--------------------------------------------------------------')

            try:
				#
				#   create process
				#
                process = subprocess.Popen(
												command, 						#	command to be executed
												stdout = subprocess.PIPE,       #	open pipe to process stdout
												stderr = subprocess.PIPE,       #	open pipe to stderr
												shell = shellmode               #	shellmode flag
											)
				#
				#	wait for command to complete
				#
                process.wait()
                #
				#	check process object properties
				#
                log.info(format, shellmode, 'process.returncode', process.returncode)
                log.info(format, shellmode, 'process.stdout', process.stdout)
                log.info(format, shellmode, 'process.stderr', process.stderr)
                #
				#	log process stdout
				#
                for line in process.stdout:
                    log.info(line.decode().rstrip())
                #
				#	log process stderr
				#
                for line in process.stderr:
                    log.error(line.decode().rstrip())
					
            except Exception as e:
                log.fatal(e)
