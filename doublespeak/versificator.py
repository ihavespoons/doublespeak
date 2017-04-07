import ipgetter
import json
from geoip import geolite2
from doublespeak.constants import *

def versificator():
    # geolocates the user to provide closest doublespeak server
    myip = ipgetter.myip()
    match = geolite2.lookup(myip)

    if(match is not None):
     country = match.country

    else:
        return(DEF_SERVER)