"""empty message

Revision ID: 946b32b0d0cd
Revises: cb88e6013fdd
Create Date: 2020-10-10 23:53:50.345565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946b32b0d0cd'
down_revision = 'cb88e6013fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('Start_time', sa.String(length=25), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'Start_time')
    # ### end Alembic commands ###
