"""fix

Revision ID: 29364e72f9dc
Revises: 4099eb008b30
Create Date: 2025-02-14 08:26:39.187983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29364e72f9dc'
down_revision: Union[str, None] = '4099eb008b30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quadrant_priority',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority_name', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quadrant_priority_id'), 'quadrant_priority', ['id'], unique=False)
    op.create_index(op.f('ix_quadrant_priority_priority_name'), 'quadrant_priority', ['priority_name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quadrant_priority_priority_name'), table_name='quadrant_priority')
    op.drop_index(op.f('ix_quadrant_priority_id'), table_name='quadrant_priority')
    op.drop_table('quadrant_priority')
    # ### end Alembic commands ###
