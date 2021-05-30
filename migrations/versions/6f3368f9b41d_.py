"""empty message

Revision ID: 6f3368f9b41d
Revises: a94294b693df
Create Date: 2021-01-05 13:03:25.303097

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f3368f9b41d'
down_revision = 'a94294b693df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    op.drop_table('trade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade',
    sa.Column('ID', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('amount', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('time', mysql.DATETIME(), nullable=True),
    sa.Column('member_ID', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('staff_ID', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['member_ID'], ['member.ID'], name='trade_ibfk_1'),
    sa.ForeignKeyConstraint(['staff_ID'], ['staff.ID'], name='trade_ibfk_2'),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('sale',
    sa.Column('ID', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('goods_ID', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('number', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('total_amount', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['goods_ID'], ['goods.ID'], name='sale_ibfk_1'),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
