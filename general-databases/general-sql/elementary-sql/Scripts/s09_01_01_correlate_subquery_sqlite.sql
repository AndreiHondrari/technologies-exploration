/*
 * Correlated subqueries are subqueries that
 * make use of columns from the outer query.
 * 
 * They are slow because the subquery is evaluated
 * for each row of the outer query.
 */
DROP TABLE IF EXISTS t3;
DROP TABLE IF EXISTS t4;

CREATE TABLE IF NOT EXISTS t3 (
    x integer
);

CREATE TABLE IF NOT EXISTS t4 (
    x_ref integer,
    k integer
);


INSERT INTO t3 VALUES
    (11), (22), (33), (44), (55), (66), (77);

INSERT INTO t4 VALUES
    (11, 7),
    (11, 29),
    (22, 70),
    (22, 60),
    (33, 29),
    (44, 9000);

-- title: original sums
SELECT x_ref, SUM(k) FROM t4 GROUP BY x_ref;

/*
 * purpose here:
 * get all t3 identities that
 * form a sum large enough on t4 via secondary column
 */
-- title: uncorellated subquery
SELECT x FROM t3 
WHERE x IN (
    SELECT x_ref FROM t4 
    GROUP BY x_ref 
    HAVING SUM(k) > 100
);

-- title: correlated
SELECT x FROM t3 
WHERE 100 < (
    SELECT SUM(k) FROM t4 
    WHERE x_ref = x
);


DROP TABLE IF EXISTS t3;
DROP TABLE IF EXISTS t4;
