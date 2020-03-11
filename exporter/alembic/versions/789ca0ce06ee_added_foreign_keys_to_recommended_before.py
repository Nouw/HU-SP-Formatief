"""Added foreign keys to recommended_before

Revision ID: 789ca0ce06ee
Revises: 8c49969fa6bf
Create Date: 2020-03-11 19:11:06.795850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '789ca0ce06ee'
down_revision = '8c49969fa6bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommended_before', sa.Column('product_id', sa.Integer(), nullable=True))
    op.add_column('recommended_before', sa.Column('profile_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recommended_before', 'products', ['product_id'], ['id_pk'])
    op.create_foreign_key(None, 'recommended_before', 'profiles', ['profile_id'], ['id_pk'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recommended_before', type_='foreignkey')
    op.drop_constraint(None, 'recommended_before', type_='foreignkey')
    op.drop_column('recommended_before', 'profile_id')
    op.drop_column('recommended_before', 'product_id')
    # ### end Alembic commands ###
