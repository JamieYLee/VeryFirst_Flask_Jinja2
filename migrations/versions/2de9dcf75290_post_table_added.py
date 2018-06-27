"""post table added

Revision ID: 2de9dcf75290
Revises: 86a1539a5746
Create Date: 2018-06-27 10:31:06.800026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2de9dcf75290'
down_revision = '86a1539a5746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###