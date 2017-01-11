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

from models import database
from models.database import RpgObject
from models.database import RpgStat
from models.database import RpgType


@orm.db_session
def populate_types():

    c = RpgType(name='Character')
    RpgType(name='PC', parent=c)
    npc = RpgType(name='NPC', parent=c)
    RpgType(name='Minion', parent=npc)

    RpgType(name='Characteristic')
    RpgType(name='Skill')

    database.save()


@orm.db_session
def populate_demo_data():

    pc_type = RpgType.get(name='Character')
    g = RpgObject(name='Gand', type=pc_type)
    RpgStat(name='Brawn', value=2, object=g,
            type=RpgType.get(name='Characteristic'))

    database.save()
