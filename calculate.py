import numpy as np
from PIL import Image
from processing import selectPoints


def lineCoeff(p1, p2, delta = 10 ** -10):
	m = (p2[1] - p1[1]) / (p2[0] - p1[0] + delta)
	b = p1[1] - m * p1[0]

	return m, b


def pointToLineDist(p, m, b):
	return np.abs(m * p[0] - p[1] + b) / np.sqrt(m ** 2 + 1)

def lineIntersection(p1, p2, p3, p4, delta = 10 ** -10):
	# Comptue coefficients representing the line passing p1 and p2
	m1, b1 = lineCoeff(p1, p2)

	# Comptue coefficients representing the line passing p3 and p4
	m2, b2 = lineCoeff(p3, p4)

	# Comptue the intersection of the two lines
	x = (b2 - b1) / (m1 - m2 + delta)
	y = m1 * x + b1
	point = [x, y]
	print(point)

	return point


def determineParameters(filename, points):
	# Initialize variables needed for computation
	img = Image.open(filename)
	p1 = lineIntersection(points[0], points[1], points[2], points[3])
	p2 = lineIntersection(points[4], points[5], points[6], points[7])
	pc = [img.size[0] / 2, img.size[1] / 2]
	vanLineCoeff = [lineCoeff(p2, p1)[0], lineCoeff(p2, p1)[1]]

	v = np.sqrt(np.abs(p1[1] * p2[1] + p1[0] * p2[0]))
	l = pointToLineDist(pc, vanLineCoeff[0], vanLineCoeff[1])

	sigma = np.pi / 2 - np.arctan(l / v)
	tau = np.arctan(vanLineCoeff[0])

	return sigma, tau

if __name__ == '__main__':
	points = selectPoints('airport.jpg')
	sigma, tau = determineParameters('airport.jpg', points)
	print(sigma)
	print(tau)