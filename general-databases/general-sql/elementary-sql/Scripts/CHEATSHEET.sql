-- create table
CREATE TABLE t1 (val INT, bla VARCHAR(30));

-- create if not exists
CREATE TABLE IF NOT EXISTS t1 (val INT, bla VARCHAR(30));

-- drop table
DROP TABLE t1;

-- drop if exists
DROP TABLE IF EXISTS t1;

-- insert
INSERT INTO t1 VALUES (11, 'bla');

-- select all
SELECT * FROM t1;

-- select field
SELECT bla FROM t1;

-- select where
SELECT * FROM t1 WHERE val >= 42;

-- insert multiple
INSERT INTO t1 VALUES
    (11, 'bla'),
    (22, 'kek'),
    (33, 'lol');

-- copy insert
INSERT INTO t2 SELECT a, b FROM t2

-- delete all
DELETE FROM t1;

-- delete specific
DELETE FROM t1 WHERE val = 42;

-- update all
UPDATE t1 SET bla = 'foo';

-- update specific
UPDATE t1 SET bla = 'foo' WHERE val = 42;

-- select distinct
SELECT DISTINCT(val) FROM t1;

-- count all
SELECT COUNT(*) FROM t1;

-- count distinct
SELECT COUNT(DISTINCT(val)) FROM t1;

-- min
SELECT MIN(val) FROM t1;

-- max
SELECT MAX(val) FROM t1;

-- average
SELECT AVG(val) FROM t1;

-- round
SELECT ROUND(val, 2) FROM t1;

-- mix function with aggregate
SELECT ROUND(AVG(val), 2) FROM t1;

-- negative condition
SELECT * FROM t1 WHERE NOT val = 11;

-- select with compound conditions
SELECT * FROM t1 WHERE val >= 0 AND val <= 50;
SELECT * FROM t1 WHERE bla = 'foo' OR bla = 'bar';
SELECT * FROM t1 WHERE val > 100 AND NOT bla = 'foo';

-- order by (ascending implied)
SELECT * FROM t1 ORDER BY val;

-- order by descending
SELECT * FROM t1 ORDER BY val DESC;

-- order by ascending and descending
SELECT * FROM t1 ORDER BY a DESC, b ASC;

-- limit
SELECT * FROM t1 LIMIT 5;

-- like pattern (starts with letter)
SELECT * FROM t1 WHERE bla LIKE 'q%';

-- like pattern (ends with letter)
SELECT * FROM t1 WHERE bla LIKE '%t';

-- like pattern (contains letters)
SELECT * FROM t1 WHERE bla LIKE '%er%';

-- like pattern (starts and ends with letter)
SELECT * FROM t1 WHERE bla LIKE 'x%y';

-- like pattern (has specific letters and any letters)
SELECT * FROM t1 WHERE bla LIKE '_kek__';

/*
 * In Sqlite LIKE is case-insensitive
 * whereas in Postgres it is case-sensitive.
 * Sqlite tackles the case-sensitive pattern
 * matches with an additional clause GLOB.
 */
SELECT * FROM t1 WHERE bla LIKE 'a%';
SELECT * FROM t1 WHERE bla LIKE 'A%';
SELECT * FROM t1 WHERE bla GLOB 'A*';

-- group by
SELECT x FROM t1 GROUP BY x;

-- group by multiple
SELECT x, y FROM t1 GROUP BY x, y;

-- count per group
SELECT x, COUNT(*) FROM t1 GROUP BY x;

-- average per group
SELECT x, ROUND(AVG(y), 2) FROM t1 GROUP BY x;

/*
 * HAVING is similar to WHERE
 * in the sense that it is used to filter
 * but unlike WHERE it filters after the query and
 * it works only in conjunction with GROUP BY
 */

-- having aggregate compared
SELECT x, COUNT(*) FROM t1
GROUP BY x HAVING AVG(y) > 100;

-- having with labeled aggregate
SELECT x, COUNT(*) AS group_count FROM t1
GROUP BY x HAVING group_count > 5;

-- expressions
SELECT a, b * 2 as b_dup FROM t1;

-- is null
SELECT * FROM t1 WHERE x ISNULL;

-- is not null
SELECT * FROM t1 WHERE x NOTNULL;

-- in
SELECT * FROM t1 WHERE x IN (1, 2, 3);

-- between
SELECT * FROM t1 WHERE x BETWEEN 42 AND 9000

-- exists (specific value)
SELECT EXISTS(SELECT * FROM t1 WHERE X = 42);

-- exists as condition
SELECT * FROM t1 WHERE EXISTS(SELECT * FROM t2 WHERE t2.k = t1.x);

-- compare subquery (works only with 1 scalar)
SELECT * FROM t1 WHERE x = (SELECT MAX(k) FROM t2);

-- compare to any in subquery
SELECT * FROM t1 WHERE x > ANY(SELECT k FROM t2);

-- compare to all in subquery
SELECT * FROM t1 WHERE x > ALL(SELECT k FROM t2);

-- correlated subquery
SELECT x, (SELECT k FROM t2 WHERE t2.k = t1.x) FROM t1;
SELECT x FROM t1 WHERE (SELECT k FROM t2 WHERE t2.k = t1.x);

-- default
CREATE TABLE t1 (a INT DEFAULT 123);

-- constraint not null
CREATE TABLE t1 (a INT NOT NULL);

-- constraint unique
CREATE TABLE t1 (a INT UNIQUE);

-- constraint primary key
CREATE TABLE t1 (a INT PRIMARY KEY);
CREATE TABLE t1 (a INT, PRIMARY KEY(a));
CREATE TABLE t1 (a INT, CONSTRAINT mypk1 PRIMARY KEY(a));

-- constraint primary key on multiple columns
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

/*
 * FK doesn't necessarily have to
 * refer to a PK. It can be any field.
 */
-- constraint foreign key (sqlite)
CREATE TABLE t2 (
    t1_ref INT,
    FOREIGN KEY (t1_ref) REFERENCES t1(a)
);

CREATE TABLE t2 (
    t1_ref INT,
    CONSTRAINT fk1 FOREIGN KEY (t1_ref) REFERENCES t1(a)
);

-- constraint check
CREATE TABLE t1 (a INT CHECK (a < 100));
CREATE TABLE t1 (a INT, CHECK (a < 100));
CREATE TABLE t1 (a INT, CONSTRAINT mycheck1 CHECK (a < 100));

-- transaction with commit
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

-- transaction with rollback
BEGIN;
    INSERT INTO t1 VALUES (11);
    UPDATE t2 SET k = 'bla';
    DELETE FROM t3;
ROLLBACK;

-- union (of rows)
SELECT x FROM t1
UNION
SELECT k FROM t2;

SELECT b as lol, a as kek FROM t1
UNION
SELECT y as lol, x as kek FROM t2
ORDER BY kek;
