import itertools
from nodebox.graphics import Point

def product(*args):
        """ return the combinatoric product of all the arguments """
	return  list(itertools.product(*args))

def productPoint(x, y):
	""" return the combinatoric pair product of lists x and y as point """
	return [ makePoint(p[0], p[1]) for p in itertools.product(x, y) ]

def makePoint(x, y):
	""" create a point or a dict """
	if type(x) == float:
		return Point(x, y)
	else:
		return { 'x': x, 'y': y }

