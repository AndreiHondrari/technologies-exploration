"""create t1 table

Revision ID: 9d08b9ea5451
Revises:
Create Date: 2022-04-28 15:04:21.847475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d08b9ea5451'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        't1',
        sa.Column('pk', sa.Integer, primary_key=True, nullable=False),
        sa.Column('v', sa.Integer),
        sa.Column('d', sa.String),
    )


def downgrade():
    op.drop_table('t1')
