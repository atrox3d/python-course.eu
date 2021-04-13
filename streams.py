#!/usr/bin/env python3
import sys
savestdout=sys.stdout

print("usage: %s [2>/dev/null]\n\n" % sys.argv[0])

print("%s: this is stdout" % sys.stdout.name)
sys.stdout = sys.stderr
print("%s: stderr: is this stderr?"  % sys.stdout.name)
stdoutid=id(sys.stdout)
stderrid=id(sys.stderr)
print("%s: %s" % ( sys.stdout.name, stderrid ))
print("%s: %s" % ( sys.stdout.name, stdoutid ))
print("%s: stdoutid == stderrid : %s" % (sys.stdout.name, stdoutid == stderrid))

sys.stdout=savestdout
print("%s: back to stdout" % sys.stdout.name)



