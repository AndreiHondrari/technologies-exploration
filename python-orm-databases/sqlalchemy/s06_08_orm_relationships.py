from functools import partial

from sqlalchemy import (
    Column, Integer, String, ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship

hprint = partial(print, "\n#")


def main() -> None:
    Base = declarative_base()

    class Item(Base):
        __tablename__ = "item"

        id = Column(Integer, primary_key=True, nullable=False)
        title = Column(String(30))
        description = Column(String, nullable=False)
        value = Column(Integer)
        potato_id = Column(ForeignKey('potato.pk'), nullable=False)

        potato = relationship('Potato', back_populates='items')

    class Potato(Base):
        __tablename__ = "potato"

        pk = Column(Integer, primary_key=True)
        size = Column(Integer)

        items = relationship('Item', back_populates='potato')

    hprint("underlying table")
    print(repr(Potato.__table__))


if __name__ == "__main__":
    main()
