"""added test col

Revision ID: 4b4d8bd014eb
Revises: b2516d1fb564
Create Date: 2020-03-05 22:03:34.252998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b4d8bd014eb'
down_revision = 'b2516d1fb564'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bug',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bug_tracker_url', sa.String(length=255), nullable=True),
    sa.Column('root_cause', sa.String(length=255), nullable=True),
    sa.Column('who', sa.String(length=255), nullable=True),
    sa.Column('when', sa.DateTime(), nullable=True),
    sa.Column('test', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bug_tracker_url')
    )
    op.add_column('products', sa.Column('recommandable', sa.Boolean(), nullable=True))
    op.add_column('products', sa.Column('sub_sub_sub_category', sa.String(length=255), nullable=True))
    op.add_column('products', sa.Column('test', sa.Integer(), nullable=True))
    op.drop_column('products', 'recommendable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('recommendable', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('products', 'test')
    op.drop_column('products', 'sub_sub_sub_category')
    op.drop_column('products', 'recommandable')
    op.drop_table('bug')
    # ### end Alembic commands ###
