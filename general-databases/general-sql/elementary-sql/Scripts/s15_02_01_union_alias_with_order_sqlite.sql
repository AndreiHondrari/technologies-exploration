
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    a int,
    b text
);

CREATE TABLE IF NOT EXISTS t2 (
    x int,
    y text
);

INSERT INTO t1 VALUES
    (11, 'gandalf'),
    (55, 'maxime'),
    (99, 'jonas')
;

INSERT INTO t2 VALUES
    (22, 'cassidi'),
    (11, 'malcom'),
    (100, 'lorantae')
;

SELECT b as lol, a as kek FROM t1
UNION
SELECT y as lol, x as kek FROM t2
ORDER BY kek;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
