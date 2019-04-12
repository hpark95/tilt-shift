import matplotlib.pyplot as plt
from PIL import Image


def selectPoints(filename):
    '''
    Let user select 8 points representing 2 pairs of parallel lines.

    Parameters:
        filename: str

    Returns:
        points: list
            - list of points respresenting 2 pairs of parallel lines
    '''
    # Show the input image
    img = Image.open(filename)
    plt.imshow(img)

    # Initialize a variable to take user inputs
    points = []

    # Take an user input for two pairs of two parallel lines
    # In total, we will collect 8 points from the user
    for num_lines in range(4):
        # Take a point from the user and plot it
        points.append(plt.ginput(n = 1)[0])
        plt.scatter(points[num_lines * 2][0], points[num_lines * 2][1], c = 'black')
        plt.draw()

        # Take another point from the user and plot it
        points.append(plt.ginput(n = 1)[0])
        plt.scatter(points[num_lines * 2 + 1][0], points[num_lines * 2 + 1][1], c = 'black')
        plt.draw()

        # Plot the line passing the two input points
        plt.plot([points[num_lines * 2][0], points[num_lines * 2 + 1][0]], [points[num_lines * 2][1], points[num_lines * 2 + 1][1]], 'black', linewidth = 1.5)

    return points


if __name__ == '__main__':
    selectPoints('airport.jpg')