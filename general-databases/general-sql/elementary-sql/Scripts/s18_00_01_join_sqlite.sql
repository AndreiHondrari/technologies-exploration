/*
 * JOIN - combines columns from multiple tables
 */

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t3;

CREATE TABLE IF NOT EXISTS t1 (
    k int, 
    y int
);

CREATE TABLE IF NOT EXISTS t2 (
    a int, 
    k int
);

CREATE TABLE IF NOT EXISTS t3 (
    k int, 
    y int
);

INSERT INTO t1 VALUES
    (11, 777), 
    (22, 888), 
    (33, 999), 
    (11, 1010)
;

INSERT INTO t2 VALUES
    ('a', 55),
    ('b', 22),
    ('c', 11)
;

INSERT INTO t3 VALUES
    (11, 222),
    (11, 999),
    (11, 777),
    (33, 222),
    (33, 999)
;

-- title: [inner] join
SELECT * FROM t1 JOIN t2;

-- title: join on
SELECT * FROM t1 JOIN t2 ON t1.k = t2.k;

-- title: join using
SELECT * FROM t1 JOIN t2 USING(k);

-- title: natural
-- t1.k as p, t1.y as q, t3.*
SELECT * FROM t1 NATURAL JOIN t3;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t3;
