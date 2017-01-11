"""
This file is part of Foobar.

    Foobar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

import glob
import os
import sys

if hasattr(sys, 'frozen'):
    # we are in an executable
    ext = '.pyc'
else:
    ext = os.path.splitext(__file__)[1]

__all__ = [os.path.basename(f)[:-len(ext)] for f in glob.glob(
           os.path.dirname(__file__) + '/*{}'.format(ext))]
