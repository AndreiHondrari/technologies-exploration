
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x int,
    y text
);

CREATE TABLE IF NOT EXISTS t2 (
    a int,
    b text
);

INSERT INTO t1 VALUES 
    (11, 'a'), 
    (22, 'a'), 
    (11, 'b'), 
    (22, 'c'), 
    (11, 'c'),
    (33, 'c'),
    (55, 'a'),
    (33, 'a');

INSERT INTO t2 VALUES 
    (11, 'b'),
    (22, 'b'),
    (33, 'a');

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
