from setuptools import setup, find_packages
import sys, os

VERSION = '0.0.1'

REQUIRES = [
    'nose',
]

setup(name='libvin',
    version=VERSION,
    description="Vehicle Identification Number Library",
    classifiers=[],
    keywords='vin vinlib authentic',
    author='Maxime Haineault (based on the work of Lukasz Szybalski)',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/python-libvin',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    tests_require=REQUIRES,
    install_requires=REQUIRES,
)
