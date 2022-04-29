"""create table t2

Revision ID: 2897f3bc82bb
Revises: 9d08b9ea5451
Create Date: 2022-04-28 15:07:07.465578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2897f3bc82bb'
down_revision = '9d08b9ea5451'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        't2',
        sa.Column('pk', sa.Integer, primary_key=True, nullable=False),
        sa.Column('v', sa.Integer),
        sa.Column('d', sa.String)
    )


def downgrade():
    op.drop_table('t2')
