"""empty message

Revision ID: f4417da578e5
Revises: df5729aed5d2
Create Date: 2016-06-17 10:55:51.582098

"""

# revision identifiers, used by Alembic.
revision = 'f4417da578e5'
down_revision = 'df5729aed5d2'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'user', ['creator_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'creator_id')
    ### end Alembic commands ###
