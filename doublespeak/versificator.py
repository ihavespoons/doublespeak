# Provides load balancing capabilities based on region for available documentation libraries

# IMPORTS
import ipgetter
import json
import urllib

from geoip import geolite2
from doublespeak.constants import *
from doublespeak.minipax import *



# IMPORTS
def versificator():
        # geolocates the user to provide closest doublespeak server
    myip = ipgetter.myip()
    match = geolite2.lookup(myip)

    if(match is not None):
        country = match.country
        with urllib.request.urlopen("http://doublespeak.io/api/serverlist") as url:
            data = json.load(url.read().decode())
        if (country in data):
            speakserver = data['country']
            configupdater('main','server', speakserver)
            return speakserver
        else:
            return(DEF_SERVER)
    else:
        return(DEF_SERVER)