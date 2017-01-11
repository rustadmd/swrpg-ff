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

from pony import orm

_DB = orm.Database()
_DB.bind('sqlite', ':memory:')


class RpgType(_DB.Entity):
    name = orm.Required(str)
    parent = orm.Optional('RpgType', reverse='children')

    children = orm.Set('RpgType', reverse='parent')
    objects = orm.Set('RpgObject')
    stats = orm.Set('RpgStat')


class RpgObject(_DB.Entity):
    name = orm.Required(str)
    description = orm.Optional(str)
    type = orm.Required(RpgType)

    stats = orm.Set('RpgStat')


class RpgStat(_DB.Entity):
    name = orm.Required(str)
    value = orm.Required(int)
    object = orm.Required(RpgObject)
    type = orm.Required(RpgType)


def save():
    _DB.commit()

_DB.generate_mapping(create_tables=True)
