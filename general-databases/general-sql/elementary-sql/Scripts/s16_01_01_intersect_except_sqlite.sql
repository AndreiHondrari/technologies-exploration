
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x int
);

CREATE TABLE IF NOT EXISTS t2 (
    a int
);

INSERT INTO t1 VALUES (11), (22), (33), (44), (55);

INSERT INTO t2 VALUES (11), (33);

-- title: intersect
SELECT * FROM t1
INTERSECT
SELECT * FROM t2;

-- title: except
SELECT * FROM t1
EXCEPT
SELECT * FROM t2;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
