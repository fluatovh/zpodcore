"""profile

Revision ID: 1427af2dd43a
Revises: a84f30a806e0
Create Date: 2023-06-14 15:24:13.467804

"""
import sqlalchemy as sa
import sqlmodel

from alembic import op

# revision identifiers, used by Alembic.
revision = "1427af2dd43a"
down_revision = "a84f30a806e0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("profile", sa.JSON(), nullable=False),
        sa.Column("creation_date", sa.DateTime(), nullable=False),
        sa.Column("last_modified_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profiles")
    # ### end Alembic commands ###