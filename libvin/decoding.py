"""
Copyright Maxime Haineault
VIN Vehicle information number checker,

Reference: http://en.wikipedia.org/wiki/Vehicle_Identification_Number

There are at least four competing standards used to calculate VIN.

 * FMVSS 115, Part 565: Used in United States and Canada
 * ISO Standard 3779: Used in Europe and many other parts of the world
 * SAE J853: Very similar to the ISO standard
 * ADR 61/2: used in Australia, referring back to ISO 3779 and 3780


ISO 3779
========
 
    1 2 3 | 4 5 6 7 8 9 | 10 11 12 13 14 15 16 17
    -----   -----------   -----------------------
    |       |             |
    |       |             Vehicle Identifier Section
    |       |
    |       Vehicle Descriptor Section
    |
    World Manufacturer Idendified


European Union & North America (>500 vehicles/year)
===================================================
 
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
===================================================
 
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

YEARS_CODES_PRE_2010 = {
    'A': 1980, 'L': 1990, 'Y': 2000,
    'B': 1981, 'M': 1991, '1': 2001,
    'C': 1982, 'N': 1992, '2': 2002,
    'D': 1983, 'P': 1993, '3': 2003,
    'E': 1984, 'R': 1994, '4': 2004,
    'F': 1985, 'S': 1995, '5': 2005,
    'G': 1986, 'T': 1996, '6': 2006,
    'H': 1987, 'V': 1997, '7': 2007,
    'J': 1988, 'W': 1998, '8': 2008,
    'K': 1989, 'X': 1999, '9': 2009,
}

YEARS_CODES_PRE_2040 = {
    'A': 2010,	'L': 2020, 'Y': 2030,
    'B': 2011,	'M': 2021, '1': 2031,
    'C': 2012,	'N': 2022, '2': 2032,
    'D': 2013,	'P': 2023, '3': 2033,
    'E': 2014,	'R': 2024, '4': 2034,
    'F': 2015,	'S': 2025, '5': 2035,
    'G': 2016,	'T': 2026, '6': 2036,
    'H': 2017,	'V': 2027, '7': 2037,
    'J': 2018,	'W': 2028, '8': 2038,
    'K': 2019,	'X': 2029, '9': 2039,
}

class Vin(object):
    def __init__(self, vin):
        self.vin = vin

    @property
    def year(self):
        """
        Returns the model year of the vehicle
        """
        if self.is_pre_2010:
            return YEARS_CODES_PRE_2010[self.vin[9]]
        else:
            return YEARS_CODES_PRE_2040[self.vin[9]]

    @property
    def is_pre_2010(self):
        """
        Returns true if the model year is in the 1980-2009 range

        In order to identify exact year in passenger cars and multipurpose 
        passenger vehicles with a GVWR of 10,000 or less, one must read 
        position 7 as well as position 10. For passenger cars, and for 
        multipurpose passenger vehicles and trucks with a gross vehicle 
        weight rating of 10,000 lb (4,500 kg) or less, if position 7 is 
        numeric, the model year in position 10 of the VIN refers to a year 
        in the range 1980-2009. If position 7 is alphabetic, the model year 
        in position 10 of VIN refers to a year in the range 2010-2039.
        """
        return self.vin[7].isdigit()

    @property
    def wmi(self):
        """
        Returns the World Manufacturer Identifier
        """
        return self.vin[0:2]

    @property
    def vds(self):
        """
        Returns the Vehicle Descriptor Section
        """
        return self.vin[3:9]

    @property
    def region(self):
        """
        Returns the World Manufacturer's Region. Possible results:
          * africa
          * asia
          * north_america
          * south_america
          * oceania
        """
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
