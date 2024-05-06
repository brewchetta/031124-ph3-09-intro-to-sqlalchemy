"""empty message

Revision ID: 3fc54300ba11
Revises: ee572564ebf0
Create Date: 2024-05-06 10:42:10.482940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc54300ba11'
down_revision = 'ee572564ebf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hamburgers_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('meat', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hamburgers_table')
    # ### end Alembic commands ###
