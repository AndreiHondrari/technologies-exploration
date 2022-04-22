/*
 *
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
    x integer,
    y integer
);

INSERT INTO t1 VALUES
    (1, 11),
    (2, 22),
    (1, 33),
    (2, 44),
    (1, 33),
    (2, 44),
    (1, 55),
    (2, 44),
    (3, 66);

-- main start

-- title: original
SELECT * FROM t1 ORDER BY x, y;

-- title: having count
SELECT x, COUNT(*) AS "# of items"
FROM t1 
GROUP BY x 
HAVING COUNT(*) > 1;

-- title: normal average
SELECT x, ROUND(AVG(y), 2) as "average y"
FROM t1
GROUP BY x;

-- title: having average
SELECT x, ROUND(AVG(y), 2) as "average y"
FROM t1 
GROUP BY x
HAVING "average y" < 40;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
