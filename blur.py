from graph import *
import numpy as np
from PIL import Image, ImageFilter
from parameters import determineParameters
from processing import selectPoints


def calculateBlur(filename, sigma, tau, v, z0, s0 = 0.017, A = 0.0046):

	img = Image.open(filename)
	width, height = img.size
	pc = [width / 2, height / 2]

	slantAxisCoeff = [np.arctan(np.pi / 2 + tau), pc[1] - np.arctan(np.pi / 2 + tau) * pc[0]]

	blurMat = np.ndarray(shape = (width, height), dtype = int)
	for i in range(width):
		for j in range(height):
			p = [i, j]
			dist = pointToLineDist(p, slantAxisCoeff[0], slantAxisCoeff[1])
			eps = np.arctan(dist / v)

			relDist = np.cos(sigma) * np.cos(eps) / np.cos(sigma + eps)

			blurDiamRad = 2 * np.arctan(np.abs(A * s0 / z0 * (1 - 1/relDist)) / 2 / s0)
			blurDiamPix = int(round(2 * v * np.tan(blurDiamRad / 2)))
			blurMat[i][j] = blurDiamPix

	return blurMat

def applyBlur(filename, blurMat):
	img = Image.open(filename)
	px = img.load()
	finalImage = Image.new(img.mode, img.size, color = (0, 0, 0, 0))
	finalImagePx = finalImage.load()

	maxBlur = np.amax(blurMat)
	currBlurDiam = np.amin(blurMat)
	print('start: ' + str(currBlurDiam))
	print('end: ' + str(maxBlur))
	while currBlurDiam <= maxBlur:
		print('curr: ' + str(currBlurDiam))
		tempImage = Image.new(img.mode, img.size, color = (0, 0, 0, 0))
		tempImagePx = tempImage.load()
		for i in range(img.size[0]):
			for j in range(img.size[1]):
				if blurMat[i][j] == currBlurDiam:
					tempImagePx[i, j] = px[i, j]
		tempImage = tempImage.filter(ImageFilter.GaussianBlur(radius = currBlurDiam))

		finalImage = Image.fromarray(np.asarray(finalImage) + np.asarray(tempImage))
		currBlurDiam += 1
		

	finalImage.save('result.png')

if __name__ == '__main__':
	points = selectPoints('airport.jpg')
	sigma, tau, v = determineParameters('airport.jpg', points)
	blurMat = calculateBlur('airport.jpg', sigma, tau, v, z0 = 0.15)
	print(blurMat)
	applyBlur('airport.jpg', blurMat)