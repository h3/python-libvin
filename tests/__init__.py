# Sorted alphabetically by VIN
TEST_DATA = [
    # http://www.vindecoder.net/?vin=137ZA903X1E412677&submit=Decode unchecked
    {'VIN': '137ZA903X1E412677', 'WMI': '137', 'VDS': 'ZA903X', 'VIS': '1E412677',
     'MODEL': 'H1', 'MAKE':  'Hummer', 'YEAR': 2001, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '412677', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1C4RJEAG2EC476429&submit=Decode
    {'VIN': '1C4RJEAG2EC476429', 'WMI': '1C4', 'VDS': 'RJEAG2', 'VIS': 'EC476429',
     'MODEL': 'Grand Cherokee', 'MAKE':  'Jeep', 'YEAR': 2014, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '476429', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1D7RB1CT1BS488952&submit=Decode
    {'VIN': '1D7RB1CT1BS488952', 'WMI': '1D7', 'VDS': 'RB1CT1', 'VIS': 'BS488952',
     'MODEL': 'Ram 1500', 'MAKE':  'Dodge', 'YEAR': 2011, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '488952', 'FEWER_THAN_500_PER_YEAR': False},

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

    # http://www.vin-decoder.org/details?vin=3C3CFFCR9FT528063
    # http://www.fiat500usa.com/2013/08/decoding-fiat-500-vin.html
    # Chrysler Passenger Car Vehicle Identification Number Code Guide
    # ftp://ftp.nhtsa.dot.gov/MfrMail/ORG9653.pdf
    {'VIN': '3C3CFFCR9FT528063', 'WMI': '3C3', 'VDS': 'CFFCR9', 'VIS': 'FT528063',
     'MODEL': '500', 'MAKE':  'Fiat', 'YEAR': 2015, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '528063', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=3C6JD7CT4CG104778&submit=Decode
    # ftp://safercar.gov/MfrMail/ORG7565.pdf
    {'VIN': '3C6JD7CT4CG104778', 'WMI': '3C6', 'VDS': 'JD7CT4', 'VIS': 'CG104778',
     'MODEL': 'Ram 1500 Pickup', 'MAKE':  'Dodge', 'YEAR': 2012, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '104778', 'FEWER_THAN_500_PER_YEAR': False},

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

    # http://www.vindecoder.net/?vin=3GYVKMEF5AG416315&submit=Decode
    {'VIN': '3GYVKMEF5AG416315', 'WMI': '3GY', 'VDS': 'VKMEF5', 'VIS': 'AG416315',
     'MODEL': 'Escalade', 'MAKE':  'Cadillac', 'YEAR': 2010, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '416315', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=3LNHL2GC1BR262548&submit=Decode
    {'VIN': '3LNHL2GC1BR262548', 'WMI': '3LN', 'VDS': 'HL2GC1', 'VIS': 'BR262548',
     'MODEL': 'MKZ', 'MAKE':  'Lincoln', 'YEAR': 2011, 'COUNTRY': 'Mexico',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '262548', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5GADS13S072592644&submit=Decode
    # https://service.gm.com/dealerworld/vincards/
    # https://service.gm.com/dealerworld/vincards/pdf/vincard07.pdf
    # ftp://www-nrd.nhtsa.dot.gov/MfrMail/ORG5807.pdf
    {'VIN': '5GADS13S072592644', 'WMI': '5GA', 'VDS': 'DS13S0', 'VIS': '72592644',
     'MODEL': 'Ranier', 'MAKE':  'Buick', 'YEAR': 2007, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '592644', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5J6TF1H33CL339137&submit=Decode
    {'VIN': '5J6TF1H33CL339137', 'WMI': '5J6', 'VDS': 'TF1H33', 'VIS': 'CL339137',
     'MODEL': 'Crosstour', 'MAKE':  'Honda', 'YEAR': 2012, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '339137', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5J8TB1H27CA348655&submit=Decode
    {'VIN': '5J8TB1H27CA348655', 'WMI': '5J8', 'VDS': 'TB1H27', 'VIS': 'CA348655',
     'MODEL': 'RDX', 'MAKE':  'Acura', 'YEAR': 2012, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '348655', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5UMDU93436L421092&submit=Decode
    {'VIN': '5UMDU93436L421092', 'WMI': '5UM', 'VDS': 'DU9343', 'VIS': '6L421092',
     'MODEL': 'M', 'MAKE':  'BMW', 'YEAR': 2006, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '421092', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=5UXXW5C54F0791433&submit=Decode
    # http://www.partesymas.com/VIN-Interpretation-Tables-2026.pdf showed 4-7 were the model,body,engine code
    # http://www.autoredbook.com/ distinguished between the two X4 models
    {'VIN': '5UXXW5C54F0791433', 'WMI': '5UX', 'VDS': 'XW5C54', 'VIS': 'F0791433',
     'MODEL': 'X4 xDrive35i', 'MAKE':  'BMW', 'YEAR': 2015, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '791433', 'FEWER_THAN_500_PER_YEAR': False},

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

    # http://www.vindecoder.net/?vin=YV1902FH5D1796335&submit=Decode doesn't have model
    # http://www.vindecoderz.com/EN/check-lookup/YV1902FH5D1796335
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2013&make=Volvo confirms XC60
    {'VIN': 'YV1902FH5D1796335', 'WMI': 'YV1', 'VDS': '902FH5', 'VIS': 'D1796335',
     'MODEL': 'XC60', 'MAKE':  'Volvo', 'YEAR': 2013, 'COUNTRY': 'Sweden',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '796335', 'FEWER_THAN_500_PER_YEAR': False},

]
