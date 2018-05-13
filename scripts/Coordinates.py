#!/usr/bin/python
class Coordinates:
    """
    this class read the txt file with coordinates inside.

    parameters
    ----------
    arg1 : the file path
    """

    def __init__(self, path):
        self.path = path
        self.data = []

        with open(self.path, 'r') as coordinates:
            lines = coordinates.read().splitlines()
            for l in lines:
                line = l.split(',')
                self.data.append([float(line[0]), float(line[1]), False])
            coordinates.close()

    def getCoordinates(self):
        return self.data
