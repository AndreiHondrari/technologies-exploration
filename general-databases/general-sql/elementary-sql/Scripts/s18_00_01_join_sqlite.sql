/*
 * JOIN - combines columns from multiple tables
 */

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    k int, 
    y int
);

CREATE TABLE IF NOT EXISTS t2 (
    a text, 
    k int
);

INSERT INTO t1 VALUES
    (11, 777), 
    (22, 888), 
    (33, 999), 
    (11, 1010);

INSERT INTO t2 VALUES
    ('a', 55),
    ('b', 22),
    ('c', 11),
    ('d', 22);

-- title: [inner] join on
SELECT * FROM t1 JOIN t2 ON t1.k = t2.k;

-- title: join using
SELECT * FROM t1 JOIN t2 USING(k);

-- title: natural
SELECT * FROM t1 NATURAL JOIN t2;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
