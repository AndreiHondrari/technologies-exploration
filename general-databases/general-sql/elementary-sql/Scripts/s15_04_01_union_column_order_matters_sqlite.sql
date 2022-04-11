
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    a int,
    b int
);

CREATE TABLE IF NOT EXISTS t2 (
    x int,
    y int
);

INSERT INTO t1 VALUES
    (11, 'gandalf'),
    (55, 'maxime'),
    (99, 'jonas')
;

INSERT INTO t2 VALUES
    (22, 'cassidi'),
    (66, 'malcom'),
    (100, 'lorantae')
;

-- title: weird mix
SELECT b, a FROM t1
UNION
SELECT x, y FROM t2
;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
