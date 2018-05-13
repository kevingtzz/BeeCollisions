#!/usr/bin/python
import folium
import branca
from Coordinates import Coordinates

bello = folium.Map(location=(6.32547929357, -75.544186527), zoom_start=14)

coordinates = Coordinates('../datasets/ConjuntoDeDatosCon100abejas.csv')

#for coor in coordinates.getCoordinates():
#    if coor[2] == False:
#        marcador = folium.Marker(location=(coor[1], coor[0]))
#    else:
#        marcador = folium.Marker(location=(coor[1], coor[0]), icon = folium.Icon(color = "red"))
#    marcador.add_to(bello)

marcador = folium.Marker(location=(6.32547929357, -75.544898999))
marcador.add_to(bello)
marcador1 = folium.Marker(location=(6.32542300030, -75.544000000), icon = folium.Icon(color = "red"))
marcador1.add_to(bello)

bello.save("bello.html")
