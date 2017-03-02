"""
Fetch a VIN record from NHTSA
(c) Copyright 2016 Dan Kegel <dank@kegel.com>
License: AGPL v3.0
"""

# Note: client app may wish to 'import requests_cache' and install a cache
# to avoid duplicate fetches
import requests


def nhtsa_decode(vin):
    '''
    Return vpic.nhtsa.dot.gov's interpretation of the VIN in a dictionary, or None on error.

    ErrorCode member of dictionary is a string starting with '0'
    if NHTSA thinks it has good data for that vin.

    Fields set seem to depend on the manufacturer.
    Here's which fields seem to be set for a few makes:

    BodyClass, Make, Model, ModelYear, GVWR: all
    Doors: most
    EngineModel: Honda, Acura
    EngineCylinders: Dodge
    DisplacementCC: Infiniti, BMW, Dodge
    DriveType: Infiniti, Dodge, Mitsubishi
    Series: BMW, Dodge, Mitsubishi
    Trim: BMW, Dodge
    '''

    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/' + vin + '?format=json'
    try:
        r = requests.get(url)
    except requests.Timeout:
        print("nhtsa: connection timed out")
        return None
    except requests.ConnectionError:
        print("nhtsa: connection failed")
        return None
    try:
        jresult = r.json()
        results = jresult['Results'][0]
    except ValueError:
        print("nhtsa: could not parse result")
        return None

    # Strip trailing spaces (as in 'Hummer ')
    for key in results:
        results[key] = results[key].rstrip()

    return results
