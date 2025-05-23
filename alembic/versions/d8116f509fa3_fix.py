"""fix

Revision ID: d8116f509fa3
Revises: 29364e72f9dc
Create Date: 2025-02-14 08:27:36.938453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8116f509fa3'
down_revision: Union[str, None] = '29364e72f9dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('priority', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'quadrant_priority', ['priority'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'priority')
    # ### end Alembic commands ###
