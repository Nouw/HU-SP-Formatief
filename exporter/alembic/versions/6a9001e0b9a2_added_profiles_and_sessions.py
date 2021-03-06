"""Added profiles and sessions

Revision ID: 6a9001e0b9a2
Revises: 2d1a65725662
Create Date: 2020-03-10 14:03:05.328962

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6a9001e0b9a2'
down_revision = '2d1a65725662'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id_pk', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=255), nullable=True),
    sa.Column('first_order', sa.DateTime(), nullable=True),
    sa.Column('latest_order', sa.DateTime(), nullable=True),
    sa.Column('order_amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_pk')
    )
    op.create_table('sessions',
    sa.Column('id_pk', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=255), nullable=True),
    sa.Column('session_start', sa.DateTime(), nullable=True),
    sa.Column('session_end', sa.DateTime(), nullable=True),
    sa.Column('browser_name', sa.String(length=255), nullable=True),
    sa.Column('os_name', sa.String(length=255), nullable=True),
    sa.Column('is_mobile_flag', sa.Boolean(), nullable=True),
    sa.Column('is_pc_flag', sa.Boolean(), nullable=True),
    sa.Column('is_tablet_flag', sa.Boolean(), nullable=True),
    sa.Column('is_email_flag', sa.Boolean(), nullable=True),
    sa.Column('device_family', sa.String(length=255), nullable=True),
    sa.Column('device_brand', sa.String(length=255), nullable=True),
    sa.Column('device_model', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id_pk')
    )
    op.drop_index('bug_tracker_url', table_name='bug')
    op.drop_table('bug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bug',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('bug_tracker_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('root_cause', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('who', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('when', mysql.DATETIME(), nullable=True),
    sa.Column('test', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('bug_tracker_url', 'bug', ['bug_tracker_url'], unique=True)
    op.drop_table('sessions')
    op.drop_table('profiles')
    # ### end Alembic commands ###
