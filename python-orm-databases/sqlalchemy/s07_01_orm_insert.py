from functools import partial

from sqlalchemy import (
    create_engine, text,
    Column, Integer, String, ForeignKey,

    insert,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.exc import InvalidRequestError

hprint = partial(print, "\n#")


Base = declarative_base()


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(30))
    description = Column(String, nullable=False)
    value = Column(Integer)

    potato_id = Column(ForeignKey('potato.pk'))
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


def main() -> None:

    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        future=True,
    )
    Base.metadata.create_all(engine)

    # insert data
    hprint("Generate insert statement")
    insert_statement = insert(Item.__table__).values(
        title="something",
        description="Walabee walaboo"
    )

    print("STATEMENT\t:", insert_statement)
    print("STATEMENT_TYPE\t:", type(insert_statement))

    compiled_statement = insert_statement.compile()
    print("COMPILED\t:", compiled_statement)
    print("PARAMS\t\t:", compiled_statement.params)

    # NOTE -> NOT SAFE DO NOT USE
    print(
        "FULL\t\t:",
        str(
            insert_statement.compile(
                compile_kwargs={'literal_binds': True}
            )
        )
    )

    hprint("Execute insert statement")
    with engine.connect() as conn:
        result = conn.execute(compiled_statement)
        print("RESULT_TYPE", type(result))
        print("IS_INSERT?:", result.is_insert)
        print("RETURNS ROWS?:", result.returns_rows)
        print("INSERTED:", result.inserted_primary_key)
        print("LAST PARAMS:", result.last_inserted_params())
        conn.commit()

    hprint("Alternative insert execution")
    with engine.connect() as conn:
        result = conn.execute(
            insert(Item.__table__),
            [
                {'title': 'kaboom', 'description': "chapa lama yama kai"},
                {'title': 'traktor', 'description': "tylko jedno glowie mam"},
            ]
        )
        if result.is_insert:
            try:
                print("INSERTED ONE:", result.inserted_primary_key)
            except InvalidRequestError:
                """
                !!! OBSERVATION
                the following propery works only for psycopg2 dialect
                at the moment
                """
                print("INSERTED MANY:", result.inserted_primary_key_rows)

            print("LAST PARAMS:", result.last_inserted_params())

        conn.commit()

    hprint("Get the data")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM item"))
        for x in result:
            print(x)


if __name__ == "__main__":
    main()
