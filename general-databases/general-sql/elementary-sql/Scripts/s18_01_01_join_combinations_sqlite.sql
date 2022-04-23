
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x int
);

CREATE TABLE IF NOT EXISTS t2 (
    a text
);

INSERT INTO t1 VALUES
    (11),
    (22),
    (33);

INSERT INTO t2 VALUES
    ('gandalf'),
    ('maxime'),
    ('jeff');

-- title: comma join
SELECT * FROM t1, t2;

-- title: join (no on)
SELECT * FROM t1 JOIN t2;

-- title: cross join
SELECT * FROM t1 CROSS JOIN t2;


DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
