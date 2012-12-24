'''
Created on Jan 15, 2011

@author: vahid
'''
import os
from setuptools import setup, find_packages
from khayyam import __version__ as package_version
 
__version__ = package_version


setup(
    name="Khayyam",
    version=package_version,
    packages=find_packages(),
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://pylover.dobisel.com/projects/khayyam",
    description="Khayyam(Jalali Persian Datetime) library",
    zip_safe=True,
    keywords="Khayyam persian jalali date time",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    classifiers=[
        "Programming Language :: Python",
        "License :: Freeware",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"],
)
