from math import *

original = "(x**n)/(n*n**(1/2)*7**n)"
x = "7"
becoming = original.replace("x", f"({x})")

def f(fnc: str()):
	n = 1
	return eval(fnc.replace("n", "(n+1)")) / eval(fnc)

print(f(becoming))
