"""modify status column in users table

Revision ID: d594fef8e32f
Revises: be0126655a68
Create Date: 2025-02-14 06:47:25.552319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd594fef8e32f'
down_revision: Union[str, None] = 'be0126655a68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.Integer(), server_default='3', nullable=True))
    op.drop_constraint('users_ibfk_1', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'status', ['status'], ['id'])
    op.drop_column('users', 'enabled')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('enabled', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_ibfk_1', 'users', 'status', ['enabled'], ['id'])
    op.drop_column('users', 'status')
    # ### end Alembic commands ###
