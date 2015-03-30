
'''
tags: fme coordinates conversion
'''

import fmeobjects

# Template Class Interface:
class FeatureProcessor(object):
    def __init__(self):
        pass
    def input(self,feature):
        geoLat = decdeg2dms_lat(feature.getAttribute("latitude"))
        geoLong = decdeg2dms_long(feature.getAttribute("longitude"))
        feature.setAttribute("geoLat", geoLat)
        feature.setAttribute("geoLong", geoLong)
        self.pyoutput(feature)
       
    def close(self):
        pass
        
def decdeg2dms_long(dd):
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    decimal = "{:0.4f}".format(seconds)[-4:]
    minutes = str(int(minutes)).zfill(2) 
    seconds = str(int(seconds)).zfill(2) 
    degrees = str(int(degrees)).zfill(3)
    if negative:
        letter = 'W'
    else:
        letter = 'E'
    return "{}{}{}.{}{}".format(degrees, minutes, seconds, decimal, letter)
    
def decdeg2dms_lat(dd):
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    decimal = "{:0.4f}".format(seconds)[-4:]
    minutes = str(int(minutes)).zfill(2) 
    seconds = str(int(seconds)).zfill(2) 
    degrees = str(int(degrees)).zfill(2)
    if negative:
        letter = 'S'
    else:
        letter = 'N'
    return "{}{}{}.{}{}".format(degrees, minutes, seconds, decimal, letter)
