"""Initial migration

Revision ID: b08084a74341
Revises: 
Create Date: 2025-01-19 16:31:03.334787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b08084a75341'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.add_column('contacts', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('contacts', sa.Column('surname', sa.String(length=50), nullable=False))
    op.add_column('contacts', sa.Column('phone', sa.String(length=20), nullable=False))
    op.add_column('contacts', sa.Column('birthday', sa.Date(), nullable=False))
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('contacts_phone_number_key', 'contacts', type_='unique')
    op.create_unique_constraint(None, 'contacts', ['phone'])
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('contacts', 'birth_date')
    op.drop_column('contacts', 'last_name')
    op.drop_column('contacts', 'phone_number')
    op.drop_column('contacts', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_constraint(None, 'contacts', type_='unique')
    op.create_unique_constraint('contacts_phone_number_key', 'contacts', ['phone_number'])
    op.drop_column('contacts', 'user_id')
    op.drop_column('contacts', 'birthday')
    op.drop_column('contacts', 'phone')
    op.drop_column('contacts', 'surname')
    op.drop_column('contacts', 'name')
    op.drop_table('users')
    # ### end Alembic commands ###
