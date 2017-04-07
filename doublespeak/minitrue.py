# Gets search results from online db and provides it back to display module

import sys
import urllib
import hashlib


def hasher():
    # Take cli input
    search_arg = sys.argv[1]
    # Encode Cli input into
    hash_sha1 = hashlib.sha1(search_arg.encode('utf-8'))
    hash_result = hash_sha1.hexdigest()
    return hash_result

def searchlight(hashresult):
    # takes a hash of the search and transmits it to the search api



