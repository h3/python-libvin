"""
libvin - VIN Vehicle information number checker
(c) Copyright 2012 Maxime Haineault <max@motion-m.ca>
"""

from libvin.static import *


class Vin(object):
    def __init__(self, vin):
        self.vin = vin

    @property
    def country(self):
        """
        Returns the World Manufacturer's Country.
        """
        countries = WORLD_MANUFACTURER_MAP[self.vin[0]]['countries']

        for codes in countries:
            if self.vin[0] in codes:
                return countries[codes]

        return 'Unknown'

    def decode(self):
        return self.vin

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
        return self.vin[6].isdigit()

    def is_valid(self):
        try:
            self.region
        except e:
            print e

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

    @property
    def region(self):
        """
        Returns the World Manufacturer's Region. Possible results:
        """
        return WORLD_MANUFACTURER_MAP[self.vin[0]]['region']

    @property
    def vis(self):
        """
        Returns the Vehicle Idendifier Sequence (ISO 3779)
        Model Year, Manufacturer Plant and/or Serial Number
        """
        return self.vin[-8:]

    @property
    def vds(self):
        """
        Returns the Vehicle Descriptor Section (ISO 3779)
        Assigned by Manufacturer; Check Digit is Calculated
        """
        return self.vin[3:9]

    @property
    def vsn(self):
        """
        Returns the Vehicle Sequential Number
        """
        if self.less_than_500_built_per_year:
            return self.vin[-3:]
        else:
            return self.vin[-6:]

    @property
    def wmi(self):
        """
        Returns the World Manufacturer Identifier (any standards)
        Assigned by SAE
        """
        return self.vin[0:3]

    @property
    def year(self):
        """
        Returns the model year of the vehicle
        """
        if self.is_pre_2010:
            return YEARS_CODES_PRE_2010[self.vin[9]]
        else:
            print self.vin[9]
            return YEARS_CODES_PRE_2040[self.vin[9]]


def decode(vin):
    v = Vin(vin)
    return v.decode()
