# SQLAlchemy

https://sqlalchemy.org

## Setting up an engine

```python
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite+pysqlite://:memory:",
    echo=True,
    future=True
)
```

The engine is our API provider that allows us to create connections to the
database of choice.

Notice that for SQL we used the `sqlite+pysqlite://:memory:` string, where:

- `sqlite` is the dialect
- `pysqlite` is the python to sqlite connector
- `:memory:` is the storage location for the database, in our case, it being the
  RAM.

If we wanted to connect to a Postgres server instead, we could have done
`postgresql+psycopg2://server_user:server_password@127.0.0.1:5432/database_name`

## Initiating a connection

The `commit()` is necessary for `engine.connect()` and `Session(engine)` context
blocks, to persist any changes to the database.

The `engine.begin()` does not require `commit()` as it will automatically commit
at the end of the context block.

The `.commit()` can be called multiple times during a transaction block.

The `.rollback()` will only roll back the transaction up to the last commit.

### By connecting

```python
with engine.connect() as conn:
    ...
    conn.commit()
```

### By beginning an auto-commit transaction

```python
with engine.begin() as conn:
    ...
    # .commit() call not required
```

### By creating a session

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    ...
    conn.commit()
```

## Using raw sql

Typically you can just call the SQL like:

```python
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE t1 (x INT)"))
    conn.commit()
```

or with session

```python
with Session(engine) as session:
    session.execute(text("CREATE TABLE t1 (x INT)"))
    session.commit()
```

A particular distinction between `Connection.execute()` and `Session.execute()`
is that:

- `Connection.execute()` will always return a `CursorResult`
- `Session.execute()` over a `Table` returns a `CursorResult`
- `Session.execute()` over an ORM model returns a `ChunkedIteratorResult`

## Defining ORM models

### Metadata and table

```python
from sqlalchemy import (
    MetaData, Table, Column,
    Integer, String,
)

metadata_obj = MetaData()

item_table = Table(
    "item",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(30)),
    Column('description', String),
)
```

### Registry

```python
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(30))
    description = Column(String, nullable=False)
    value = Column(Integer)
```

For which we can obtain the underlying table with `Item.__table__`.

### Declarative base

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(30))
    description = Column(String, nullable=False)
    value = Column(Integer)
```

## SQL to SQLAlchemy mapping

### Create table

```sql
CREATE TABLE t1 (val INT, bla VARCHAR(30));
```

#### With metadata and table

```python
metadata_obj = MetaData()
t1_table = Table(
    "t1",
    metadata_obj,
    Column('val', Integer),
    Column('bla', String(30))
)

metadata_obj.create_all(engine)
```

#### With ORM base

```python
class T1(Base):
    __tablename__ = "t1"
    val = Column(Integer)
    bla = Column(String(30))

Base.metadata.create_all(engine)
```

For both Core and ORM a single table can be created by calling
`table_obj.create(engine)`

Throughout the rest of the document we will be using ORM tables for
simplification.

### Create table if it doesn't exist

```sql
CREATE TABLE IF NOT EXISTS t1 (val INT, bla VARCHAR(30));
```

By default `metadata.create_all` has a parameter `checkfirst=True` that will
bake the `IF NOT EXISTS` into the resulting SQL declaration.

The `table_obj.create` however has the `checkfirst` parameter <u> **set to False
by default**</u>

### Drop table

```sql
DROP TABLE t1;
```

```python
table_obj.drop(engine)
```

**! BEWARE !** - the table will still exist in the **MetaData**, so you will
need to manually remove it by calling `metadata.remove(table_obj)`.

### Drop table if it exists

```sql
DROP TABLE IF EXISTS t1;
```

```python
table_obj.drop(engine, checkfirst=True)
```

### Insert a single value

Assuming our table is:

```sql
CREATE TABLE t1 (val INT, bla VARCHAR(30));
```

```sql
INSERT INTO t1 VALUES (11, 'bla');
```

#### With insert and values

```python
from sqlalchemy import insert

insert_statement = insert(T1).values((11, "abcdefg",))
session.execute(insert_statement)
```

or

```python
insert_statement = insert(T1).values({'val': 11, 'bla': "abcdefg"})
session.execute(insert_statement)
```

#### Values as parameters for execute

```python
session.execute(insert(T1), {'val': 11, 'bla': "abcdefg"})
```

### Query all rows

```sql
SELECT * FROM t1;
```

```python
from sqlalchemy import select

select_statement = select(T1)
result = session.execute(select_statement)
rows = result.all()
```

or

```python
select("*").select_from(T1)
```

### Query specific column

```sql
SELECT bla FROM t1;
```

```python
select_statement = select(T1.bla)
```

### Query with condition

```sql
SELECT * FROM t1 WHERE val >= 42;
```

```python
select(T1).where(x >= 42)
```

### Insert multiple rows

```sql
INSERT INTO t1 VALUES
    (11, 'bla'),
    (22, 'kek'),
    (33, 'lol');
```

```python
insert(T1).values([
    {'v': 11, 'd': "bla"},
    {'v': 22, 'd': "kek"},
    {'v': 33, 'd': "lol"},
])
```

### Copy insert from one table to another

Assuming our tables our:

```python
class T1(Base):
    pk = Column(Integer, primary_key=True)
    v = Column(Integer)
    d = Column(String(30))


class T2(Base):
    pk = Column(Integer, primary_key=True)
    x = Column(Integer)
    descr = Column(String(30))
```

```sql
INSERT INTO t2(x, descr) SELECT t1.v, t1.d FROM t1
```

```python
select_statement = select(T1.v, T1.d)
insert(T2).from_select([T2.x, T2.descr], select_statement)
```

### Delete all rows

```sql
DELETE FROM t1;
```

```python
from sqlalchemy import delete

delete(T1)
```

### Delete specific row

```sql
DELETE FROM t1 WHERE val >= 42;
```

```python
delete(T1).where(T1.val >= 42)
```

### Update column with specific value on all rows

```sql
UPDATE t1 SET bla = 'foo';
```

```python
from sqlalchemy import update

update(T1).values(bla="foo")
```

### Update column with specific value on condition

```sql
UPDATE t1 SET bla = 'foo' WHERE val = 42;
```

```python
update(T1).where(T1.val==42).values(bla="foo")
```

### Query distinct values on column

```sql
SELECT DISTINCT val FROM t1;
SELECT DISTINCT(val) FROM t1;
```

```python
from sqlalchemy import distinct

select(distinct(T1.val))
```

### Limit query results

```sql
SELECT * FROM t1 LIMIT 5;
```

```python
select(T1).limit(5)
```

or we could fetch only one value

```python
select(T1).limit(1)
```

but since we get a single row we could call

```python
session.execute(select(T1).limit(1)).first()
```

### Scalars

A select typically will result in a list of rows, but if we are dealing with a
single column, or the row has only 1 item within, then we might want to look at
`session.scalars` for an 1x1 array and `session.scalar` for a single value.

These functions are especially useful if we retrieve one-dimensional vectors or
if our query results in an array of instances.

#### How it is done usually

```python
# [ (Some(1),), (Some(2),), (Some(3),), ]
session.execute(select(Some)).all()
```

#### Forcing one dimension

```python
# [Some(1), Some(2), Some(3)]
session.scalars(select(Some)).all()
```

#### How to retrieve top of the table as sole item

```python
# Some(1)
session.scalar(select(Some).limit(1))
```

### Round function

```sql
SELECT ROUND(val, 2) FROM t1;
```

```python
from sqlalchemy.sql import func

select(func.round(T1.val, 2))
```

### Aggregates

#### Count all

```sql
SELECT COUNT(*) FROM t1;
```

```python
from sqlalchemy.sql.functions import count

statement = select(count()).select_from(T1)

rows_count = session.scalar(statement)
```

#### Count distinct aggregate

```sql
SELECT COUNT(DISTINCT(val)) FROM t1;
```

```python
from sqlalchemy import distinct
from sqlalchemy.sql.functions import count

statement = select(
    count(distinct(T1.val))
)

x = session.scalar(statement)
```

#### Min aggregate

```sql
SELECT MIN(val) FROM t1;
```

```python
from sqlalchemy.sql import functions
statement = select(functions.min(T1.val))
x = session.scalar(statement)
```

#### Max aggregate

```sql
SELECT MAX(val) FROM t1;
```

```python
from sqlalchemy.sql import functions
statement = select(functions.max(T1.val))
x = session.scalar(statement)
```

#### Average aggregate

```sql
SELECT AVG(val) FROM t1;
```

```python
from sqlalchemy.sql import func
statement = select(func.avg(T1.val))
x = session.scalar(statement)
```

#### Mix function with aggregate

```sql
SELECT ROUND(AVG(val), 2) FROM t1;
```

```python
from sqlalchemy.sql import func
statement = select(
    func.round(
        func.avg(T1.val),
        2
    )
)
x = session.scalar(statement)
```

### Query with negative condition

```sql
SELECT * FROM t1 WHERE NOT val = 11;
```

```python
from sqlalchemy import not_
select(T1).where(not_(T1.val == 11))
```

### Query with compound conditions

```sql
SELECT * FROM t1 WHERE val >= 0 AND val <= 50;
SELECT * FROM t1 WHERE bla = 'foo' OR bla = 'bar';
SELECT * FROM t1 WHERE val > 100 AND NOT bla = 'foo';
```

```python
from sqlalchemy import and_, or_, not_

# SELECT * FROM t1 WHERE val >= 0 AND val <= 50;
select(T1).where(
    and_(
        T1.val >= 0,
        T1.val <= 50
    )
)

# SELECT * FROM t1 WHERE bla = 'foo' OR bla = 'bar';
select(T1).where(
    or_(
        T1.bla == "foo",
        T1.bla == "bar"
    )
)

# SELECT * FROM t1 WHERE val > 100 AND NOT bla = 'foo';
select(T1).where(
    and_(
        T1.val > 100,
        not_(T1.bla == "foo")
    )
)
```

### Order query results

#### Order by (ascending implied)

```sql
SELECT * FROM t1 ORDER BY val;
```

```python
select(T1).order_by(T1.val)
```

#### Order by descending

```sql
SELECT * FROM t1 ORDER BY val DESC;
```

```python
select(T1).order_by(T1.val.desc())
```

#### Order by ascending and descending

```sql
SELECT * FROM t1 ORDER BY a DESC, b ASC;
```

```python
select(T1).order_by(T1.a.desc(), T1.b.asc())
```

### Text query

#### Pattern - LIKE

```sql
SELECT * FROM t1 WHERE bla LIKE 'q%';
SELECT * FROM t1 WHERE bla LIKE '%t';
SELECT * FROM t1 WHERE bla LIKE '%er%';
SELECT * FROM t1 WHERE bla LIKE 'x%y';
SELECT * FROM t1 WHERE bla LIKE '_kek__';
```

```python
select(T1).where(T1.bla.like("q%"))
select(T1).where(T1.bla.like("%t"))
select(T1).where(T1.bla.like("%er%"))
select(T1).where(T1.bla.like("x%y"))
select(T1).where(T1.bla.like("_kek__"))
```

In Sqlite **LIKE** is case-insensitive, whereas in Postgres it is
case-sensitive. Sqlite tackles the case-sensitive pattern matches with an
additional clause **GLOB**.

```sql
SELECT * FROM t1 WHERE bla LIKE 'a%';
SELECT * FROM t1 WHERE bla LIKE 'A%';
SELECT * FROM t1 WHERE bla GLOB 'A*';
```

#### Escape

```sql
SELECT * FROM t1 WHERE d LIKE '%§%%' ESCAPE '§'
```

```python
from sqlalchemy.sql import operators

select(T1.d).where(operators.op(T1.d.like("%§%%"), "ESCAPE", "§"))
```

#### Regexp

```python
select(T1).where(T1.d.regexp_match('^.*[0-9]+'))
```

#### Full-text search (FTS)

TODO

### Grouping

#### Group by a single column

```sql
SELECT x FROM t1 GROUP BY x;
```

```python
select(T1.x).group_by(T1.x)
```

#### Group by multiple columns

```sql
SELECT x, y FROM t1 GROUP BY x, y;
```

```python
select(T1.x).group_by(T1.x, T1.y)
```

#### Count aggregate per group

```sql
SELECT x, COUNT(*) FROM t1 GROUP BY x;
```

```python
select(T1.x, count()).group_by(T1.x, T1.y)
```

#### Average aggregate per group

```sql
SELECT x, ROUND(AVG(y), 2) FROM t1 GROUP BY x;
```

```python
from sqlalchemy.sql import func

select(
    T1.x,
    func.round(
        func.avg(T1.y),
        2
    )
).group_by(T1.x, T1.y)
```

### Having aggregate compared

**HAVING** is similar to **WHERE** in the sense that it is used to filter, but
unlike **WHERE** it filters after the query and it works only in conjunction
with **GROUP BY**.

#### HAVING clause with direct aggregate

```sql
SELECT x, COUNT(*) FROM t1
GROUP BY x HAVING AVG(y) > 100;
```

```python
from sqlalchemy.sql import func
from sqlalchemy.sql.functions import count

select(T1.x, count()).group_by(T1.x).having(func.avg(T1.y) > 100)
```

#### HAVING clause with labeled aggregate

```sql
SELECT x, COUNT(*) AS group_count FROM t1
GROUP BY x HAVING group_count > 5;
```

```python
from sqlalchemy.sql import func
from sqlalchemy.sql.functions import count

group_count = count().label("group_count")
select(
    T1.x,
    group_count
).group_by(T1.x).having(group_count > 5)
```

### Expressions

```sql
SELECT a, b * 2 as b_dup FROM t1;
```

```python
select(T1.a, (T1.b * 2).label("b_dup"))
```

### IS NULL operator

```sql
SELECT * FROM t1 WHERE x ISNULL;
```

```python
select(T1).where(T1.x.is_(None))
```

### IS NOT NULL operator

```sql
SELECT * FROM t1 WHERE x NOTNULL;
```

```python
select(T1).where(T1.x.is_not(None))
```

### IN operator

```sql
SELECT * FROM t1 WHERE x IN (1, 2, 3);
```

```python
select(T1).where(T1.x.in_([1, 2, 3]))
```

### BETWEEN operator

```sql
SELECT * FROM t1 WHERE x BETWEEN 42 AND 9000
```

```python
select(T1).where(T1.x.between(42, 9000))
```

### EXISTS operator (specific value)

```sql
SELECT EXISTS(SELECT * FROM t1 WHERE x = 42);
```

```python
from sqlalchemy.sql import exists

query = select(
    exists().select_from(T1).where(T1.x == 42)
)

result = session.scalar(query)
```

or

```python
select(T1).where(T1.x == 42).exists()
```

### EXISTS operator as condition

```sql
SELECT * FROM t1 WHERE EXISTS(SELECT * FROM t2 WHERE t2.k = t1.x);
```

```sql
select(T1).where(
    select(T2).where(T2.k == T1.x).exists()
)
```

### Compare subquery (works only with 1 scalar)

```sql
SELECT * FROM t1 WHERE x = (SELECT MAX(k) FROM t2);
```

```python
from sqlalchemy.sql import functions
t2_max = select(functions.max(T2.k))
select(T1).where(T1.x = t2_max)
```

### Compare to any in subquery

```sql
SELECT * FROM t1 WHERE x > ANY(SELECT k FROM t2);
```

```python
from sqlalchemy import any_

t2_vals = select(T2.k)
select(T1).where(T1.x > any_(t2_vals))
```

### Compare to all in subquery

```sql
SELECT * FROM t1 WHERE x > ALL(SELECT k FROM t2);
```

```python
from sqlalchemy import all_

t2_vals = select(T2.k)
select(T1).where(T1.x > all_(t2_vals))
```

### Correlated subquery

```sql
SELECT x, (SELECT k FROM t2 WHERE t2.k = t1.x) FROM t1;
SELECT x FROM t1 WHERE (SELECT k FROM t2 WHERE t2.k = t1.x);
```

```python
select(T1.x).where(select(T2.k).where(T2.k == T1.x))
```

### Constraints

#### Default

```sql
CREATE TABLE t1 (a INT DEFAULT 123);
```

```python
class T1(Base):
    pk = Column(Integer, primary_key=True)
    a = Column(Integer, default=123)
```

#### Constraint not null

```sql
CREATE TABLE t1 (a INT NOT NULL);
```

```python
class T1(Base):
    pk = Column(Integer, primary_key=True)
    a = Column(Integer, nullable=False)
```

#### Constraint unique

```sql
CREATE TABLE t1 (a INT UNIQUE);
```

```python
class T1(Base):
    pk = Column(Integer, primary_key=True)
    a = Column(Integer, unique=True)
```

#### Constraint primary key

```sql
CREATE TABLE t1 (a INT PRIMARY KEY);
CREATE TABLE t1 (a INT, PRIMARY KEY(a));
CREATE TABLE t1 (a INT, CONSTRAINT mypk1 PRIMARY KEY(a));
```

```python
class T1(Base):
    pk = Column(Integer, primary_key=True)
```

#### Constraint primary key on multiple columns

```sql
CREATE TABLE t1 (
    a INT,
    b INT,
    PRIMARY KEY (a, b)
);

CREATE TABLE t1 (
    a INT,
    b INT,
    CONSTRAINT pkcombo_1 PRIMARY KEY (a, b)
);
```

#### Constraint foreign key (sqlite)

FK doesn't necessarily have to refer to a PK. It can be any field.

```sql
CREATE TABLE t2 (
    t1_ref INT,
    FOREIGN KEY (t1_ref) REFERENCES t1(a)
);

CREATE TABLE t2 (
    t1_ref INT,
    CONSTRAINT fk1 FOREIGN KEY (t1_ref) REFERENCES t1(a)
);
```

#### Constraint check

```sql
CREATE TABLE t1 (a INT CHECK (a < 100));
CREATE TABLE t1 (a INT, CHECK (a < 100));
CREATE TABLE t1 (a INT, CONSTRAINT mycheck1 CHECK (a < 100));
```

### Transactions

#### Transaction with commit

```sql
BEGIN [TRANSACTION];
    INSERT INTO t1 VALUES (11);
    UPDATE t2 SET k = 'bla';
    DELETE FROM t3;
END [TRANSACTION];

BEGIN [TRANSACTION];
    INSERT INTO t1 VALUES (11);
    UPDATE t2 SET k = 'bla';
    DELETE FROM t3;
COMMIT [TRANSACTION];
```

#### Transaction with rollback

```sql
BEGIN;
    INSERT INTO t1 VALUES (11);
    UPDATE t2 SET k = 'bla';
    DELETE FROM t3;
ROLLBACK;
```

### Unions

#### Union (of rows)

```sql
SELECT x FROM t1
UNION
SELECT k FROM t2;
```

#### Union with aliases

```sql
SELECT b as lol, a as kek FROM t1
UNION
SELECT y as lol, x as kek FROM t2
ORDER BY kek;
```

#### union all

```sql
SELECT a as kek FROM t1
UNION ALL
SELECT x as kek FROM t2;
```

#### Union column order matters

```sql
SELECT b, a FROM t1
UNION
SELECT x, y FROM t2;
```

b will combine with x, a will combine with y

### Intersect

Unlike **UNION**, **INTERSECT** will output only does values that exist in both
tables

```sql
SELECT x FROM t1
INTERSECT
SELECT k FROM t2;

SELECT x, y FROM t1
INTERSECT
SELECT k, p FROM t2;
```

### Except

Unlike INTERSECT, EXCEPT will output only does values that are NOT common in
both tables. Essentially is the opposite of INTERSECT.

```sql
SELECT x FROM t1
EXCEPT
SELECT k FROM t2;

SELECT x, y FROM t1
EXCEPT
SELECT k, p FROM t2;
```

### Joins

**JOIN** will combine columns. **ON** and **USING** clauses are for filtering
which of the rows should pass. It is usually used as a cross-table condition

**JOIN** with an **ON** or **USING** clause will combine rows only if the
cross-condition is true.

Selecting all from an inner join will show the crossing column from both tables.

#### Inner join

```sql
SELECT * FROM t1 [INNER] JOIN t2 ON t1.k = t2.k;
```

Selecting all from an inner join with **USING** clause on a specific column will
show that column only once (unlike the **INNER JOIN** with **ON**)

#### Inner join using

```sql
SELECT * FROM t1 JOIN t2 USING(k);
```

Natural joins will look for all columns that have the same name and they will
use those for cross-checking.

#### Natural join

```sql
SELECT * FROM t1 NATURAL JOIN t2;
```

#### Cross product of all the rows from both tables

##### Comma cross join

```sql
SELECT * FROM t1, t2;
```

##### Sqlite no-ON inner cross join

```sql
SELECT * FROM t1 JOIN t2;
```

##### Postgres ON TRUE inner cross join

Basically an **ON** filter where everything passes.

```sql
SELECT * FROM t1 JOIN t2 ON TRUE;
```

##### Cross join

```sql
SELECT * FROM t1 CROSS JOIN t2;
```

#### Filter by the column of another table.

##### Filter by inner join on different columns

Analogous to **INNER JOIN** on different columns.

```sql
SELECT * FROM t1 JOIN t2 ON t1.a = t2.k;
```

##### Filter in scalar subquery

```sql
SELECT * FROM t1 WHERE t1.x IN (SELECT k FROM t2);
```

##### Filter with **EXISTS** operator in a correlated subquery (slow)

```sql
SELECT * FROM t1
WHERE EXISTS(
    SELECT a FROM t2 WHERE a = t1.x
);
```

#### Outer joins

Include rows from joining tables that don't necessarily pass the ON cross-check.
Otherwise said **INNER JOIN** + rows from tables that don't match anything in
the right.

##### Left join

```sql
SELECT * FROM t1 LEFT OUTER JOIN t2 ON t1.k = t2.k;
```

##### Right join (postgres)

```sql
SELECT * FROM t1 RIGHT OUTER JOIN t2 ON t1.k = t2.k;
```

Sqlite doesn't have **RIGHT OUTER JOIN** so we simply reverse t1 and t2 and use
them in an **LEFT OUTER JOIN**.

##### Right join (sqlite)

```sql
SELECT * FROM t2 LEFT OUTER JOIN t1 ON t1.k = t2.k;
```

##### Full outer join (postgres)

```sql
SELECT * FROM t1 FULL OUTER JOIN t2 ON t1.k = t2.k;
```

##### Full outer join (sqlite)

Sqlite doesn't have **FULL OUTER JOIN** so we make it from **LEFT OUTER JOIN**
and a **RIGHT OUTER JOIN**.

```sql
SELECT * FROM
t1 LEFT JOIN t2 ON t1.k = t2.k
UNION
SELECT * FROM
t2 LEFT JOIN t1 ON t1.k = t2.k;
```

#### Self join

Useful for tables that have relations pointing to itself.

```sql
SELECT * FROM
t1 AS foo INNER JOIN t1 as bar
ON t1.a = t1.b;
```

### Views - queries saved under a name

#### Define a view in <u>sqlite</u>

```sql
CREATE VIEW IF NOT EXISTS view1
AS
    SELECT * FROM t1;
```

#### Define a view in postgres

```sql
CREATE OR REPLACE VIEW view1
AS
    SELECT * FROM t1;
```

#### Query from view

```sql
SELECT * FROM view1;
```

### Indexes - special columns designed to speed up search

```sql
CREATE TABLE IF NOT EXISTS t1 (
    pk int NOT NULL,
    something text NOT NULL,
    val int NOT NULL,

    PRIMARY KEY (pk)
);

CREATE INDEX idx_t1_some ON t1(something);
```
