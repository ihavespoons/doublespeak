# Collection of universal utilities libraries

# IMPORTS
import hashlib
# IMPORTS


def hashcat(filament):
    hash_sha1 = hashlib.sha1(filament.encode('utf-8'))
    hash_result = hash_sha1.hexdigest()
    return hash_result