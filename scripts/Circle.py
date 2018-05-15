#!/usr/bin/python
import math

class Circle:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.r = 0.0009000009/2
        self.rSquared = self.r * self.r


    def contains(self, point):
        d = (point.x - this.x)**2 + (point.y - this.y)**2
        return d <= self.rSquared


    def intersects(self, range):
        xDist = abs(range.x - self.x)
        yDist = abs(range.y - self.y)

        r = self.r
        w = range.w
        h = range.h

        edges = (xDist - w)**2 + (yDist - h)**2

        #no intersection
        if xDist > (r + w) or yDist > (r + h):
            return False

        #intersection within the circle
        if xDist <= w or yDist <= h:
            return true;

        #intersection on the edge of the circle
        return edges <= this.rSquared;
