
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x int,
    descr text
);

CREATE TABLE IF NOT EXISTS t2 (
    a int
);

INSERT INTO t1 VALUES
    (11, 'gandalf'),
    (55, 'maxime'),
    (99, 'jonas'),
    (55, 'hermione'),
    (77, 'broko'),
    (11, 'admiral');

INSERT INTO t2 VALUES
    (11),
    (55);

-- title: inner join
SELECT t1.* FROM t1 JOIN t2 ON t1.x = t2.a;

-- title: analogous subquery
SELECT *
FROM t1
WHERE t1.x IN (SELECT a FROM t2);

-- title: analogous exists
SELECT *
FROM t1
WHERE EXISTS(SELECT a FROM t2 WHERE a = t1.x);


DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
