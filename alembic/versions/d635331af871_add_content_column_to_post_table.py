"""add content column to post table

Revision ID: d635331af871
Revises: 3ac54088df0f
Create Date: 2023-05-31 21:58:08.958502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd635331af871'
down_revision = '3ac54088df0f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
