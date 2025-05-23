"""fixing the default value

Revision ID: f1ac5bb66d16
Revises: d594fef8e32f
Create Date: 2025-02-14 07:34:33.844588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f1ac5bb66d16'
down_revision: Union[str, None] = 'd594fef8e32f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_ibfk_1', 'users', type_='foreignkey')
    op.drop_column('users', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', mysql.INTEGER(), server_default=sa.text("'3'"), autoincrement=False, nullable=True))
    op.create_foreign_key('users_ibfk_1', 'users', 'status', ['status'], ['id'])
    # ### end Alembic commands ###
