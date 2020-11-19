"""empty message

Revision ID: aaa79a998760
Revises: 3e2dd47a0a1c
Create Date: 2020-10-08 21:59:10.253497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaa79a998760'
down_revision = '3e2dd47a0a1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('Vanue_id', sa.Integer(), nullable=False),
    sa.Column('Artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['Vanue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('Vanue_id', 'Artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    # ### end Alembic commands ###