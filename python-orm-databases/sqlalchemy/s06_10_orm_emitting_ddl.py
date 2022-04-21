from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship

hprint = partial(print, " \n#")


def main() -> None:
    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
    )

    # declare tables
    Base = declarative_base()

    class Item(Base):
        __tablename__ = "item"

        id = Column(Integer, primary_key=True, nullable=False)
        title = Column(String(30))
        description = Column(String, nullable=False)
        value = Column(Integer)

        potato_id = Column(ForeignKey('potato.pk'), nullable=False)
        potato = relationship('Potato', back_populates='items')

        def __repr__(self) -> str:
            return (
                f"Item(id={self.id}, title='{self.title}', value={self.value})"
            )

    class Potato(Base):
        __tablename__ = "potato"

        pk = Column(Integer, primary_key=True)
        size = Column(Integer)

        items = relationship('Item', back_populates='potato')

        def __repr__(self) -> str:
            return f"Potato(pk={self.pk})"

    hprint("Emit DDL")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
