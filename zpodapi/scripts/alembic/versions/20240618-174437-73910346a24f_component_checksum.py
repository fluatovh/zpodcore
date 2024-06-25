"""component_checksum

Revision ID: 73910346a24f
Revises: 08d982dc70de
Create Date: 2024-06-18 17:44:37.783173

"""

import json
from pathlib import Path

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = "73910346a24f"
down_revision = "08d982dc70de"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "components",
        sa.Column("file_checksum", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )

    components_table = sa.sql.table(
        "components",
        sa.Column("id", sa.INTEGER()),
        sa.Column("jsonfile", sa.VARCHAR()),
        sa.Column("file_checksum", sa.VARCHAR()),
    )

    # Add checksum to the new column file_checksum
    conn = op.get_bind()
    results = conn.execute(text("select id, jsonfile from components")).fetchall()
    for id_, jsonfile in results:
        if Path(jsonfile).exists():
            with open(jsonfile) as f:
                component_json = json.load(f)
                component_checksum = component_json["component_download_file_checksum"]
        else:
            print(f"Unable to find file: {jsonfile}")
            component_checksum = ""

        op.execute(
            components_table.update()
            .where(components_table.c.id == id_)
            .values(file_checksum=component_checksum)
        )

    op.alter_column("components", "file_checksum", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("components", "file_checksum")
    # ### end Alembic commands ###
