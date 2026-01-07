"""add content column to posts table

Revision ID: 515242a91b07
Revises: 636d0235d07c
Create Date: 2026-01-06 15:33:55.410849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '515242a91b07'
down_revision: Union[str, Sequence[str], None] = '636d0235d07c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
