import ipgetter
import json
import urllib

from geoip import geolite2
from doublespeak.constants import *

def versificator():
    # geolocates the user to provide closest doublespeak server
    myip = ipgetter.myip()
    match = geolite2.lookup(myip)

    if(match is not None):
     country = match.country
     with urllib.request.urlopen("http://doublespeak.io/api/serverlist") as url:
        data = json.loads(url.read().decode())

    else:
        return(DEF_SERVER)