# -*- coding: utf-8 -*-
from nose.tools import assert_equals, raises

from libvin.decoding import Vin

"""
Test data

JM1BL1SF3A1267720   2010 Mazda 3
2A4GM684X6R632476   2006 Chrysler Pacifica
2B3KA43G27H825762   2007 Dodge Charger
1FAHP3FN8AW139719   2010 Ford Focus
1GKEV13728J123735   2008 GMC Acadia

"""


TEST_DATA = [
    # http://www.vindecoder.net/?vin=JM1BL1SF3A1267720&submit=Decode
    {'VIN': 'JM1BL1SF3A1267720',
     'WMI': 'JM1',
     'VDS': 'BL1SF3',
     'VIS': 'A1267720',
     'MODEL': 'MAZDA3',
     'MAKE':  'Mazda',
     'YEAR': 2010,
     'COUNTRY': 'Japan',
     'REGION': 'asia',
     'SEQUANTIAL_NUMBER': 267720,
     'FEWER_THAN_500_PER_YEAR': False},
    # http://www.vindecoder.net/?vin=2A4GM684X6R632476&submit=Decode
    {'VIN': '2A4GM684X6R632476',
     'WMI': '2A4',
     'VDS': 'GM684X',
     'VIS': '6R632476',
     'MODEL': 'Pacifica',
     'MAKE':  'Chrysler',
     'YEAR': 2006,
     'COUNTRY': 'Canada',
     'REGION': 'north_america',
     'SEQUANTIAL_NUMBER': 632476,
     'FEWER_THAN_500_PER_YEAR': False}
]


class TestDecode(object):

    def test_less_than_500_per_year(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.less_than_500_built_per_year, test['FEWER_THAN_500_PER_YEAR'])

    def test_region(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.region, test['REGION'])

    def test_vds(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.vds, test['VDS'])

    def test_year(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.year, test['YEAR'])
