# Copyright (c) 2001-2014, Canal TP and/or its affiliates. All rights reserved.
#
# This file is part of Navitia,
#     the software to build cool stuff with public transport.
#
# Hope you'll enjoy and contribute to this project,
#     powered by Canal TP (www.canaltp.fr).
# Help us simplify mobility and open public transport:
#     a non ending quest to the responsive locomotion way of traveling!
#
# LICENCE: This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Stay tuned using
# twitter @navitia
# IRC #navitia on freenode
# https://groups.google.com/d/forum/navitia
# www.navitia.io

""" init database

Revision ID: 1fd68e6d0456
Revises: None
Create Date: 2014-01-10 16:25:30.432738

"""

# revision identifiers, used by Alembic.
revision = '1fd68e6d0456'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('login', sa.Text(), nullable=False),
        sa.Column('email', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('login')
    )
    op.create_table('instance',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('is_free', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('authorization',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('instance_id', sa.Integer(), nullable=False),
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['api_id'], ['api.id'], ),
        sa.ForeignKeyConstraint(['instance_id'], ['instance.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'instance_id', 'api_id')
    )
    op.create_table('job',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('task_uuid', sa.Text(), nullable=True),
        sa.Column('filename', sa.Text(), nullable=True),
        sa.Column('type', sa.Text(), nullable=True),
        sa.Column('instance_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['instance_id'], ['instance.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('key',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('token', sa.Text(), nullable=False),
        sa.Column('valid_until', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('token')
    )

    api = table('api', column('name', sa.String))
    op.bulk_insert(api, [{'name': 'ALL'}])
    ### end Alembic commands ###



def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('key')
    op.drop_table('job')
    op.drop_table('authorization')
    op.drop_table('instance')
    op.drop_table('user')
    op.drop_table('api')
    ### end Alembic commands ###