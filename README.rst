python-libvin
=============

`libvin` is a python library which can decode Vehicle Identification Numbers.

Currently it can exctract these informations:

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

::

    >>> from libvin.decoding import Vin
    >>>
    >>> v = Vin('2A4GM684X6R632476')
    >>> v.region
    north_america
    >>> v.country
    Canada
    >>> v.year
    2006
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

Credits
=======

This project was created and is sponsored by:

.. figure:: http://motion-m.ca/media/img/logo.png
    :figwidth: image

Motion Média (http://motion-m.ca)
