"""empty message

Revision ID: 3fde81e57700
Revises: 02053f375c4e
Create Date: 2020-10-11 06:37:07.507452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fde81e57700'
down_revision = '02053f375c4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.drop_constraint('show_vanue_id_fkey', 'show', type_='foreignkey')
    op.create_foreign_key(None, 'show', 'Venue', ['venue_id'], ['id'])
    op.drop_column('show', 'vanue_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('vanue_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.create_foreign_key('show_vanue_id_fkey', 'show', 'Venue', ['vanue_id'], ['id'])
    op.drop_column('show', 'venue_id')
    # ### end Alembic commands ###
