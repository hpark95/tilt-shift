from parameters import determineParameters
from processing import selectPoints
from blur import *


if __name__ == '__main__':
	filename = 'parking_lot.jpg'
	z0 = 0.7

	points = selectPoints(filename)
	sigma, tau, v = determineParameters(filename, points)
	blurMat = calculateBlur(filename, sigma, tau, v, z0 = z0)
	applyBlur(filename, blurMat)