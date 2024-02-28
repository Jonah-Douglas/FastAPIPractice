"""Add content column to posts table

Revision ID: d67eafb19b68
Revises: 49194e111918
Create Date: 2024-02-27 19:01:23.070130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd67eafb19b68'
down_revision: Union[str, None] = '49194e111918'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
