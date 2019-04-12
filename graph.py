import numpy as np
from PIL import Image


def lineCoeff(p1, p2, delta = 10 ** -10):
	'''
	Find the coefficients of the line passing p1 and p2

	Parameters:
		p1: tuple
			- contains x and y coordinates of p1, i.e. [x, y]
		p2: tuple
			- contains x and y coordinates of p2, i.e. [x, y]
		delta: float
			- a constant used to avoid division by zero

	Returns:
		m: float
			- the slope of the line passing p1 and p2 (y = mx + b)
		b: float
			- the constant of the line passing p1 and p2 (y = mx + b) 
	'''
	m = (p2[1] - p1[1]) / (p2[0] - p1[0] + delta)
	b = p1[1] - m * p1[0]

	return m, b


def pointToLineDist(p, m, b):
	'''
	Find the distance between a point and a line.
	Especially, return the distance from the point p to the line y = mx + b.

	Parameters:
		p: tuple
			- contains x and y coordinates of p, i.e. [x, y]
		m: float
			- the slope of the input line y = mx + b
		b: float
			- the constant of the input line y = mx + b

	Returns:
		dist: float
			- the perpendicular distance from p to y = mx + b
			- computed by |mp_x - p_y + b| / sqrt(m^2 + 1)
	'''
	dist = np.abs(m * p[0] - p[1] + b) / np.sqrt(m ** 2 + 1)

	return dist


def lineIntersection(p1, p2, p3, p4, delta = 10 ** -10):
	'''
	Find the intersecting point of two lines: one line passing p1 and p2, and the other line passing p3 and p4

	Parameters:
		p1: tuple
			- contains x and y coordinates of p1, i.e. [x, y]
		p2: tuple
			- contains x and y coordinates of p2, i.e. [x, y]
		p3: tuple
			- contains x and y coordinates of p3, i.e. [x, y]
		p4: tuple
			- contains x and y coordinates of p4, i.e. [x, y]
		delta: float
			- a constant used to avoid division by zero

	Returns:
		point: tuple
			- contains x and y coordinates of the intersecting point

	'''
	# Comptue coefficients representing the line passing p1 and p2
	m1, b1 = lineCoeff(p1, p2)

	# Comptue coefficients representing the line passing p3 and p4
	m2, b2 = lineCoeff(p3, p4)

	# Comptue the intersection of the two lines
	x = (b2 - b1) / (m1 - m2 + delta)
	y = m1 * x + b1
	point = [x, y]

	return point


if __name__ == '__main__':
	print(lineIntersection([1, 1], [2, 2], [1, -1], [1, 1]))