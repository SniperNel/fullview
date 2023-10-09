"""update

Revision ID: f2dec5bfa782
Revises: 5c98bf46ca64
Create Date: 2023-10-08 16:37:19.204846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2dec5bfa782'
down_revision: Union[str, None] = '5c98bf46ca64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
