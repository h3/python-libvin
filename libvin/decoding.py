"""
libvin - VIN Vehicle information number checker
(c) Copyright 2012 Maxime Haineault <max@motion-m.ca>
"""

from libvin.static import *

class Vin(object):
    def __init__(self, vin):
        self.vin = vin.upper()

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

    @property
    def is_valid(self):
        """
        Returns True if a VIN is valid, otherwise returns False.
        """
        if len(self.vin) != 17:
            """
            For model years 1981 to present, the VIN is composed of 17 
            alphanumeric values
            """
            return False

        if any(x in 'IOQ' for x in self.vin):
            """ 
            The letters I,O, Q are prohibited from any VIN position 
            """
            return False

        if self.vin[9] in 'UZ0':
            """
            The tenth position of the VIN represents the Model Year and 
            does not permit the use of the characters U and Z, as well 
            as the numeric zero (0)
            """
            return False
        
        products = [VIN_WEIGHT[i] * VIN_TRANSLATION[j] for i, j in enumerate(self.vin)]
        check_digit = sum(products) % 11
        if check_digit == 10:
            check_digit = 'X'

        if self.vin[8] != str(check_digit):
            """
            The ninth position of the VIN is a calculated value based on 
            the other 16 alphanumeric values, it's called the 
            "Check Digit". The result of the check digit can ONLY be a 
            numeric 0-9 or letter "X".
            """
            return False

        return True

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
    def manufacturer(self):
        wmi = self.wmi
        if wmi[:3] in WMI_MAP:
            return WMI_MAP[wmi[:3]]
        if wmi[:2] in WMI_MAP:
            return WMI_MAP[wmi[:2]]
        return 'Unknown'

    @property
    def make(self):
        '''
        This is like manufacturer, but without country or other suffixes, and should be short common name.
        Should be same as values from e.g. http://www.fueleconomy.gov/ws/rest/vehicle/menu/make?year=2012
        Should probably have a static table instead of doing late fixup like this.
        '''
        man = self.manufacturer
        for suffix in ['Mexico', 'USA', 'USA - trucks', 'Canada', 'Turkey', 'Motor Company']:
            if man.endswith(suffix):
                man = man.replace(" %s" % suffix, "")
        if man == "General Motors":
            return "GMC"
        return man

    @property
    def year(self):
        """
        Returns the model year of the vehicle
        """
        if self.is_pre_2010:
            return YEARS_CODES_PRE_2010[self.vin[9]]
        else:
            return YEARS_CODES_PRE_2040[self.vin[9]]


def decode(vin):
    v = Vin(vin)
    return v.decode()
