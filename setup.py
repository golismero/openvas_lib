#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from distutils.core import setup


__license__ = """
OpenVAS Manager OMPv4 and XML parser.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


# Text describing the module.
description = 'OpenVAS Manager for OpenVAS 6 to 8 and XML report parser'
try:
    readme = os.path.join(os.getcwd(), 'README.rst')
    long_description = open(readme, 'rU').read()
except IOError:
    long_description = description

# Set the parameters for the setup script.
metadata = {

    # Setup instructions.
    'provides': ['openvas_lib'],
    'packages': ['openvas_lib'],

    # Metadata.
    'name': 'openvas_lib',
    'version': '1.1',
    'description': description,
    'long_description': long_description,
    'author': 'Daniel Garcia Garcia (cr0hn)',
    'author_email': 'cr0hn' + '@' + 'cr0hn.com',
    'license': 'GPLv2',
    'url': 'http://www.golismero.com/',
    'download_url': 'https://github.com/golismero/openvas_lib/zipball/master',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
    ],
}


# Execute the setup script.
def main():
    setup(**metadata)


if __name__ == '__main__':
    main()
