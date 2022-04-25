# SQL cheatsheet

## Create table

```sql
CREATE TABLE t1 (val INT, bla VARCHAR(30));
```

## Create table if it doesn't exist

```sql
CREATE TABLE IF NOT EXISTS t1 (val INT, bla VARCHAR(30));
```

## Drop table

```sql
DROP TABLE t1;
```

## Drop table if it exists

```sql
DROP TABLE IF EXISTS t1;
```

## Insert a single value

```sql
INSERT INTO t1 VALUES (11, 'bla');
```

## Query all rows

```sql
SELECT * FROM t1;
```

## Query specific column

```sql
SELECT bla FROM t1;
```

## Query with condition

```sql
SELECT * FROM t1 WHERE val >= 42;
```

## Insert multiple rows

```sql
INSERT INTO t1 VALUES
    (11, 'bla'),
    (22, 'kek'),
    (33, 'lol');
```

## Copy insert from one table to another

```sql
INSERT INTO t2 SELECT a, b FROM t2
```

## Delete all rows

```sql
DELETE FROM t1;
```

## Delete specific row

```sql
DELETE FROM t1 WHERE val = 42;
```

## Update column with specific value on all rows

```sql
UPDATE t1 SET bla = 'foo';
```

## Update column with specific value on condition

```sql
UPDATE t1 SET bla = 'foo' WHERE val = 42;
```

## Query distinct values on column

```sql
SELECT DISTINCT(val) FROM t1;
```

## Round function

```sql
SELECT ROUND(val, 2) FROM t1;
```

## Aggregates

### Count all

```sql
SELECT COUNT(*) FROM t1;
```

### Count distinct aggregate

```sql
SELECT COUNT(DISTINCT(val)) FROM t1;
```

### Min aggregate

```sql
SELECT MIN(val) FROM t1;
```

### Max aggregate

```sql
SELECT MAX(val) FROM t1;
```

### Average aggregate

```sql
SELECT AVG(val) FROM t1;
```

### Mix function with aggregate

```sql
SELECT ROUND(AVG(val), 2) FROM t1;
```

## Query with negative condition

```sql
SELECT * FROM t1 WHERE NOT val = 11;
```

## Query with compound conditions

```sql
SELECT * FROM t1 WHERE val >= 0 AND val <= 50;
SELECT * FROM t1 WHERE bla = 'foo' OR bla = 'bar';
SELECT * FROM t1 WHERE val > 100 AND NOT bla = 'foo';
```

## Order query results

### Order by (ascending implied)

```sql
SELECT * FROM t1 ORDER BY val;
```

### Order by descending

```sql
SELECT * FROM t1 ORDER BY val DESC;
```

### Order by ascending and descending

```sql
SELECT * FROM t1 ORDER BY a DESC, b ASC;
```

## Limit query results

```sql
SELECT * FROM t1 LIMIT 5;
```

## Text query

### Pattern - starts with letter

```sql
SELECT * FROM t1 WHERE bla LIKE 'q%';
```

### Pattern - ends with letter

```sql
SELECT * FROM t1 WHERE bla LIKE '%t';
```

### Pattern - contains letters

```sql
SELECT * FROM t1 WHERE bla LIKE '%er%';
```

### Pattern - starts and ends with letter

```sql
SELECT * FROM t1 WHERE bla LIKE 'x%y';
```

### Pattern - has specific letters and any letters

```sql
SELECT * FROM t1 WHERE bla LIKE '_kek__';
```

In Sqlite **LIKE** is case-insensitive, whereas in Postgres it is
case-sensitive. Sqlite tackles the case-sensitive pattern matches with an
additional clause **GLOB**.

```sql
SELECT * FROM t1 WHERE bla LIKE 'a%';
SELECT * FROM t1 WHERE bla LIKE 'A%';
SELECT * FROM t1 WHERE bla GLOB 'A*';
```

## Grouping

### Group by a single column

```sql
SELECT x FROM t1 GROUP BY x;
```

### Group by multiple columns

```sql
SELECT x, y FROM t1 GROUP BY x, y;
```

### Count aggregate per group

```sql
SELECT x, COUNT(*) FROM t1 GROUP BY x;
```

### Average aggregate per group

```sql
SELECT x, ROUND(AVG(y), 2) FROM t1 GROUP BY x;
```

## Having aggregate compared

**HAVING** is similar to **WHERE** in the sense that it is used to filter, but
unlike **WHERE** it filters after the query and it works only in conjunction
with **GROUP BY**.

### HAVING clause with direct aggregate

```sql
SELECT x, COUNT(*) FROM t1
GROUP BY x HAVING AVG(y) > 100;
```

### HAVING clause with labeled aggregate

```sql
SELECT x, COUNT(*) AS group_count FROM t1
GROUP BY x HAVING group_count > 5;
```

## Expressions

```sql
SELECT a, b * 2 as b_dup FROM t1;
```

## IS NULL operator

```sql
SELECT * FROM t1 WHERE x ISNULL;
```

## IS NOT NULL operator

```sql
SELECT * FROM t1 WHERE x NOTNULL;
```

## IN operator

```sql
SELECT * FROM t1 WHERE x IN (1, 2, 3);
```

## BETWEEN operator

```sql
SELECT * FROM t1 WHERE x BETWEEN 42 AND 9000
```

## EXISTS operator (specific value)

```sql
SELECT EXISTS(SELECT * FROM t1 WHERE X = 42);
```

## EXISTS operator as condition

```sql
SELECT * FROM t1 WHERE EXISTS(SELECT * FROM t2 WHERE t2.k = t1.x);
```

## Compare subquery (works only with 1 scalar)

```sql
SELECT * FROM t1 WHERE x = (SELECT MAX(k) FROM t2);
```

## Compare to any in subquery

```sql
SELECT * FROM t1 WHERE x > ANY(SELECT k FROM t2);
```

## Compare to all in subquery

```sql
SELECT * FROM t1 WHERE x > ALL(SELECT k FROM t2);
```

## Correlated subquery

```sql
SELECT x, (SELECT k FROM t2 WHERE t2.k = t1.x) FROM t1;
SELECT x FROM t1 WHERE (SELECT k FROM t2 WHERE t2.k = t1.x);
```

## Constraints

### Default

```sql
CREATE TABLE t1 (a INT DEFAULT 123);
```

### Constraint not null

```sql
CREATE TABLE t1 (a INT NOT NULL);
```

### Constraint unique

```sql
CREATE TABLE t1 (a INT UNIQUE);
```

### Constraint primary key

```sql
CREATE TABLE t1 (a INT PRIMARY KEY);
CREATE TABLE t1 (a INT, PRIMARY KEY(a));
CREATE TABLE t1 (a INT, CONSTRAINT mypk1 PRIMARY KEY(a));
```

### Constraint primary key on multiple columns

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

### Constraint foreign key (sqlite)

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

### Constraint check

```sql
CREATE TABLE t1 (a INT CHECK (a < 100));
CREATE TABLE t1 (a INT, CHECK (a < 100));
CREATE TABLE t1 (a INT, CONSTRAINT mycheck1 CHECK (a < 100));
```

## Transactions

### Transaction with commit

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

### Transaction with rollback

```sql
BEGIN;
    INSERT INTO t1 VALUES (11);
    UPDATE t2 SET k = 'bla';
    DELETE FROM t3;
ROLLBACK;
```

## Unions

### Union (of rows)

```sql
SELECT x FROM t1
UNION
SELECT k FROM t2;
```

### Union with aliases

```sql
SELECT b as lol, a as kek FROM t1
UNION
SELECT y as lol, x as kek FROM t2
ORDER BY kek;
```

### union all

```sql
SELECT a as kek FROM t1
UNION ALL
SELECT x as kek FROM t2;
```

### Union column order matters

```sql
SELECT b, a FROM t1
UNION
SELECT x, y FROM t2;
```

b will combine with x, a will combine with y

## Intersect

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

## Except

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

## Joins

**JOIN** will combine columns. **ON** and **USING** clauses are for filtering
which of the rows should pass. It is usually used as a cross-table condition

**JOIN** with an **ON** or **USING** clause will combine rows only if the
cross-condition is true.

Selecting all from an inner join will show the crossing column from both tables.

### Inner join

```sql
SELECT * FROM t1 [INNER] JOIN t2 ON t1.k = t2.k;
```

Selecting all from an inner join with **USING** clause on a specific column will
show that column only once (unlike the **INNER JOIN** with **ON**)

### Inner join using

```sql
SELECT * FROM t1 JOIN t2 USING(k);
```

Natural joins will look for all columns that have the same name and they will
use those for cross-checking.

### Natural join

```sql
SELECT * FROM t1 NATURAL JOIN t2;
```

### Cross product of all the rows from both tables

#### Comma cross join

```sql
SELECT * FROM t1, t2;
```

#### Sqlite no-ON inner cross join

```sql
SELECT * FROM t1 JOIN t2;
```

#### Postgres ON TRUE inner cross join

Basically an **ON** filter where everything passes.

```sql
SELECT * FROM t1 JOIN t2 ON TRUE;
```

#### Cross join

```sql
SELECT * FROM t1 CROSS JOIN t2;
```

### Filter by the column of another table.

#### Filter by inner join on different columns

Analogous to **INNER JOIN** on different columns.

```sql
SELECT * FROM t1 JOIN t2 ON t1.a = t2.k;
```

#### Filter in scalar subquery

```sql
SELECT * FROM t1 WHERE t1.x IN (SELECT k FROM t2);
```

#### Filter with **EXISTS** operator in a correlated subquery (slow)

```sql
SELECT * FROM t1
WHERE EXISTS(
    SELECT a FROM t2 WHERE a = t1.x
);
```

### Outer joins

Include rows from joining tables that don't necessarily pass the ON cross-check.
Otherwise said **INNER JOIN** + rows from tables that don't match anything in
the right.

#### Left join

```sql
SELECT * FROM t1 LEFT OUTER JOIN t2 ON t1.k = t2.k;
```

#### Right join (postgres)

```sql
SELECT * FROM t1 RIGHT OUTER JOIN t2 ON t1.k = t2.k;
```

Sqlite doesn't have **RIGHT OUTER JOIN** so we simply reverse t1 and t2 and use
them in an **LEFT OUTER JOIN**.

#### Right join (sqlite)

```sql
SELECT * FROM t2 LEFT OUTER JOIN t1 ON t1.k = t2.k;
```

#### Full outer join (postgres)

```sql
SELECT * FROM t1 FULL OUTER JOIN t2 ON t1.k = t2.k;
```

#### Full outer join (sqlite)

Sqlite doesn't have **FULL OUTER JOIN** so we make it from **LEFT OUTER JOIN**
and a **RIGHT OUTER JOIN**.

```sql
SELECT * FROM
t1 LEFT JOIN t2 ON t1.k = t2.k
UNION
SELECT * FROM
t2 LEFT JOIN t1 ON t1.k = t2.k;
```

### Self join

Useful for tables that have relations pointing to itself.

```sql
SELECT * FROM
t1 AS foo INNER JOIN t1 as bar
ON t1.a = t1.b;
```

## Views - queries saved under a name

### Define a view in <u>sqlite</u>

```sql
CREATE VIEW IF NOT EXISTS view1
AS
    SELECT * FROM t1;
```

### Define a view in postgres

```sql
CREATE OR REPLACE VIEW view1
AS
    SELECT * FROM t1;
```

### Query from view

```sql
SELECT * FROM view1;
```

## Indexes - special columns designed to speed up search

```sql
CREATE TABLE IF NOT EXISTS t1 (
    pk int NOT NULL,
    something text NOT NULL,
    val int NOT NULL,

    PRIMARY KEY (pk)
);

CREATE INDEX idx_t1_some ON t1(something);
```
