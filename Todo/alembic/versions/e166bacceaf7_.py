"""empty message

Revision ID: e166bacceaf7
Revises: 199f2f468c8c
Create Date: 2023-10-29 13:33:36.992510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e166bacceaf7'
down_revision: Union[str, None] = '199f2f468c8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
