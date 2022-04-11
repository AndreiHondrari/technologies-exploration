
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    a int
);

CREATE TABLE IF NOT EXISTS t2 (
    x int
);

INSERT INTO t1 VALUES
    (11),
    (55),
    (99)
;

INSERT INTO t2 VALUES
    (22),
    (11),
    (55)
;

-- title: union simple
SELECT a as kek FROM t1
UNION
SELECT x as kek FROM t2;

-- title: union all
SELECT a as kek FROM t1
UNION ALL
SELECT x as kek FROM t2;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
