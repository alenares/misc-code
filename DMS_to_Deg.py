'''
tags: fme coordinates conversion
'''

import fmeobjects

# Template Class Interface:
class FeatureProcessor(object):
    def __init__(self):
        pass
    def input(self,feature):
        latitude = DMS2Deg(feature.getAttribute("geoLat"))
        longitude = -DMS2Deg(feature.getAttribute("geoLong"))
        feature.setAttribute("_latitude", latitude)
        feature.setAttribute("_longitude", longitude)
        self.pyoutput(feature)
       
    def close(self):
        pass
        
def DMS2Deg(x):
    x = x[:len(x)-1]
    x1,x2,x3 = x.partition('.')
    if len(x1) <= 3:
        case = 0
        xD = x1
        xM = 0
    elif len(x1) <= 5:
        case = 1
        xD = x1[:len(x1)-2]
        xM = x1[len(xD):]
    else:
        case = 2
        xD = x1[:len(x1)-4]
        xM = x1[len(xD):len(x1)-2]
    xS = 0
    if x3 != '':
       if case == 0:
           xD = xD + x2 + x3
       elif case == 1:
           xM = xM + x2 + x3
       else:
           xS = x1[len(xD)+len(xM):] + x2 + x3
    return (float(xD) + float(xM)/60 + float(xS)/3600)
