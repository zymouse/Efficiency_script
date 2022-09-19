
#!/usr/bin/env python3
#！-*- coding:utf-8 -*-
from pyproj import Transformer
 
 
transformer = Transformer.from_crs("epsg:4326", "epsg:32648") 
 
lat = 22.744435950
lon = 113.595417400
x, y = transformer.transform(lat, lon)

print("x:", x, "y:", y)
lat = 26.7487259482772
lon = 106.668773828569


