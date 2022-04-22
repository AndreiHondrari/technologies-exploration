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
    (3, 55),
    (4, 66),
    (5, 44),
    (6, 55),
    (7, 44),
    (8, 66),
    (9, 66);
    
-- main start

-- title: case in select
SELECT 
    DISTINCT(y),
    CASE
        WHEN y < 40 THEN 'kek'
        WHEN y >= 40 THEN 'lol'
    END woot
FROM t1
ORDER BY y;

-- title: case in where
SELECT * FROM t1
WHERE
    x <= 5 AND
    CASE 
        WHEN x < 3 THEN y <= 40
        WHEN x >= 3 THEN y > 40
    END
ORDER BY x, y;

/*
 * FRAGILE
 * This doesn't work in postgresql (this is sqlite)
 * because of the postgres rule to have all
 * listed select fields in the group by clause
 */
-- title: case in group by
SELECT 
    -- show from which column the value is
    CASE
        WHEN y < 50 THEN 'x'
        WHEN y >= 50 THEN 'y'
    END "which column",
    
    -- show the actual value
    CASE
        WHEN y < 50 THEN x
        WHEN y >= 50 THEN y
    END woot,
    
    -- show the actual value
    CASE
        WHEN y < 50 THEN 'y < 50'
        WHEN y >= 50 THEN 'y >= 50'
    END "why?"
FROM t1
group by
    CASE
        WHEN y < 50 THEN "x"
        WHEN y >= 50 THEN "y"
    END
order by "which column", woot;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
