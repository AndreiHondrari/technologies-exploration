
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    a int
);

CREATE TABLE IF NOT EXISTS t2 (
    b int
);

INSERT INTO t1 VALUES (11), (11), (22), (33), (33), (33);

-- title: t1 if any in t2 (bef)
SELECT * FROM t1
WHERE EXISTS(SELECT * FROM t2);

INSERT INTO t2 VALUES (33);

-- title: t1 if any in t2 (aft)
SELECT * FROM t1
WHERE EXISTS(SELECT * FROM t2);

/*
 * returns a filtered query result set
 * only if there is any of a specific value
 * in another table
 */
-- title: refined exists query
SELECT a FROM t1
WHERE EXISTS(SELECT b FROM t2 WHERE b = 33) AND a = 33;


DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
