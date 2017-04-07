# Main running program that calls a retreives the results of all functions.

# IMPORTS
import sys
from doublespeak.miniplenty import *
from doublespeak.minitrue import *
#IMPORTS


def main():

    if len(sys.argv) >  1:
        search_arg = sys.argv[1]
        print('''doublespeak, the documentation client for people:/ Usage: doublespeak: <search term>''')
    else:
        if (sys.argv[1].encode('utf-8') == '?' or sys.argv[1].encode('utf-8') == 'help'):
            print('''doublespeak, the documentation client for people:/ Usage: doublespeak: <search term>''')
        else:
             searchlight(hashcat(sys.argv[1].encode('utf-8')))
             print (hashcat(sys.argv[1].encode('utf-8')))
main()



