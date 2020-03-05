"""Baseline migration

Revision ID: b2516d1fb564
Revises: 
Create Date: 2020-03-05 21:52:02.292390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2516d1fb564'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id_pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255)),
        sa.Column('description', sa.Text),
        sa.Column('brand', sa.String(255)),
        sa.Column('price', sa.Integer),
        sa.Column('discount', sa.Integer),
        sa.Column('stock', sa.Integer),
        sa.Column('category', sa.String(255)),
        sa.Column('sub_category', sa.String(255)),
        sa.Column('sub_sub_category', sa.String(255)),
        sa.Column('recommendable', sa.Boolean),
        sa.Column('online_only', sa.Boolean),
        sa.Column('target_demographic', sa.String(255)),
        sa.Column('gender', sa.String(90)),  # TODO: Hier nog een set van maken
        sa.Column('color', sa.String(100)),  # TODO: Hier nog een set van maken
        sa.Column('unit', sa.String(255)),
        sa.Column('odor_type', sa.String(255)),
        sa.Column('series', sa.String(255)),
        sa.Column('kind', sa.String(255)),
        sa.Column('variant', sa.String(255)),
        sa.Column('type', sa.String(255)),
        sa.Column('type_of_hair_care', sa.String(255)),
        sa.Column('type_of_hair_coloring', sa.String(255)),  # TODO: Hier nog een set van maken
    )


def downgrade():
    op.drop_table('bug')
