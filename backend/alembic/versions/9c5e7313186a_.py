"""empty message

Revision ID: 9c5e7313186a
Revises: 62caa81583ec
Create Date: 2025-06-20 03:43:35.418593

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "9c5e7313186a"
down_revision: str | None = "62caa81583ec"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
