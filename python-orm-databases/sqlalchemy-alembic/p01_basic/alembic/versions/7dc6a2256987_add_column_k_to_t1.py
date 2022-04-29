"""add column k to t1

Revision ID: 7dc6a2256987
Revises: 2897f3bc82bb
Create Date: 2022-04-28 15:09:02.277147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dc6a2256987'
down_revision = '2897f3bc82bb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        't1',
        sa.Column('k', sa.Integer)
    )


def downgrade():
    op.drop_column('t1', 'k')
