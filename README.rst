python-libvin
=============

`libvin` is a python library which can decode Vehicle Identification Numbers.

Currently it can extract these informations:

 * Country
 * If the vehicle was build before 2010
 * If there is less than 500 of this vehicle model built per year
 * Region
 * Vehicle Descriptor Section
 * Vehicle Identifier Sequence
 * Vehicle Sequential Number
 * World Manufacturer Identifier
 * Year of the vehicle model

This is a work in progress and my only source of information about the many VIN standards
is a half baked Wikipedia article. So don't expect it to be perfect. 

Feel free to contribute !

Low level API example
---------------------

.. code-block:: python

    >>> from libvin.decoding import Vin
    >>>
    >>> v = Vin('2A4GM684X6R632476')
    >>> v.region
    north_america
    >>> v.country
    Canada
    >>> v.year
    2006
    >>> v.make
    Honada
    >>> v.manufacturer
    Honada Canda
    >>> v.is_pre_2010
    True
    >>> v.wmi
    2A4
    >>> v.vds
    GM684X
    >>> v.vis
    6R632476
    >>> v.vsn
    632476
    >>> v.less_than_500_built_per_year
    False


Methods
-------

+------------------------------+----------------------------------------------------------------+
| Method                       | Description                                                    |
+==============================+================================================================+
| country                      | Manufacturer's country                                         |
+------------------------------+----------------------------------------------------------------+
| is_pre_2010                  | If the vehicle was build before 2010                           |
+------------------------------+----------------------------------------------------------------+
| less_than_500_built_per_year | If there is less than 500 of this vehicle model built per year |
+------------------------------+----------------------------------------------------------------+
| make                         | Brand (e.g. Ford)                                              |
+------------------------------+----------------------------------------------------------------+
| manufacturer                 | Company (e.g. Ford Motor Company)                              |
+------------------------------+----------------------------------------------------------------+
| region                       | Region                                                         |
+------------------------------+----------------------------------------------------------------+
| vds                          | Vehicle Descriptor Section                                     |
+------------------------------+----------------------------------------------------------------+
| vis                          | Vehicle Identifier Sequence                                    |
+------------------------------+----------------------------------------------------------------+
| vsn                          | Vehicle Sequential Number                                      |
+------------------------------+----------------------------------------------------------------+
| wmi                          | World Manufacturer Identifier                                  |
+------------------------------+----------------------------------------------------------------+
| year                         | Year of the vehicle model                                      |
+------------------------------+----------------------------------------------------------------+


Standards
---------

There are at least four competing standards used to calculate VIN.

 * FMVSS 115, Part 565: Used in United States and Canada
 * ISO Standard 3779: Used in Europe and many other parts of the world
 * SAE J853: Very similar to the ISO standard
 * ADR 61/2: used in Australia, referring back to ISO 3779 and 3780

Here's a breakdown of the most common types:

ISO 3779
^^^^^^^^

::

    1 2 3 | 4 5 6 7 8 9 | 10 11 12 13 14 15 16 17
    -----   -----------   -----------------------
    |       |             |
    |       |             Vehicle Identifier Section
    |       |
    |       Vehicle Descriptor Section
    |
    World Manufacturer Idendified


European Union & North America (>500 vehicles/year)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::
 
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::
 
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


References
----------

 * http://en.wikipedia.org/wiki/Vehicle_Identification_Number
 * http://www.nisrinc.com/include/common/VIN.html
