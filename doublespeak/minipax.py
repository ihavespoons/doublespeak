# Manages and updates all configurations as required.
from configparser import ConfigParser

def configcreator():
    config = ConfigParser()
    config.read('config.ini')
    config.add_section('main')
    config.set('main', 'server', 'https://doublespeak.io/api/us/')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def configupdater(section,key,changes):
    config = ConfigParser()
    config.read('config.ini')
    config.set(section,key,changes)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)