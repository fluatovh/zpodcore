"""user_updates

Revision ID: e67c0d042ef8
Revises: cf21e63aeb4f
Create Date: 2023-09-12 20:30:52.403061

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "e67c0d042ef8"
down_revision = "cf21e63aeb4f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "status")
    # ### end Alembic commands ###