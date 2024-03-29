"""empty message

Revision ID: af4bddb27fb4
Revises: 8d49d1e5547c
Create Date: 2019-12-04 09:10:31.429755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af4bddb27fb4'
down_revision = '8d49d1e5547c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('description', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'description')
    # ### end Alembic commands ###
