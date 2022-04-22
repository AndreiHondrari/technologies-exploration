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

-- title: group by one column
SELECT x FROM t1 WHERE x < 500 GROUP BY x;  -- will always pick the first match for a given grouping

-- title: count for each group
SELECT x, COUNT(*) FROM t1 GROUP BY x;

-- title: conditional
SELECT x, COUNT(*) FROM t1 WHERE y > 40 GROUP BY x;

-- title: avg for group
SELECT x, ROUND(AVG(y), 2) FROM t1 WHERE x < 500 GROUP BY x;

-- title: group by multiple
SELECT x, y FROM t1 WHERE x < 500 GROUP BY x, y;

/*
 * While performing a select when grouping by only one column works,
 * the result does not make sense. This is only possible because
 * Sqlite is permissive. It will by default chose the first value
 * of the columns that are not used for grouping.
 * 
 * Why doesn't it make sense?
 * Example: Let's assume we have table (a int, b int) with values
 * (1, 11), (1, 22), (2, 33)
 * 
 * if the "SELECT * FROM table GROUP BY a;" were to work
 * how would the result be for a = 1 ? In column b 
 * there are 11 and 22 for the same a = 1, 
 * which one would you should display? 
 * it wouldn't make sense to display only one of them.
 */
select * from t1 group by x;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
