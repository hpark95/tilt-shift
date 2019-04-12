from graph import *
import numpy as np
from PIL import Image
from processing import selectPoints


def determineParameters(filename, points):
	'''
	Determine parameter values for the blur effect

	Parameters:
		filename: str
			- the input filename
			- used to find the x and y coordinates of the image center
		points: tuple
			- tuple containing 8 points selected by user

	Retruns:
		sigma: float
			- the slant
			- the angle between the line of sight and surface normal
		tau: float
			- the tilt
			- the direction of the slant relative to horizontal
	'''
	# Initialize variables needed for computation
	img = Image.open(filename)
	p1 = lineIntersection(points[0], points[1], points[2], points[3])
	p2 = lineIntersection(points[4], points[5], points[6], points[7])
	pc = [img.size[0] / 2, img.size[1] / 2]
	vanLineCoeff = [lineCoeff(p2, p1)[0], lineCoeff(p2, p1)[1]]

	v = np.sqrt(np.abs(p1[1] * p2[1] + p1[0] * p2[0]))
	l = pointToLineDist(pc, vanLineCoeff[0], vanLineCoeff[1])

	# Compute the sland and tilt
	sigma = np.pi / 2 - np.arctan(l / v)
	tau = np.arctan(vanLineCoeff[0])

	return sigma, tau, v


if __name__ == '__main__':
	points = selectPoints('airport.jpg')
	sigma, tau, v = determineParameters('airport.jpg', points)
	print(sigma)
	print(tau)
	print(v)
