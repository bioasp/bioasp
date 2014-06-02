# Copyright (c) 2014, Sven Thiele <sthiele78@gmail.com>
#
# This file is part of BioASP.
#
# BioASP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BioASP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BioASP.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name = 'bioasp',
    version = '1.2dev',
    url='http://bioasp.github.io/',
    license='GPLv3+',
    description="Answer Set Programming for Systems Biology",
    long_description=open('README.md').read(),   
    author='Sven Thiele',
    author_email='sthiele78@gmail.com',
    install_requires=[
        'ingranalyze',
        'meneco',
        'shogen',
        'precursor',
        'caspo'
    ]
)
