from functools import partial

from sqlalchemy import (
    Column, Integer, String, ForeignKey,
)
from sqlalchemy.orm import registry

hprint = partial(print, " \n#")


def main() -> None:
    mapper_registry = registry()
    hprint("metadata from registry")
    print(repr(mapper_registry.metadata))

    Base = mapper_registry.generate_base()

    class Item(Base):
        __tablename__ = "item"

        id = Column(Integer, primary_key=True, nullable=False)
        title = Column(String(30))
        description = Column(String, nullable=False)
        value = Column(Integer)
        potato = Column(ForeignKey('potato.pk'), nullable=False)

    class Potato(Base):
        __tablename__ = "potato"

        pk = Column(Integer, primary_key=True)
        size = Column(Integer)

    hprint("underlying table")
    print(repr(Potato.__table__))


if __name__ == "__main__":
    main()
