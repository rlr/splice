"""empty message

Revision ID: 4e412794c186
Revises: 29166b03d02a
Create Date: 2014-09-15 21:19:21.343928

"""

# revision identifiers, used by Alembic.
revision = '4e412794c186'
down_revision = '29166b03d02a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('impression_stats_daily', sa.Column('month', sa.Integer(), nullable=False))
    op.add_column('impression_stats_daily', sa.Column('week', sa.Integer(), nullable=False))
    op.add_column('impression_stats_daily', sa.Column('year', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('impression_stats_daily', 'year')
    op.drop_column('impression_stats_daily', 'week')
    op.drop_column('impression_stats_daily', 'month')
    ### end Alembic commands ###
