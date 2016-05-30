# -*- coding: utf-8 -*-
from nose.tools import assert_equals, assert_true, raises

from libvin.decoding import Vin
from libvin.static import *

from . import TEST_DATA


class TestDecode(object):

    def test_country(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.country, test['COUNTRY'])

    def test_is_pre_2010(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            if test['YEAR'] < 2010:
                assert_true(v.is_pre_2010)
            else:
                assert_true(not v.is_pre_2010)

    def test_less_than_500_per_year(self): # no tests yet..
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.less_than_500_built_per_year, test['FEWER_THAN_500_PER_YEAR'])

    def test_make(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s, %s" % (test['VIN'], v.make)
            assert_equals(v.make, test['MAKE'])

    def test_region(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.region, test['REGION'])

    def test_vis(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.vis, test['VIS'])

    def test_vds(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.vds, test['VDS'])

    def test_vsn(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.vsn, test['SEQUENTIAL_NUMBER'])

    def test_wmi(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.wmi, test['WMI'])

    def test_year(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s - %s" % (test['VIN'], v.year)
            assert_equals(v.year, test['YEAR'])

    def test_is_valid(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print "Testing: %s" % test['VIN']
            assert_equals(v.is_valid, True)
