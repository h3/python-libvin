# -*- coding: utf-8 -*-
from nose.tools import assert_equals, raises

from libvin.decoding import Vin
from libvin.static import *

from . import TEST_DATA


class TestDecode(object):

    def test_less_than_500_per_year(self): # no tests yet..
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.less_than_500_built_per_year, test['FEWER_THAN_500_PER_YEAR'])

    def test_region(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.region, test['REGION'])

    def test_country(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.country, test['COUNTRY'])

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
