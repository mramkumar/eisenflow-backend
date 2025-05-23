"""adding foreign key for assignee in tasks table

Revision ID: dda6b9b982e8
Revises: f97ccda6337e
Create Date: 2025-02-14 05:54:11.762586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dda6b9b982e8'
down_revision: Union[str, None] = 'f97ccda6337e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tasks', 'users', ['assignee'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    # ### end Alembic commands ###
