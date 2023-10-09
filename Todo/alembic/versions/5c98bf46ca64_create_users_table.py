"""create_users_table

Revision ID: 5c98bf46ca64
Revises: 
Create Date: 2023-10-07 23:54:02.847824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c98bf46ca64'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'routines',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('morning', sa.String(100), nullable=False),
        sa.Column('afternoon', sa.String(100), nullable=False),
        sa.Column('night', sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('routines')
