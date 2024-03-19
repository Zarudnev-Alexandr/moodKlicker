"""change db

Revision ID: 3433a625235d
Revises: 1b717181ec21
Create Date: 2024-02-27 20:04:13.295621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3433a625235d'
down_revision: Union[str, None] = '1b717181ec21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### bot auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'boost', ['id'])
    op.create_unique_constraint(None, 'bought', ['id'])
    op.create_unique_constraint(None, 'item', ['id'])
    op.create_unique_constraint(None, 'user', ['telegram_id'])
    # ### end Alembic bot ###


def downgrade() -> None:
    # ### bot auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'item', type_='unique')
    op.drop_constraint(None, 'bought', type_='unique')
    op.drop_constraint(None, 'boost', type_='unique')
    # ### end Alembic bot ###
