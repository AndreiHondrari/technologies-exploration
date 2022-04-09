
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    a int
);

CREATE TABLE IF NOT EXISTS t2 (
    b int
);

INSERT INTO t1 VALUES (11), (22), (33), (44), (55);

INSERT INTO t2 VALUES (22), (44);

/*
 * comparison always goes against first result of subquery
 * or subquery must have only one row and one column
 * 
 * could add LIMIT 1 for plus of clarity
 */
-- title: t1 if first in t2 (bef)
SELECT * FROM t1
WHERE a = (SELECT b FROM t2);


DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
