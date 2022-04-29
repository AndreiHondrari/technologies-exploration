import sqlalchemy as sa

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class T1(Base):
    __tablename__ = "t1"
    pk = sa.Column(
        sa.Integer,
        primary_key=True,
        nullable=False
    )

    v = sa.Column(sa.Integer)
    d = sa.Column(sa.String)
