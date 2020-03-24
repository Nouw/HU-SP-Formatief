"""Testing foreignkeys

Revision ID: f17d8ed185f6
Revises: 1040843763a0
Create Date: 2020-03-11 17:24:06.938211

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f17d8ed185f6'
down_revision = '1040843763a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recommended_before',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('products', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('test', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_table('recommended_before')
    # ### end Alembic commands ###