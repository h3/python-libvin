"""
Copyright Maxime Haineault
VIN Vehicle information number checker,

There are at least four competing standards used to calculate VIN.

 * FMVSS 115, Part 565: Used in United States and Canada
 * ISO Standard 3779: Used in Europe and many other parts of the world
 * SAE J853: Very similar to the ISO standard
 * ADR 61/2: used in Australia, referring back to ISO 3779 and 3780


ISO 3779
--------
 
    1 2 3 | 4 5 6 7 8 9 | 10 11 12 13 14 15 16 17
    -----   -----------   -----------------------
    |       |             |
    |       |             Vehicle Identifier Section
    |       |
    |       Vehicle Descriptor Section
    |
    World Manufacturer Idendified


European Union & North America (>500 vehicles/year)
---------------------------------------------------
 
    1 2 3 | 4 5 6 7 8 | 9 | 10 | 11 | 12 13 14 15 16 17
    -----   ---------   -   --   --   -----------------
    |       |           |   |    |    |
    |       |           |   |    |    Sequential Number
    |       |           |   |    |
    |       |           |   |    Plant Code
    |       |           |   |
    |       |           |   Model Year
    |       |           |
    |       |           Check Digit
    |       |
    |       Vehicle Attributes
    |
    World Manufacturer Idendified


European Union & North America (<500 vehicles/year)
---------------------------------------------------
 
    1 2 3 | 4 5 6 7 8 | 9 | 10 | 11 | 12 13 14 | 15 16 17
    -----   ---------   -   --   --   --------   --------
    |       |           |   |    |    |          |
    |       |           |   |    |    |          Sequential Number
    |       |           |   |    |    |
    |       |           |   |    |    Manufacturer Identifier
    |       |           |   |    |
    |       |           |   |    Plant Code
    |       |           |   |
    |       |           |   Model Year
    |       |           |
    |       |           Check Digit
    |       |
    |       Vehicle Attributes
    |
    World Manufacturer Idendified

"""

WORLD_MANUFACTURER_REGIONS = {
    'africa': 'ABCDEFGH',
    'asia': 'JKLMNPR',
    'north_america': '12345',
    'south_america': '89',
    'oceania': '67',
}

class Vin(object):
    def __init__(self, vin):
        self.vin = vin

    @property
    def region(self):
        for region in WORLD_MANUFACTURER_REGIONS:
            codes = WORLD_MANUFACTURER_REGIONS[region]
            if self.vin[0] in codes:
                return region
        return None
        

    @property
    def less_than_500_built_per_year(self):
        """
        A manufacturer who builds fewer than 500 vehicles 
        per year uses a 9 as the third digit
        """
        try:
            return int(self.vin[2]) is 9
        except ValueError:
            return False

    def decode(self):
        return self.vin


def decode(vin):
    v = Vin(vin)
    return v.decode()
