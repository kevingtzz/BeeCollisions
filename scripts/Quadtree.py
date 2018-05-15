#!/usr/bin/python
import folium
import branca
from Coordinates import Coordinates
from Rectangle import Rectangle
from Point import Point

map = folium.Map(location=(6.32547929357, -75.544186527), zoom_start=14)

class Quadtree:

    def __init__(self, boundary, capacity):
         """
         This method instantiates the Quadtree class.

         Parameters:
            Arg1: boundary (Rectangle Object)
            Arg2: capacity (integer Object)
        """
         self.boundary = boundary
         self.capacity = capacity
         self.points = []
         self.divided = False
         self.noSpace = False


    def subdivide(self):

        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w/2
        h = self.boundary.h/2

        nw = Rectangle(x - w/2, y + h/2, w/2, h/2)
        ne = Rectangle(x + w/2, y + h/2, w/2, h/2)
        sw = Rectangle(x - w/2, y - h/2, w/2, h/2)
        se = Rectangle(x + w/2 ,y - h/2, w/2, h/2)

        self.northeast = Quadtree(ne, self.capacity)
        self.northwest = Quadtree(nw, self.capacity)
        self.southwest = Quadtree(sw, self.capacity)
        self.southeast = Quadtree(se, self.capacity)

        self.divided = True


    def insert (self, point):

        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            point.marker.add_to(map)
            return True
        else:
            if (self.boundary.w < 0.0009000009*2 and
                self.boundary.h < 0.0009000009*2):
                self.noSpace = True

            if not self.divided:
                self.subdivide()
            if self.northwest.insert(point):
                return True
            elif self.northeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True


    def query(self, range, found):
        if not found:
            found = []

        if not self.boundary.intersects(range):
            return
        else:
            for p in self.points:
                if range.contains(p):
                    found.push(p)
                if self.divided:
                    self.northwest.query(range, found)
                    self.northeast.query(range, found)
                    self.southwest.query(range, found)
                    self.southeast.query(range, found)
        return found


    def addMarkers(self, points):
        for p in points:
            marcador = folium.Marker(location=(coor[1], coor[0]),
                                      icon = folium.Icon(color = "red"))
            marker.add_to(map)


boundary = Rectangle(-75.5579529, 6.3373199, 0.1, 0.07)
quadtree = Quadtree(boundary, 4)
coordinates = Coordinates('../datasets/ConjuntoDeDatosCon100abejas.csv')

for coordinate in coordinates.getCoordinates():
    p = Point(coordinate[0], coordinate[1])
    quadtree.insert(p)

map.save("map.html")
