WORLD_MANUFACTURER_REGIONS = {
    'africa': 'ABCDEFGH',
    'asia': 'JKLMNPR',
    'north_america': '12345',
    'south_america': '89',
    'oceania': '67',
}

WORLD_MANUFACTURER_MAP = {
    
    # AFRICA 

    'A': {'region': 'africa', 'countries': {
          'ABCDEFGH': 'south_africa',
          'JKLMN': 'ivory_coast'}},

    'B': {'region': 'africa', 'countries': {
          'ABCDE': 'angola',
          'FGHIJK': 'kenya',
          'LMNOPQR': 'tanzania'}},

    'C': {'region': 'africa', 'countries': {
          'ABCDE': 'benin',
          'FGHIJK': 'madagascar',
          'LMNOPQR': 'tunisia'}},

    'D': {'region': 'africa', 'countries': {
            'ABCDE': 'egypt',
            'FGHIJK': 'morocco',
            'LMNOPQR': 'zambia'}},

    'E': {'region': 'africa', 'countries': {
            'ABCDE': 'ethiopia',
            'FGHIJK': 'mozambique'}},

    'F': {'region': 'africa', 'countries': {
            'ABCDE': 'ghana',
            'FGHIJK': 'nigeria'}},

    # ASIA

    'J': {'region': 'asia', 'countries': {
            'ABCDEFGHIJKLMNOPQRST': 'Japan'}},

    'K': {'region': 'asia', 'countries': {
            'ABCDE': 'Sri Lanka',
            'FGHIJK': 'Israel',
            'LMNOPQR': 'Korea (South)'}},

    'L': {'region': 'asia', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'China'}},

    'M': {'region': 'asia', 'countries': {
            'ABCDE': 'India',
            'FGHIJK': 'Indonesia',
            'LMNOPQR': 'Thailand'}},

    'N': {'region': 'asia', 'countries': {
            'ABCDE': 'Philippines',
            'FGHIJK': 'Singapore',
            'LMNOPQR': 'Malaysia'}},

    'P': {'region': 'asia', 'countries': {
            'ABCDE': 'United Arab Emirates',
            'FGHIJK': 'Taiwan',
            'LMNOPQR': 'Vietnam',
            'STUVWXYZ0': 'Saudi Arabia'}},

    # Europe

    'S': {'region': 'europe', 'countries': {
            'ABCDEFGHIJKLM': 'United Kingdom',
            'NOPQRST': 'Germany',
            'UVWXYZ': 'Poland',
            '1234': 'Latvia'}},

    'T': {'region': 'europe', 'countries': {
            'ABCDEFGH': 'Switzerland',
            'JKLMNOP': 'Czech Republic',
            'RSTUV': 'Hungary',
            'WXYZ1234567890': 'Portugal'}},

    'U': {'region': 'europe', 'countries': {
            'HIJKLM': 'Denmark',
            'NOPQRST': 'Ireland',
            'UVWXYZ': 'Romania',
            '567': 'Slovakia'}},

    'V': {'region': 'europe', 'countries': {
            'ABCDE': 'Austria',
            'FGHIJKLMNOPQR': 'France',
            'STUVW': 'Spain',
            'XYZ12': 'Serbia',
            '345': 'Croatia',
            '67890': 'Estonia'}},

    'W': {'region': 'europe', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'Germany'}},

    'X': {'region': 'europe', 'countries': {
            'ABCDE': 'Bulgaria',
            'FGHIJK': 'Greece',
            'LMNOPQR': 'Netherlands',
            'STUVW': 'USSR',
            'XYZ2': 'Luxembourg',
            '34567890': 'Russia'}},

    'Y': {'region': 'europe', 'countries': {
            'ABCDE': 'Belgium',
            'FGHIJK': 'Finland',
            'LMNOPQR': 'Malta',
            'STUVW': 'Sweden',
            'XYZ12': 'Norway',
            '345': 'Belarus',
            '67890': 'Ukraine'}},

    'Z': {'region': 'europe', 'countries': {
            'ABCDEFGHIJKLMNOPQR': 'Italy',
            'STUVW': 'Finland',
            'XYZ12': 'Slovenia',
            '345': 'Lithuania'}},

    # Nort America

    '1': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'United States'}},

    '2': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'Canada'}},

    '3': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVW': 'Mexico'}},

    '3': {'region': 'north_america', 'countries': {
            'XYZ1234567': 'Costa Rica'}},

    '3': {'region': 'north_america', 'countries': {
            '890': 'Cayman Islands'}},

    '4': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'United States'}},

    '5': {'region': 'north_america', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': 'United States'}},

    # Oceania

    '6': {'region': 'oceania', 'countries': {
            'ABCDEFGHIJKLMNOPQRSTUVW': 'Australia'}},

    '7': {'region': 'oceania', 'countries': {
            'ABCDE': 'New Zealand'}},

    # South America

    '8': {'region': 'south_america', 'countries': {
            'ABCDE': 'Argentina',
            'FGHIJK': 'Chile',
            'LMNOPQR': 'Ecuador',
            'STUVW': 'Peru',
            'XYZ12': 'Venezuela'}},

    '9': {'region': 'south_america', 'countries': {
            'ABCDE': 'Brazil',
            'FGHIJK': 'Colombia',
            'LMNOPQR': 'Paraguay',
            'STUVW': 'Uruguay',
            'XYZ12': 'Trinidad & Tobago',
            '3456789': 'Brazil'}},

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
