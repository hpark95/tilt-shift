import numpy as np


def lineIntersection(p1, p2, p3, p4, delta = 10 ** -10):
	# Comptue coefficients representing the line passing p1 and p2
	m1 = (p2[1] - p1[1]) / (p2[0] - p1[0] + delta)
	b1 = p1[1] - m1 * p1[0]

	# Comptue coefficients representing the line passing p3 and p4
	m2 = (p4[1] - p3[1]) / (p4[0] - p3[1] + delta)
	b2 = p3[1] - m2 * p3[0]

	# Comptue the intersection of the two lines
	x = (b2 - b1) / (m1 - m2 + delta)
	y = m1 * x + b1
	point = [x, y]
	print(point)

	return point


def determineParameters(filename, points):
	p1 = lineIntersection(points[0], points[1], points[2], points[3])
	p2 = lineIntersection(points[4], points[5], points[6], points[7])

if __name__ == '__main__':
	lineIntersection([0, 0], [2, 2], [1, -1], [-1, 1])