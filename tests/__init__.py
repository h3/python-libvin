# To run tests that depend on network, do e.g. 'NETWORK_OK=1 nose2'
import os
if 'NETWORK_OK' in os.environ:
    import requests
    import requests_cache
    # Cache responses for 7 days to be kind to servers (and rerun quickly)
    requests_cache.install_cache('libvin_tests_cache', expire_after=7*24*60*60)

# Sorted alphabetically by VIN
TEST_DATA = [
    # http://www.vindecoder.net/?vin=137ZA903X1E412677&submit=Decode unchecked
    {'VIN': '137ZA903X1E412677', 'WMI': '137', 'VDS': 'ZA903X', 'VIS': '1E412677',
     'MODEL': 'H1', 'MAKE':  'Hummer', 'YEAR': 2001, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '412677', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.fueleconomy.gov/ws/rest/vehicle/37075
    {'VIN': '19XFC1F7XGE028370', 'WMI': '19X', 'VDS': 'FC1F7X', 'VIS': 'GE028370',
     'MODEL': 'Civic', 'MAKE': 'Honda', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '028370', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '37075', 'epa.co2TailpipeGpm': '252.0', 'epa.model' : 'Civic 4Dr', 'epa.trim' : 'Auto (variable gear ratios), 4 cyl, 1.5 L, Turbo',
    },

    # http://www.vindecoder.net/?vin=1C4RJEAG2EC476429&submit=Decode
    {'VIN': '1C4RJEAG2EC476429', 'WMI': '1C4', 'VDS': 'RJEAG2', 'VIS': 'EC476429',
     'MODEL': 'Grand Cherokee', 'MAKE':  'Jeep', 'YEAR': 2014, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '476429', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1D7RB1CP8BS798034&submit=Decode
    {'VIN': '1D7RB1CP8BS798034', 'WMI': '1D7', 'VDS': 'RB1CP8', 'VIS': 'BS798034',
     'MODEL': 'Ram 1500', 'MAKE':  'Dodge', 'YEAR': 2011, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '798034', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1D7RB1CT1BS488952&submit=Decode
    {'VIN': '1D7RB1CT1BS488952', 'WMI': '1D7', 'VDS': 'RB1CT1', 'VIS': 'BS488952',
     'MODEL': 'Ram 1500', 'MAKE':  'Dodge', 'YEAR': 2011, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '488952', 'FEWER_THAN_500_PER_YEAR': False},

    # Breadcrumbs for how libvin/epa.py looks up the epa results:
    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/1GB0C4EGXGZ280783
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2016&make=Chevrolet
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year=2016&make=Chevrolet&model=Silverado%20C15%202WD
    # There is ambiguity, so all possibly matching epa variants for this epa model are listed:
    # http://www.fueleconomy.gov/ws/rest/vehicle/37007
    ## http://www.fueleconomy.gov/ws/rest/vehicle/37006
    ## http://www.fueleconomy.gov/ws/rest/vehicle/37008
    {'VIN': '1GB0C4EGXGZ280783', 'WMI': '1GB', 'VDS': '0C4EGX', 'VIS': 'GZ280783',
     'MODEL': 'Silverado', 'MAKE': 'Chevrolet', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '280783', 'FEWER_THAN_500_PER_YEAR': False,
     'nhtsa.trim': '', 'nhtsa.series': '',
     'epa.id' : '37007', 'epa.co2TailpipeGpm': '493.0', 'epa.model' : 'Silverado C15 2WD', 'epa.trim' : 'Auto 8-spd, 8 cyl, 5.3 L, SIDI',
     #'epa.id' : '37006', 'epa.co2TailpipeGpm': '480.0', 'epa.model' : 'Silverado C15 2WD', 'epa.trim' : 'Auto 6-spd, 8 cyl, 5.3 L, SIDI',
     #'epa.id' : '37008', 'epa.co2TailpipeGpm': '527.0', 'epa.model' : 'Silverado C15 2WD', 'epa.trim' : 'Auto 8-spd, 8 cyl, 6.2 L, SIDI',
    },

    # http://www.fueleconomy.gov/ws/rest/vehicle/36354
    {'VIN': '1GNKRHKD2GJ223195', 'WMI': '1GN', 'VDS': 'KRHKD2', 'VIS': 'GJ223195',
     'MODEL': 'Traverse AWD', 'MAKE': 'Chevrolet', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '223195', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '36354', 'epa.co2TailpipeGpm': '519.0', 'epa.model' : 'Traverse AWD', 'epa.trim' : 'Auto 6-spd, 6 cyl, 3.6 L',
    },

    # http://www.vindecoder.net/?vin=19UUA65694A043249&submit=Decode
    # http://acurazine.com/forums/vindecoder.php?vin=19UUA65694A043249
    {'VIN': '19UUA65694A043249', 'WMI': '19U', 'VDS': 'UA6569', 'VIS': '4A043249',
     'MODEL': 'TL', 'MAKE':  'Acura', 'YEAR': 2004, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '043249', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=19XFB4F24DE547421&submit=Decode says unknown
    # http://www.civicx.com/threads/2016-civic-vin-translator-decoder-guide.889/
    {'VIN': '19XFB4F24DE547421', 'WMI': '19X', 'VDS': 'FB4F24', 'VIS': 'DE547421',
     'MODEL': 'Civic Hybrid', 'MAKE':  'Honda', 'YEAR': 2013, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '547421', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1FAHP3FN8AW139719&submit=Decode
    {'VIN': '1FAHP3FN8AW139719', 'WMI': '1FA', 'VDS': 'HP3FN8', 'VIS': 'AW139719',
     'MODEL': 'Focus', 'MAKE':  'Ford', 'YEAR': 2010, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '139719', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1GKEV13728J123735&submit=Decode
    {'VIN': '1GKEV13728J123735', 'WMI': '1GK', 'VDS': 'EV1372', 'VIS': '8J123735',
     'MODEL': 'Acadia', 'MAKE':  'GMC', 'YEAR': 2008, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '123735', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1GT020CG4EF828544&submit=Decode
    {'VIN': '1GT020CG4EF828544', 'WMI': '1GT', 'VDS': '020CG4', 'VIS': 'EF828544',
     'MODEL': 'Sierra 2500', 'MAKE':  'GMC', 'YEAR': 2014, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '828544', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1GYFC56299R410242&submit=Decode didn't have model
    # http://www.vindecoderz.com/EN/check-lookup/1GYFC56299R410242
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2009&make=Cadillac confirms Escalade ESV
    {'VIN': '1GYFC56299R410242', 'WMI': '1GY', 'VDS': 'FC5629', 'VIS': '9R410242',
     'MODEL': 'Escalade ESV', 'MAKE':  'Cadillac', 'YEAR': 2009, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '410242', 'FEWER_THAN_500_PER_YEAR': False},

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/1YVHZ8DH0C5M33844
    {'VIN': '1YVHZ8DH0C5M33844', 'WMI': '1YV', 'VDS': 'HZ8DH0', 'VIS': 'C5M33844',
     'MODEL': 'Mazda6', 'MAKE': 'Mazda', 'YEAR': 2012, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': 'M33844', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/1ZVBP8CF4E5242560
    {'VIN': '1ZVBP8CF4E5242560', 'WMI': '1ZV', 'VDS': 'BP8CF4', 'VIS': 'E5242560',
     'MODEL': 'Mustang', 'MAKE': 'Ford', 'YEAR': 2014, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '242560', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.vindecoder.net/?vin=19VDE2E5XEE644230&submit=Decode unchecked
    # http://acurazine.com/forums/vindecoder.php?vin=19VDE2E5XEE644230
    {'VIN': '19VDE2E5XEE644230', 'WMI': '19V', 'VDS': 'DE2E5X', 'VIS': 'EE644230',
     'MODEL': 'ILX', 'MAKE':  'Acura', 'YEAR': 2014, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '644230', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2A4GM684X6R632476&submit=Decode
    {'VIN': '2A4GM684X6R632476', 'WMI': '2A4', 'VDS': 'GM684X', 'VIS': '6R632476',
     'MODEL': 'Pacifica', 'MAKE':  'Chrysler', 'YEAR': 2006, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '632476', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2B3KA43G27H825762&submit=Decode
    {'VIN': '2B3KA43G27H825762', 'WMI': '2B3', 'VDS': 'KA43G2', 'VIS': '7H825762',
     'MODEL': 'Charger', 'MAKE':  'Dodge', 'YEAR': 2007, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '825762', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2C3CDYAGXDH825982&submit=Decode doesn't have good info
    # http://dodgeforum.com/forum/vindecoder.php?vin=2C3CDYAGXDH825982
    {'VIN': '2C3CDYAGXDH825982', 'WMI': '2C3', 'VDS': 'CDYAGX', 'VIS': 'DH825982',
     'MODEL': 'Challenger', 'MAKE':  'Dodge', 'YEAR': 2013, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '825982', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2C4RDGBG4FR987134&submit=Decode
    {'VIN': '2C4RDGBG4FR987134', 'WMI': '2C4', 'VDS': 'RDGBG4', 'VIS': 'FR987134',
     'MODEL': 'Grand Caravan', 'MAKE':  'Dodge', 'YEAR': 2015, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '987134', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2D4RN6DX5AR939562&submit=Decode
    {'VIN': '2D4RN6DX5AR939562', 'WMI': '2D4', 'VDS': 'RN6DX5', 'VIS': 'AR939562',
     'MODEL': 'Grand Caravan', 'MAKE':  'Dodge', 'YEAR': 2010, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '939562', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2FTCF15F2ECA55516&submit=Decode
    {'VIN': '2FTCF15F2ECA55516', 'WMI': '2FT', 'VDS': 'CF15F2', 'VIS': 'ECA55516',
     'MODEL': 'F-150', 'MAKE':  'Ford', 'YEAR': 1984, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': 'A55516', 'FEWER_THAN_500_PER_YEAR': False},

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/2GCEC13C981202392
    {'VIN': '2GCEC13C981202392', 'WMI': '2GC', 'VDS': 'EC13C9', 'VIS': '81202392',
     'MODEL': 'Silverado', 'MAKE': 'Chevrolet', 'YEAR': 2008, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '202392', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/2GNFLPE55C6105926
    {'VIN': '2GNFLPE55C6105926', 'WMI': '2GN', 'VDS': 'FLPE55', 'VIS': 'C6105926',
     'MODEL': 'Equinox', 'MAKE': 'Chevrolet', 'YEAR': 2012, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '105926', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.vindecoder.net/?vin=2G61W5S83E9422251&submit=Decode
    # ftp://safercar.gov/MfrMail/ORG7595.pdf "General Motors LLC 2013 Vehicle Identification Numbering Standard"
    {'VIN': '2G61W5S83E9422251', 'WMI': '2G6', 'VDS': '1W5S83', 'VIS': 'E9422251',
     'MODEL': 'XTS', 'MAKE':  'Cadillac', 'YEAR': 2014, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '422251', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2HNYD18975H033218&submit=Decode
    # http://acurazine.com/forums/vindecoder.php?vin=2HNYD18975H033218
    {'VIN': '2HNYD18975H033218', 'WMI': '2HN', 'VDS': 'YD1897', 'VIS': '5H033218',
     'MODEL': 'MDX', 'MAKE':  'Acura', 'YEAR': 2005, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '033218', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2LMHJ5AT9CB565906&submit=Decode
    {'VIN': '2LMHJ5AT9CB565906', 'WMI': '2LM', 'VDS': 'HJ5AT9', 'VIS': 'CB565906',
     'MODEL': 'MKT', 'MAKE':  'Lincoln', 'YEAR': 2012, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '565906', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.toyodiy.com/parts/q?vin=2t1kr32e26c557497 says ATM 4-SPEED FLOOR SHIFT (how's it know?)
    # http://www.fueleconomy.gov/ws/rest/vehicle/22123
    {'VIN': '2T1KR32E16C583752', 'WMI': '2T1', 'VDS': 'KR32E1', 'VIS': '6C583752',
     'MODEL': 'Matrix', 'MAKE': 'Toyota', 'YEAR': 2006, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '583752', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '22123', 'epa.co2TailpipeGpm': '329.1', 'epa.model' : 'Matrix', 'epa.trim' : 'Auto 4-spd, 4 cyl, 1.8 L',
    },

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/2T2BGMCA0GC004299
    {'VIN': '2T2BGMCA0GC004299', 'WMI': '2T2', 'VDS': 'BGMCA0', 'VIS': 'GC004299',
     'MODEL': 'RX', 'MAKE': 'Lexus', 'YEAR': 2016, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '004299', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.vin-decoder.org/details?vin=3C3CFFCR9FT528063
    # http://www.fiat500usa.com/2013/08/decoding-fiat-500-vin.html
    # Chrysler Passenger Car Vehicle Identification Number Code Guide
    # ftp://ftp.nhtsa.dot.gov/MfrMail/ORG9653.pdf
    {'VIN': '3C3CFFCR9FT528063', 'WMI': '3C3', 'VDS': 'CFFCR9', 'VIS': 'FT528063',
     'MODEL': '500', 'MAKE':  'Fiat', 'YEAR': 2015, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '528063', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.fueleconomy.gov/ws/rest/vehicle/34122
    {'VIN': '3C4PDCBG3ET296933', 'WMI': '3C4', 'VDS': 'PDCBG3', 'VIS': 'ET296933',
     'MODEL': 'Journey', 'MAKE': 'Dodge', 'YEAR': 2014, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '296933', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '34122', 'epa.co2TailpipeGpm': '456.0', 'epa.model' : 'Journey FWD', 'epa.trim' : 'Auto 6-spd, 6 cyl, 3.6 L',
    },

    # http://www.vindecoder.net/?vin=3C6JD7CT4CG104778&submit=Decode
    # ftp://safercar.gov/MfrMail/ORG7565.pdf
    {'VIN': '3C6JD7CT4CG104778', 'WMI': '3C6', 'VDS': 'JD7CT4', 'VIS': 'CG104778',
     'MODEL': 'Ram 1500 Pickup', 'MAKE':  'Dodge', 'YEAR': 2012, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '104778', 'FEWER_THAN_500_PER_YEAR': False},

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/3CZRU5H35GM739695
    # http://www.fueleconomy.gov/ws/rest/vehicle/35999
    {'VIN': '3CZRU5H35GM739695', 'WMI': '3CZ', 'VDS': 'RU5H35', 'VIS': 'GM739695',
     'MODEL': 'HR-V', 'MAKE': 'Honda', 'YEAR': 2016, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '739695', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '35999', 'epa.co2TailpipeGpm': '285.0', 'epa.model' : 'HR-V 2WD', 'epa.trim' : 'Auto (variable gear ratios), 4 cyl, 1.8 L',
    },

    # http://www.vindecoder.net/?vin=3D4PH6FV5AT152960&submit=Decode
    # http://www.rambodybuilder.com/2010/docs/intro/vin.pdf
    {'VIN': '3D4PH6FV5AT152960', 'WMI': '3D4', 'VDS': 'PH6FV5', 'VIS': 'AT152960',
     'MODEL': 'Journey', 'MAKE':  'Dodge', 'YEAR': 2010, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '152960', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=3D4PH7FG1BT808130&submit=Decode
    {'VIN': '3D4PH7FG1BT808130', 'WMI': '3D4', 'VDS': 'PH7FG1', 'VIS': 'BT808130',
     'MODEL': 'Journey', 'MAKE':  'Dodge', 'YEAR': 2011, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '808130', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=3D73Y3CL0BG113805&submit=Decode
    # Edmunds has this as Dodge up to 2010, RAM thereafter,
    # but EPA confused; https://www.fueleconomy.gov/feg/EPAGreenGuide/txt/all_alpha_11.txt has it as Dodge still
    # ftp://safercar.gov/MfrMail/ORG7565.pdf bit confused too
    # ftp://safercar.gov/MfrMail/ORG5870.pdf is for 2011, but calls it Dodge still
    # Heck, http://www.rambodybuilder.com/2012/docs/intro/vin.pdf is 2012, and still calls it Dodge
    # Screw it, let's go with Dodge, as I have no way of getting this right
    {'VIN': '3D73Y3CL0BG113805', 'WMI': '3D7', 'VDS': '3Y3CL0', 'VIS': 'BG113805',
     'MODEL': 'Ram 3500', 'MAKE':  'Dodge', 'YEAR': 2011, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '113805', 'FEWER_THAN_500_PER_YEAR': False},

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/3GCEC13078G157479
    {'VIN': '3GCEC13078G157479', 'WMI': '3GC', 'VDS': 'EC1307', 'VIS': '8G157479',
     'MODEL': 'Silverado', 'MAKE': 'Chevrolet', 'YEAR': 2008, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '157479', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.fueleconomy.gov/ws/rest/vehicle/23047
    {'VIN': '3GNFK16387G115163', 'WMI': '3GN', 'VDS': 'FK1638', 'VIS': '7G115163',
     'MODEL': 'Suburban', 'MAKE':  'Chevrolet', 'YEAR': 2007, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '115163', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '23047', 'epa.co2TailpipeGpm': '555.4', 'epa.model' : 'Suburban 1500 4WD', 'epa.trim' : 'Auto 4-spd, 8 cyl, 5.3 L',
    },

    # http://www.vindecoder.net/?vin=3GYVKMEF5AG416315&submit=Decode
    {'VIN': '3GYVKMEF5AG416315', 'WMI': '3GY', 'VDS': 'VKMEF5', 'VIS': 'AG416315',
     'MODEL': 'Escalade', 'MAKE':  'Cadillac', 'YEAR': 2010, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '416315', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=3LNHL2GC1BR262548&submit=Decode
    {'VIN': '3LNHL2GC1BR262548', 'WMI': '3LN', 'VDS': 'HL2GC1', 'VIS': 'BR262548',
     'MODEL': 'MKZ', 'MAKE':  'Lincoln', 'YEAR': 2011, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '262548', 'FEWER_THAN_500_PER_YEAR': False},

    # Can't tell transmission from vin, so pick one at random :-(
    # https://vpic.nhtsa.dot.gov/mid/home/displayfile/6089
    # http://www.fueleconomy.gov/ws/rest/vehicle/36534
    ## http://www.fueleconomy.gov/ws/rest/vehicle/36535
    {'VIN': '3MZBM1K72GM303265', 'WMI': '3MZ', 'VDS': 'BM1K72', 'VIS': 'GM303265',
     'MODEL': 'Mazda3', 'MAKE': 'Mazda', 'YEAR': 2016, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '303265', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '36534', 'epa.co2TailpipeGpm': '269.0', 'epa.model' : '3 5-Door', 'epa.trim' : 'Man 6-spd, 4 cyl, 2.0 L, SIDI',
     #'epa.id' : '36535', 'epa.co2TailpipeGpm': '265.0', 'epa.model' : '3 5-Door', 'epa.trim' : 'Auto (S6), 4 cyl, 2.0 L, SIDI',
    },

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/3TMCZ5AN2GM040551
    {'VIN': '3TMCZ5AN2GM040551', 'WMI': '3TM', 'VDS': 'CZ5AN2', 'VIS': 'GM040551',
     'MODEL': 'Tacoma', 'MAKE': 'Toyota', 'YEAR': 2016, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '040551', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.vindecoder.net/?vin=4A31K3DT4CE403200&submit=Decode
    {'VIN': '4A31K3DT4CE403200', 'WMI': '4A3', 'VDS': '1K3DT4', 'VIS': 'CE403200',
     'MODEL': 'Eclipse', 'MAKE':  'Mitsubishi', 'YEAR': 2012, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '403200', 'FEWER_THAN_500_PER_YEAR': False},

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/4JGDA6DB9GA764832
    {'VIN': '4JGDA6DB9GA764832', 'WMI': '4JG', 'VDS': 'DA6DB9', 'VIS': 'GA764832',
     'MODEL': 'GLE', 'MAKE': 'Mercedes-Benz', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '764832', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.fueleconomy.gov/ws/rest/vehicle/36406
    {'VIN': '4S3BNAH62G3049699', 'WMI': '4S3', 'VDS': 'BNAH62', 'VIS': 'G3049699',
     'MODEL': 'Legacy', 'MAKE': 'Subaru', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '049699', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '36406', 'epa.co2TailpipeGpm': '298.0', 'epa.model' : 'Legacy AWD', 'epa.trim' : 'Auto(AV-S6), 4 cyl, 2.5 L',
    },

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/55SWF4JB6GU104745
    {'VIN': '55SWF4JB6GU104745', 'WMI': '55S', 'VDS': 'WF4JB6', 'VIS': 'GU104745',
     'MODEL': 'C-Class', 'MAKE': 'Mercedes-Benz', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '104745', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/58ABK1GG4GU016219
    {'VIN': '58ABK1GG4GU016219', 'WMI': '58A', 'VDS': 'BK1GG4', 'VIS': 'GU016219',
     'MODEL': 'ES', 'MAKE': 'Lexus', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '016219', 'FEWER_THAN_500_PER_YEAR': False,
    },

    # http://www.vindecoder.net/?vin=5FRYD3H26GB020813&submit=Decode unchecked
    {'VIN': '5FRYD3H26GB020813', 'WMI': '5FR', 'VDS': 'YD3H26', 'VIS': 'GB020813',
     'MODEL': 'MDX', 'MAKE':  'Acura', 'YEAR': 2016, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '020813', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5GADS13S072592644&submit=Decode
    # https://service.gm.com/dealerworld/vincards/
    # https://service.gm.com/dealerworld/vincards/pdf/vincard07.pdf
    # ftp://www-nrd.nhtsa.dot.gov/MfrMail/ORG5807.pdf
    {'VIN': '5GADS13S072592644', 'WMI': '5GA', 'VDS': 'DS13S0', 'VIS': '72592644',
     'MODEL': 'Ranier', 'MAKE':  'Buick', 'YEAR': 2007, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '592644', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5GNRNGEE9A8215904&submit=Decode
    {'VIN': '5GNRNGEE9A8215904', 'WMI': '5GN', 'VDS': 'RNGEE9', 'VIS': 'A8215904',
     'MODEL': 'H3T', 'MAKE':  'Hummer', 'YEAR': 2010, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '215904', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5J6TF1H33CL339137&submit=Decode
    {'VIN': '5J6TF1H33CL339137', 'WMI': '5J6', 'VDS': 'TF1H33', 'VIS': 'CL339137',
     'MODEL': 'Crosstour', 'MAKE':  'Honda', 'YEAR': 2012, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '339137', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5J8TB1H27CA348655&submit=Decode
    {'VIN': '5J8TB1H27CA348655', 'WMI': '5J8', 'VDS': 'TB1H27', 'VIS': 'CA348655',
     'MODEL': 'RDX', 'MAKE':  'Acura', 'YEAR': 2012, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '348655', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5N1CR2MN6EC875492&submit=Decode
    {'VIN': '5N1CR2MN6EC875492', 'WMI': '5N1', 'VDS': 'CR2MN6', 'VIS': 'EC875492',
     'MODEL': 'Pathfinder', 'MAKE':  'Nissan', 'YEAR': 2014, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '875492', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5UMDU93436L421092&submit=Decode
    {'VIN': '5UMDU93436L421092', 'WMI': '5UM', 'VDS': 'DU9343', 'VIS': '6L421092',
     'MODEL': 'M', 'MAKE':  'BMW', 'YEAR': 2006, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '421092', 'FEWER_THAN_500_PER_YEAR': False},

    # https://vpic.nhtsa.dot.gov/mid/home/displayfile/6197 "BMW Model Year 2015 Decipherment of VINs in Accordance with Part 565"
    # http://www.vindecoder.net/?vin=5UXXW5C54F0791433&submit=Decode
    # http://www.partesymas.com/VIN-Interpretation-Tables-2026.pdf showed 4-7 were the model,body,engine code
    # http://www.autoredbook.com/ distinguished between the two X4 models
    {'VIN': '5UXXW5C54F0791433', 'WMI': '5UX', 'VDS': 'XW5C54', 'VIS': 'F0791433',
     'MODEL': 'X4 xDrive35i', 'MAKE':  'BMW', 'YEAR': 2015, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '791433', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.fueleconomy.gov/ws/rest/vehicle/34949
    {'VIN': '5XXGM4A7XFG459047', 'WMI': '5XX', 'VDS': 'GM4A7X', 'VIS': 'FG459047',
     'MODEL': 'Optima', 'MAKE': 'Kia', 'YEAR': 2015, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '459047', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '34949', 'epa.co2TailpipeGpm': '330.0', 'epa.model' : 'Optima', 'epa.trim' : 'Auto (S6), 4 cyl, 2.4 L',
    },

    # http://www.fueleconomy.gov/ws/rest/vehicle/35500
    {'VIN': '5YFBURHE9FP280940', 'WMI': '5YF', 'VDS': 'BURHE9', 'VIS': 'FP280940',
     'MODEL': 'Corolla', 'MAKE':  'Toyota', 'YEAR': 2015, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '280940', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '35500', 'epa.co2TailpipeGpm': '280.0', 'epa.model' : 'Corolla', 'epa.trim' : 'Man 6-spd, 4 cyl, 1.8 L',
    },

    # http://www.vindecoder.net/?vin=JA4AD2A3XEZ426420&submit=Decode didn't have model
    # https://www.mitsubishicars.com/owners/support/vin-information
    {'VIN': 'JA4AD2A3XEZ426420', 'WMI': 'JA4', 'VDS': 'AD2A3X', 'VIS': 'EZ426420',
     'MODEL': 'Outlander ES', 'MAKE':  'Mitsubishi', 'YEAR': 2014, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '426420', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JH4CW2H53BC567925&submit=Decode
    {'VIN': 'JH4CW2H53BC567925', 'WMI': 'JH4', 'VDS': 'CW2H53', 'VIS': 'BC567925',
     'MODEL': 'TSX', 'MAKE':  'Acura', 'YEAR': 2011, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '567925', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JN1CV6FE4EM164066&submit=Decode
    # http://infinitihelp.com/diy/common/infiniti_vin.php
    {'VIN': 'JN1CV6FE4EM164066', 'WMI': 'JN1', 'VDS': 'CV6FE4', 'VIS': 'EM164066',
     'MODEL': 'Q60 Convertible', 'MAKE':  'Infiniti', 'YEAR': 2014, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '164066', 'FEWER_THAN_500_PER_YEAR': False},

    # And another random JN1 that isn't Infiniti
    # http://nissanvindecoder.com/vins/jn1az44ex9m403788
    {'VIN': 'JN1AZ44EX9M403788', 'WMI': 'JN1', 'VDS': 'AZ44EX', 'VIS': '9M403788',
     'MODEL': '370Z', 'MAKE':  'Nissan', 'YEAR': 2009, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '403788', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JN8BS1MW7EM920252&submit=Decode
    {'VIN': 'JN8BS1MW7EM920252', 'WMI': 'JN8', 'VDS': 'BS1MW7', 'VIS': 'EM920252',
     'MODEL': 'QX70', 'MAKE':  'Infiniti', 'YEAR': 2014, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '920252', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JN8CS1MU0DM236239&submit=Decode
    {'VIN': 'JN8CS1MU0DM236239', 'WMI': 'JN8', 'VDS': 'CS1MU0', 'VIS': 'DM236239',
     'MODEL': 'FX37', 'MAKE':  'Infiniti', 'YEAR': 2013, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '236239', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JTHBW1GG7D2369737&submit=Decode has no model
    # http://www.autocalculator.org/VIN/WMI.aspx agrees JTH is Lexus
    # http://www.clublexus.com/forums/vindecoder.php?vin=JTHBW1GG7D2369737
    {'VIN': 'JTHBW1GG7D2369737', 'WMI': 'JTH', 'VDS': 'BW1GG7', 'VIS': 'D2369737',
     'MODEL': 'ES 300h', 'MAKE':  'Lexus', 'YEAR': 2013, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '369737', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JTJHY7AX4D4667505&submit=Decode
    {'VIN': 'JTJHY7AX4D4667505', 'WMI': 'JTJ', 'VDS': 'HY7AX4', 'VIS': 'D4667505',
     'MODEL': 'LX 570', 'MAKE':  'Lexus', 'YEAR': 2013, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '667505', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JM1BL1SF3A1267720&submit=Decode
    {'VIN': 'JM1BL1SF3A1267720', 'WMI': 'JM1', 'VDS': 'BL1SF3', 'VIS': 'A1267720',
     'MODEL': 'MAZDA3', 'MAKE':  'Mazda', 'YEAR': 2010, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '267720', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=KNDJT2A54D7883468&submit=Decode
    {'VIN': 'KNDJT2A54D7883468', 'WMI': 'KND', 'VDS': 'JT2A54', 'VIS': 'D7883468',
     'MODEL': 'Soul', 'MAKE':  'Kia', 'YEAR': 2013, 'COUNTRY': 'Korea (South)',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '883468', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.fueleconomy.gov/ws/rest/vehicle/36940
    {'VIN': 'KNMAT2MT0GP672329', 'WMI': 'KNM', 'VDS': 'AT2MT0', 'VIS': 'GP672329',
     'MODEL': 'Rogue', 'MAKE': 'Nissan', 'YEAR': 2016, 'COUNTRY': 'Korea (South)',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '672329', 'FEWER_THAN_500_PER_YEAR': False,
     'epa.id' : '36940', 'epa.co2TailpipeGpm': '318.0', 'epa.model' : 'Rogue FWD', 'epa.trim' : 'Auto (variable gear ratios), 4 cyl, 2.5 L',
    },

    # http://www.vindecoder.net/?vin=SCBEC9ZA1EC225243&submit=Decode
    # https://www.vinaudit.com/vin-search?vin=SCBEC9ZA1EC225243 got model slightly wrong
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2014&make=Bentley confirms model name
    {'VIN': 'SCBEC9ZA1EC225243', 'WMI': 'SCB', 'VDS': 'EC9ZA1', 'VIS': 'EC225243',
     'MODEL': 'Flying Spur', 'MAKE':  'Bentley', 'YEAR': 2014, 'COUNTRY': 'United Kingdom',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '225243', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=SCFAD01A65G199359&submit=Decode
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2005&make=Aston%20Martin verifies spelling
    {'VIN': 'SCFAD01A65G199359', 'WMI': 'SCF', 'VDS': 'AD01A6', 'VIS': '5G199359',
     'MODEL': 'DB9', 'MAKE':  'Aston Martin', 'YEAR': 2005, 'COUNTRY': 'United Kingdom',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '199359', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=TRUSC28N711268458&submit=Decode
    {'VIN': 'TRUSC28N711268458', 'WMI': 'TRU', 'VDS': 'SC28N7', 'VIS': '11268458',
     'MODEL': 'TT', 'MAKE':  'Audi', 'YEAR': 2001, 'COUNTRY': 'Hungary',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '268458', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=VNKJTUD36FA838549&submit=Decode
    {'VIN': 'VNKJTUD36FA838549', 'WMI': 'VNK', 'VDS': 'JTUD36', 'VIS': 'FA838549',
     'MODEL': 'Yaris', 'MAKE':  'Toyota', 'YEAR': 2015, 'COUNTRY': 'France',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '838549', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=W04GW5EV0B1603732&submit=Decode
    # http://gmvindecoder.net/vins/W04GW5EV0B1603732
    {'VIN': 'W04GW5EV0B1603732', 'WMI': 'W04', 'VDS': 'GW5EV0', 'VIS': 'B1603732',
     'MODEL': 'Regal', 'MAKE':  'Buick', 'YEAR': 2011, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '603732', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=WA1EY74LX9D205644&submit=Decode
    # https://vindecoder.eu/check-vin/WA1EY74LX9D205644
    {'VIN': 'WA1EY74LX9D205644', 'WMI': 'WA1', 'VDS': 'EY74LX', 'VIS': '9D205644',
     'MODEL': 'Q7', 'MAKE':  'Audi', 'YEAR': 2009, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '205644', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=WBSWL9C54AP786013&submit=Decode
    {'VIN': 'WBSWL9C54AP786013', 'WMI': 'WBS', 'VDS': 'WL9C54', 'VIS': 'AP786013',
     'MODEL': 'M3 Convertible', 'MAKE':  'BMW', 'YEAR': 2010, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '786013', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=WDCYC7DF3FX109287&submit=Decode
    # http://www.vindecoderz.com/EN/check-lookup/WDCYC7DF3FX109287
    # http://www.autocalculator.org/VIN/WMI.aspx says WDC is Mercedes-Benz, hmm
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/make?year=2015 spells it Mercedes-Benz, too, let's go with that
    {'VIN': 'WDCYC7DF3FX109287', 'WMI': 'WDC', 'VDS': 'YC7DF3', 'VIS': 'FX109287',
     'MODEL': 'G643', 'MAKE':  'Mercedes-Benz', 'YEAR': 2015, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '109287', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=WDDNG7BB4AA522219&submit=Decode
    # ftp://safercar.gov/MfrMail/ORG4488.pdf
    {'VIN': 'WDDNG7BB4AA522219', 'WMI': 'WDD', 'VDS': 'NG7BB4', 'VIS': 'AA522219',
     'MODEL': 'S550', 'MAKE':  'Mercedes-Benz', 'YEAR': 2010, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '522219', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=WUADUAFG6AN410499&submit=Decode
    {'VIN': 'WUADUAFG6AN410499', 'WMI': 'WUA', 'VDS': 'DUAFG6', 'VIS': 'AN410499',
     'MODEL': 'R8', 'MAKE':  'Audi', 'YEAR': 2010, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '410499', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=WVGAV7AX9BW549850&submit=Decode unchecked
    # http://acurazine.com/forums/vindecoder.php?vin=WVGAV7AX9BW549850
    {'VIN': 'WVGAV7AX9BW549850', 'WMI': 'WVG', 'VDS': 'AV7AX9', 'VIS': 'BW549850',
     'MODEL': 'Tiguan', 'MAKE':  'Volkswagen', 'YEAR': 2011, 'COUNTRY': 'Germany',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '549850', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=YV1902FH5D1796335&submit=Decode doesn't have model
    # http://www.vindecoderz.com/EN/check-lookup/YV1902FH5D1796335
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2013&make=Volvo confirms XC60
    {'VIN': 'YV1902FH5D1796335', 'WMI': 'YV1', 'VDS': '902FH5', 'VIS': 'D1796335',
     'MODEL': 'XC60', 'MAKE':  'Volvo', 'YEAR': 2013, 'COUNTRY': 'Sweden',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '796335', 'FEWER_THAN_500_PER_YEAR': False},

]
