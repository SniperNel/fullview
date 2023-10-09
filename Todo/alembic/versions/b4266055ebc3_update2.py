"""update2

Revision ID: b4266055ebc3
Revises: f2dec5bfa782
Create Date: 2023-10-08 16:40:53.061825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4266055ebc3'
down_revision: Union[str, None] = 'f2dec5bfa782'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
