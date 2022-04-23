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
    (11, 1010),
    (66, 888);

INSERT INTO t2 VALUES
    ('a', 55), 
    ('b', 22), 
    ('c', 11),
    ('b', 77),
    ('d', 22);

/*
 * compare to an inner join
 * it simply inserts NULL for the counterpart
 * columns of the other table
 * when no actual match is met
 */
-- title: left outer join
SELECT * 
FROM t1 LEFT OUTER JOIN t2
ON t1.k = t2.k
ORDER BY t1.k;

/*
 * sqlite does not have
 * right outer join
 * 
 * so we simply invert 
 * t1 JOIN t2 -> t2 JOIN t1
 * 
 * to obtain the desired efect
 */
-- title: right outer join
SELECT t1.*, t2.* 
FROM t2 LEFT OUTER JOIN t1
ON t1.k = t2.k
ORDER BY t2.k;

/*
 * sqlite also does not have
 * FULL OUTER JOIN
 * 
 * we improvise by doing
 * (left join) union (right join)
 * on the two tables
 */
-- title: full outer join
SELECT t1.*, t2.*
FROM t1 LEFT OUTER JOIN t2
ON t1.k = t2.k
UNION
SELECT t1.*, t2.*
FROM t2 LEFT OUTER JOIN t1
ON t1.k = t2.k;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
