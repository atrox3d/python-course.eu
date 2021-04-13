#!/usr/bin/env python3
import doctest
"""
	doctest will execute the same instruction pasted from
	the interactive session and test the results
"""

def fib(n):
    """ 
	Calculates the n-th Fibonacci number iteratively 
	
	>>> fib(0)
	0
	>>> fib(1)
	1
	>>> fib(10)
	55
	>>> fib(15)
	610
	
	"""
    a, b = 0, 1
    a, b = 1, 1					# <-- force error
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
	doctest.testmod()
	
