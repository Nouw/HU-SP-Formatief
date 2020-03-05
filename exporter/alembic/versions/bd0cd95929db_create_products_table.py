"""create products table


Revision ID: bd0cd95929db
Revises: 
Create Date: 2020-03-05 20:13:06.136879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd0cd95929db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id_pk', sa.Integer, primary_key=True),
        sa.Column('_id', sa.Integer)
    )


def downgrade():
    op.drop_table('products')