from graph import *
import numpy as np
from PIL import Image
from processing import selectPoints


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
