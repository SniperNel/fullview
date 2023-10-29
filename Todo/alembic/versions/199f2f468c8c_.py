"""empty message

Revision ID: 199f2f468c8c
Revises: 7cb34ef83ce9
Create Date: 2023-10-28 07:40:47.319358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '199f2f468c8c'
down_revision: Union[str, None] = '7cb34ef83ce9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
