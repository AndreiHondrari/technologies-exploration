/*
 * UNION - combines rows from multiple tables
 */

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x, y
);

CREATE TABLE IF NOT EXISTS t2 (
    a, b
);


INSERT INTO t1 VALUES
    (11, 777), (22, 888), (33, 999);

INSERT INTO t2 VALUES
    ('a', 55), ('b', 22), ('c', 11);

-- title: unite
SELECT x FROM t1
UNION
SELECT b FROM t2;

-- title: unite everything
SELECT x, y FROM t1
UNION
SELECT b, a FROM t2;


DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
