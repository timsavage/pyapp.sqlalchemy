"""
SQL Alchemy Extension for PyApp
===============================
"""
from __future__ import unicode_literals, absolute_import

import os

from pkg_resources import get_distribution, DistributionNotFound

from .factories import *

__name__ = 'SQL Alchemy Extension'
__default_settings__ = '.default_settings'
__checks__ = '.checks'

# Get installed version
try:
    _dist = get_distribution('pyApp')
    # Normalise case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'pyApp')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install pyApp.sqlalchemy via a package.'
else:
    __version__ = _dist.version
