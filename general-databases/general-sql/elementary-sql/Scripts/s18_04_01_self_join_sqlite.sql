/*
 * JOIN - combines columns from multiple tables
 */

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x int, 
    y int,
    descr text
);

INSERT INTO t1 VALUES
    (11, 22, 'a'),
    (33, 11, 'b'),
    (11, 44, 'c'),
    (66, 11, 'd'),
    (55, 77, 'e')
;

-- title: self inner join same col
SELECT * FROM 
t1 kek INNER JOIN t1 lol
ON kek.x = lol.x;

-- title: self inner join diff col
SELECT * FROM 
t1 kek INNER JOIN t1 lol
ON kek.x = lol.y;

-- title: self outer join diff col
SELECT * FROM 
t1 kek LEFT JOIN t1 lol
ON kek.x = lol.y
ORDER BY kek.x, kek.y, lol.x, lol.y;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
