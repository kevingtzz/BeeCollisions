#!/usr/bin/python
import math

class Point:
    def __init__(self, x, y, r = 0.0009000009/2):
        self.x = x
        self.y = y
        self.r = r


    def distance (self, otherPoint):
        """
        This method implements the Pythagorean theorem to calculate the
        distance between two points.

        parameters: otherPoint = Point Object.

        returns: the distance between them. (float type)
        """
        return math.sqrt(abs(otherPoint.x - self.x) ** 2 +
                         abs(otherPoint.y - self.y) ** 2 )


    def distance_in_meters(self, otherPoint):
        return math.sqrt(abs(otherPoint.x - self.x) ** 2 +
                         abs(otherPoint.y - self.y) ** 2 ) * 111111


    def collided (self, otherPoint):
        """
        This method detects if the perimeter of a point enters the perimeter
        of another point.

        parameters: otherPoint = Point Object.

        returns: boolean Object.
        """
        return self.r + otherPoint.r > self.distance(otherPoint)

#p1 = Point(6.32547929357, -75.544898999)
#p2 = Point(6.32542300030, -75.544000000)
#
#print(p1.distance(p2))
#print(p1.distance_in_meters(p2))
#print(p1.collided(p2))
