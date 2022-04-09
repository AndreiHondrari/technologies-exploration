/*
 * JOIN - combines columns from multiple tables
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
    (11, 777), (22, 888), (33, 999), (11, 1010)
;

INSERT INTO t2 VALUES
    ('a', 55), ('b', 22), ('c', 11), ('d', 11)
;

-- title: join
SELECT * FROM t1 JOIN t2;

-- title: join on
SELECT * FROM t1 JOIN t2 ON x = b;


DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
