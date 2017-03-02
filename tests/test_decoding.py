# -*- coding: utf-8 -*-
from nose.tools import assert_equals, assert_true, raises

from libvin.decoding import Vin
from libvin.static import *

from . import TEST_DATA

# To run tests that depend on network, do e.g. 'NETWORK_OK=1 nose2'
import os
if 'NETWORK_OK' in os.environ:
    from time import sleep
    from libvin.nhtsa import nhtsa_decode


class TestDecode(object):

    def test_country(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.country, test['COUNTRY'])

    def test_is_pre_2010(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            if test['YEAR'] < 2010:
                assert_true(v.is_pre_2010)
            else:
                assert_true(not v.is_pre_2010)

    def test_less_than_500_per_year(self): # no tests yet..
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.less_than_500_built_per_year, test['FEWER_THAN_500_PER_YEAR'])

    def test_make(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s, %s" % (test['VIN'], v.make))
            assert_equals(v.make, test['MAKE'])
            if 'NETWORK_OK' in os.environ:
                # Verify that our decoded make is the same as NHTSA's.
                n = nhtsa_decode(test['VIN'])
                if n['ErrorCode'][0] == '0':
                    assert_equals(v.make.upper(), n['Make'])
                # Avoid swamping nhtsa server when cache empty.
                # FIXME: Using requests_cache throttling would be better, wouldn't slow down cache full case.
                sleep(0.05)

    def test_region(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.region, test['REGION'])

    def test_vis(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.vis, test['VIS'])

    def test_vds(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.vds, test['VDS'])

    def test_vsn(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.vsn, test['SEQUENTIAL_NUMBER'])

    def test_wmi(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.wmi, test['WMI'])

    def test_year(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s - %s" % (test['VIN'], v.year))
            assert_equals(v.year, test['YEAR'])

    def test_is_valid(self):
        for test in TEST_DATA:
            v = Vin(test['VIN'])
            print("Testing: %s" % test['VIN'])
            assert_equals(v.is_valid, True)
