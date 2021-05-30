"""empty message

Revision ID: a214cc560f99
Revises: 6f3368f9b41d
Create Date: 2021-01-05 13:09:29.890721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a214cc560f99'
down_revision = '6f3368f9b41d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade',
    sa.Column('ID', sa.String(length=255), nullable=False),
    sa.Column('amount', sa.String(length=255), nullable=True),
    sa.Column('time', sa.DATETIME(), nullable=True),
    sa.Column('member_ID', sa.String(length=255), nullable=True),
    sa.Column('staff_ID', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['member_ID'], ['member.ID'], ),
    sa.ForeignKeyConstraint(['staff_ID'], ['staff.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('sale',
    sa.Column('ID', sa.String(length=255), nullable=False),
    sa.Column('goods_ID', sa.String(length=255), nullable=True),
    sa.Column('number', sa.INTEGER(), nullable=True),
    sa.Column('total_amount', sa.String(length=255), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['goods_ID'], ['goods.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    op.drop_table('trade')
    # ### end Alembic commands ###
