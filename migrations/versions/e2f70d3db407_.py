"""empty message

Revision ID: e2f70d3db407
Revises: cbd83d28cb41
Create Date: 2017-05-15 15:01:40.150704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2f70d3db407'
down_revision = 'cbd83d28cb41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ss_user', sa.Column('created', sa.Date(), nullable=True))
    op.add_column('ss_user', sa.Column('submitted', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ss_user', 'submitted')
    op.drop_column('ss_user', 'created')
    # ### end Alembic commands ###
