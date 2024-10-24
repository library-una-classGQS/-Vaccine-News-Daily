"""empty message

Revision ID: 5ff73c0b7ff2
Revises: a0e90b3312a3
Create Date: 2024-09-23 20:07:28.152334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ff73c0b7ff2'
down_revision = 'a0e90b3312a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cartao_sus', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('cartao_sus')

    # ### end Alembic commands ###
