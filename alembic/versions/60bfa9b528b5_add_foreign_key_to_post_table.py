"""add foreign key to post table

Revision ID: 60bfa9b528b5
Revises: b5242390f771
Create Date: 2023-05-31 22:16:06.850961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60bfa9b528b5'
down_revision = 'b5242390f771'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
