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

    # Take an user input for two pairs of two parallel lines
    # In total, we will collect 4 points from the user
    points = []

    for num_lines in range(4):
        points.append(plt.ginput(n = 1)[0])
        plt.scatter(points[num_lines * 2][0], points[num_lines * 2][1], c = 'black')
        plt.draw()
        points.append(plt.ginput(n = 1)[0])
        plt.scatter(points[num_lines * 2 + 1][0], points[num_lines * 2 + 1][1], c = 'black')
        plt.draw()
        plt.plot([points[num_lines * 2][0], points[num_lines * 2 + 1][0]], [points[num_lines * 2][1], points[num_lines * 2 + 1][1]], 'black', linewidth = 1.5)

    print(points)

    return points


if __name__ == '__main__':
    selectPoints('airport.jpg');