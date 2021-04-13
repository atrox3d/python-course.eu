#!/usr/bin/env python3
import logging, re
#
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(module)s | %(levelname)-" + str(len("CRITICAL")) + "s | %(message)s",
	datefmt	= '%Y/%m/%d %H:%M:%S',
	stream = sys.stdout
    )
log = logging.getLogger(__name__) 
print("################################################################################")
print("#                                                                              #")
print("#    passing function as arguments                                             #")
print("#                                                                              #")
print("################################################################################")
def functioncaller(f):
    print("calling " + f.__name__)
    f()
#
#   define some functions
#
def f1():   print("f1 here")
def f2():   print("f2 here")
def f3():   print("f3 here")
def f4():   print("f4 here")
#
#   list of functions
#
fx = [ f1, f2, f3, f4 ]
#
#   loop call functions
#
for f in fx:
    functioncaller(f)
print("################################################################################")
print("#                                                                              #")
print("#    returning functions                                                       #")
print("#                                                                              #")
print("################################################################################")
def external(extparam):

    def otherinternal():
        print("otherinternal here")
    #
    #   define ad internal function
    #   extparam is "saved" into internal scope
    #
    externalscopevar = "scope:externalscopevar"
    def internal(
                    intparam,                               # will be passed when calling internal
                    extargument=extparam                    # another way to persist
        ):
        #
        #   extparam value is accessed from internal scope
        #   externalscopevar is accessed from internal scope
        #   extargument saves extparam in a local variable
        #
        print( "externalscopevar : ", externalscopevar )
        print( "str(extparam)    : ", str(extparam)    )
        print( "extargument      : ", extargument      )
        print( "str(intparam)    : ", str(intparam)    )
        
        otherinternal()
    #
    #   return the function
    #
    return internal, otherinternal
    

try:
    internal()
except Exception as e:
    print(e)

f, g =external("external param")
print("f.__name__       : ", f.__name__)

f("internal param")
g()

print("################################################################################")
print("#                                                                              #")
print("#    simple decorator                                                          #")
print("#                                                                              #")
print("################################################################################")

def simpledecorator(function):
    print( "simpledecorator : decorating function                       : %s" % function.__name__ )
    print( "simpledecorator : doing something before calling function   : %s" % function.__name__ )
    print( "simpledecorator : calling function                          : %s" % function.__name__ )
    function()
    print( "simpledecorator : end decoration after function             : %s" % function.__name__ )

def tobedecorated():
    print("this is decorated function, yay")

simpledecorator(tobedecorated)

print("################################################################################")
print("#                                                                              #")
print("#    normal decorator                                                          #")
print("#                                                                              #")
print("################################################################################")

def normaldecorator(function):
	print( "normaldecorator	:	passing %s to functionwrapper" % function.__name__ )
	
	def functionwrapper():
		print( "normaldecorator::functionwrapper : calling %s" % function.__name__ )
		function()
		print( "normaldecorator::functionwrapper :  %s called" % function.__name__ )
	
	return functionwrapper

decorated=normaldecorator(tobedecorated)
decorated()

print("################################################################################")
print("#                                                                              #")
print("#    python  @decorator syntax                                                 #")
print("#                                                                              #")
print("################################################################################")

@normaldecorator
def justedecorateme():
	print("hello, being decorated now")

justedecorateme()

print("################################################################################")
print("#                                                                              #")
print("#    decorator with *args                                                      #")
print("#                                                                              #")
print("################################################################################")

def generaldecorator(function):
	def functionwrapper(*args, **kwargs):
		print("functionwrapper: pre %s call" % function.__name__)
		function(*args, **kwargs)
		print("functionwrapper: post %s call" % function.__name__)
	
	return functionwrapper
	
@generaldecorator
def noargs():	print("noargs")
noargs()

@generaldecorator
def onearg(arg):	print("onearg	: %s" % arg)
onearg("argument")

@generaldecorator
def oneargandlist(arg, *args):	print("oneargandlist	: %s, %s" % (arg, *args))
oneargandlist("argument", [ 1, 2, 3 ] )

@generaldecorator
def someargs(*args):	print("someargs	: %s" % [str(arg) for arg in args])
someargs(1,2,3,4)

@generaldecorator
def onlykwargs(**kwargs):	print("onlykwargs	: %s" % kwargs)
onlykwargs(one=1, two=2)

@generaldecorator
def everything(arg, *args, **kwargs):	print("everything	: %s, %s, %s" % (arg, args, kwargs))

everything("arg", "args1", "args2", one=1, two=2)
everything("arg", [ "args1", "args2" ], one=1, two=2)

print("################################################################################")
print("#                                                                              #")
print("#    parametric decorator                                                      #")
print("#                                                                              #")
print("################################################################################")

def parametric(decoratorparameter):
    def functiondecorator(function):
        def function_wrapper(functionparameter):
            print("functionwrapper::decoratorparameter : %s" % decoratorparameter)
            print("functionwrapper::functionparameter  : %s" % functionparameter)
            print("functionwrapper::calling            : %s(%s)" % (function.__name__, functionparameter))
            function(functionparameter)
        return function_wrapper
    return functiondecorator

# @syntax
@parametric("0xWhatever")
def normalfunction(x):
    print(x)

normalfunction("Hi")

# non-@ syntax
runtimedecorator = parametric("parametric-param")
decoratednormalfunction = runtimedecorator(normalfunction)
decoratednormalfunction("hi from decoratednormalfunction")


