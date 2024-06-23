"""Renomear coluna usuario para cpf_cnpj

Revision ID: 99a4e0cf7f29
Revises: 
Create Date: 2024-06-13 17:40:54.882117

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "99a4e0cf7f29"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("usuario", schema=None) as batch_op:
        batch_op.add_column(sa.Column("cpf_cnpj", sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column("email", sa.String(length=20), nullable=False))
        batch_op.drop_column("usuario")
        batch_op.drop_column("_email")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("usuario", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("_email", mysql.VARCHAR(length=20), nullable=False)
        )
        batch_op.add_column(
            sa.Column("usuario", mysql.VARCHAR(length=20), nullable=False)
        )
        batch_op.drop_column("email")
        batch_op.drop_column("cpf_cnpj")

    # ### end Alembic commands ###